from tests import vocs_test

class Test:
    def __init__(self):
        self.vocs = vocs_test.VocTests()
    
    def test_vocs(self):
        self.vocs.check_connection()
        print()
        self.vocs.check_disconnect()
        print()
        self.vocs.check_count()
        print()
        self.vocs.check_fetch()
        print()
        self.vocs.check_users()
        print()
        self.vocs.check_edit()
        print()
        self.vocs.check_add()
        print()
        self.vocs.check_delete()


if __name__ == '__main__':
    test = Test()
    test.test_vocs()