import textwrap
from PythonAlloyClient import AlloyServer

class TestJail():
    def check_syntax(self, alloy_code):
        server = AlloyServer()
        server.start()
        success, error = server.check_syntax(alloy_code)
        server.stop()
        return success, error

    def test_correct_syntax(self):
        alloy_code = """sig A {}"""
        success, error = self.check_syntax(alloy_code)

        assert success == True
        for key in error:
            assert error[key] is None
