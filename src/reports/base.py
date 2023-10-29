from fpdf import FPDF
from fpdf.enums import XPos, YPos
import sqlite3
import datetime as dt
from tkinter import filedialog, messagebox

class PDF(FPDF):
    def header(self):
        self.set_font('Courier','B', 24)
        self.cell(
            w=195, h=15, text='Base Material Report', align='C', border=1,
            new_y=YPos.NEXT, new_x=XPos.LMARGIN
        )

    def footer(self):
        self.set_y(-15)
        self.set_font('Courier', 'I', 14)
        self.cell(w=65, h=10, text=f'Page {self.page_no()}/{{nb}}')
        self.cell(w=65, h=10, text='SimpleInks')
        self.cell(w=65, h=10, text=str(dt.datetime.today()).split('.')[0], align='R')

class Report:
    def __init__(self, database, base):
        self.database = database
        self.base_name = base
        self.page_setup()
        self.import_info()
        self.compile_data()
        self.create_table()
        self.ghs_label()
        self.save_report()

    def page_setup(self):
        self.pdf = PDF(orientation='portrait', format='letter', unit='mm')
        self.pdf.alias_nb_pages()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()

    def import_info(self):
        sql = '''SELECT base_name, alt_name, lb_cost, health, flammable,
        reactive, ppe, warning_level, revision_version, notes, description,
        vendor, system, gallon_lb FROM bases WHERE base_name = ?'''
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        self.record = cur.execute(sql, (self.base_name,)).fetchone()
        sql = '''SELECT voc, amount FROM base_voc WHERE base = ?'''
        self.vocs = cur.execute(sql, (self.base_name,)).fetchall()
        print(self.vocs)
        con.close()

    def compile_data(self):
        base_name, alt_name, lb_cost, self.health, self.flammable,\
        self.reactive, self.ppe, warning_level, self.revision_version, notes, \
        description, vendor, system, gallon_lb = self.record
        height = 10
        self.pdf.cell(w=0, h=height, new_y=YPos.NEXT, new_x=XPos.LMARGIN)
        # Title
        self.pdf.set_font('Courier', '', 18)
        # Base Name Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=40, h=height, text='Base Name:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=height, text=base_name,new_y=YPos.NEXT,
            new_x=XPos.LMARGIN
        )
        # Alternative Name Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=68, h=height, text='Alternative Name:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=height, text=alt_name,new_y=YPos.NEXT,
            new_x=XPos.LMARGIN
        )
        # Pound Cost Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=52, h=height, text='Price Per Lb:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=height, text='$'+str(lb_cost),new_y=YPos.NEXT,
            new_x=XPos.LMARGIN
        )
        # Warning Levels Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=92, h=height, text='Inventory Warning Level:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=height, text=str(warning_level) + ' lbs.',new_y=YPos.NEXT,
            new_x=XPos.LMARGIN
        )
        # Vendor Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=28, h=height, text='Vendor:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=height, text=vendor, new_y=YPos.NEXT,
            new_x=XPos.LMARGIN
        )
        # Ink System Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=43, h=height, text='Ink System:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=height, text=system, new_y=YPos.NEXT,
            new_x=XPos.LMARGIN
        )
        # Pound Per Gallon Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=55, h=height, text='Lbs. Per Gal.:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=height, text=str(gallon_lb), new_y=YPos.NEXT,
            new_x=XPos.LMARGIN
        )
        # Description Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=38, h=20, text='Description:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=20, text=description,new_y=YPos.NEXT,
            new_x=XPos.LMARGIN, align='C'
        )
        # Notes Information
        self.pdf.set_font('Courier', 'B', 18)
        self.pdf.cell(w=35, h=20, text='Notes:')
        self.pdf.set_font('Courier', '', 18)
        self.pdf.cell(
            w=100, h=20, text=notes, new_y=YPos.NEXT,
            new_x=XPos.LMARGIN, align='C'
        )
    
    def create_table(self):
        self.pdf.cell(w=0, h=5, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        col_width = self.pdf.w / 2.25
        row_height = 10
        self.pdf.set_font('Courier', 'B', 22)
        self.pdf.cell(w=col_width, h=row_height, text='Voc', border=1, align='C')
        self.pdf.cell(
            w=col_width, h=row_height, text='Amount', border=1,
            new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.pdf.set_font('Courier', '', 16)
        for row in self.vocs:
            self.pdf.cell(
                w=col_width, h=row_height, text=str(row[0]), border=1, align='C'
            )
            self.pdf.cell(
                w=col_width, h=row_height, text=str(row[1]), border=1,
                new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C'
            )

    def ghs_label(self):
        width = 90
        height = 8
        self.pdf.cell(w=0, h=5, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # Health
        self.pdf.set_fill_color(0, 140, 204)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.set_font('Courier', 'B', 20)
        self.pdf.cell(w=width, h=height, text='Health', border=1, align='C',
                      fill=True)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(
            w=40, h=height, text=str(self.health), border=1, align='C',
            new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )
        # Fire
        self.pdf.set_fill_color(230, 13, 46)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.set_font('Courier', 'B', 20)
        self.pdf.cell(w=width, h=height, text='Fire', border=1, align='C',
                      fill=True)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(
            w=40, h=height, text=str(self.flammable), border=1, align='C',
            new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )
        # Reactivity
        self.pdf.set_fill_color(245, 227, 38)
        self.pdf.set_font('Courier', 'B', 20)
        self.pdf.cell(w=width, h=height, text='Reactive', border=1, align='C',
                      fill=True)
        self.pdf.cell(
            w=40, h=height, text=str(self.reactive), border=1, align='C',
            new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )
        # PPE
        self.pdf.set_font('Courier', 'B', 20)
        self.pdf.cell(w=width, h=height, text='PPE', border=1, align='C',)
        self.pdf.cell(
            w=40, h=height, text=str(self.ppe), border=1, align='C',
            new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )
        self.pdf.cell(w=0, h=10, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.pdf.set_font('Courier', 'B', 16)
        self.pdf.cell(
            w=self.pdf.w, h=10,
            text=f'Revision Number {self.revision_version}', align='C')

    def save_report(self):
        file = [('PDF Files','*.pdf')]
        output = filedialog.asksaveasfile(
            filetypes= file,
            defaultextension=file,
            initialfile='base_report',
        )
        self.pdf.output(output.name)
        messagebox.showinfo(
            title='Report Saved',
            message='Base report was successfully saved.'
        )

if __name__ == '__main__':
    db = 'C:\\Users\\msrog\\Documents\\SimpleInks\\src\\cims.db'
    base = 'Mixing Red'
    app = Report(db, base)