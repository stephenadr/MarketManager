import unittest
from api.login import LoginAPI

class TestMyClass(unittest.TestCase):
    def test_method(self):
        obj = LoginAPI()
        result = obj.get_verify_code()
        print(result)
        assert result.status_code == 200


if __name__ == '__main__':
    unittest.main()
