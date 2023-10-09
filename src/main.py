from gui import login


class App:
    def __init__(self):
        database = 'cims.db'
        self.login_gui = login.Login(database)
        self.login_gui.create_widgets()


if __name__ == "__main__":
    app = App()
