from gui import login
from functions import login_commands as lc

class App:
    def __init__(self):
        self.login_gui = login.Login()
        self.login_gui.create_widgets()

if __name__ == '__main__':
    app = App()