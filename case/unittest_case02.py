import unittest
class firstcase02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有0case执行之前的前置")
    @classmethod
    def tearDownClass(cls):
        print("所有0case执行之后的后置")
    def setUp(self):
        print("0前置条件")
    def tearDown(self):
        print("0后置条件")
    @unittest.skip("不执行第一条")
    def testfirst001(self):
        print('这是第0一条case')
    def testfirst002(self):
        print("这是第0二条case")
    def testfirst003(self):
        print("这是第03条case")
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(firstcase02('testfirst002'))
    suite.addTest(firstcase02('testfirst001'))
    suite.addTest(firstcase02('testfirst003'))
    unittest.TextTestRunner().run(suite)
    '''
    suite = unittest.TestSuite()
    suite.addTest(firstcase01('testfirst01'))
    unittest.TextTestRunner().run(suite)
    '''

