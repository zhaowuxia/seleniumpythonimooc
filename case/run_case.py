import unittest
import os
class runcase(unittest.TestCase):
    def test_case01(self):
        case_path=os.path.join(os.getcwd())
        suite=unittest.defaultTestLoader.discover(case_path,'unittest_*.py')#有三个参数，路径，匹配规则，3可不填
        unittest.TextTestRunner().run(suite)
if __name__ == '__main__':
    unittest.main()