# 117-3_unittest.py
import unittest
import calculator


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)
        print("Running setUp")

    def tearDown(self):
        self.args = None
        print("Running tearDown")

    def test_plus(self):
        expected = 5
        result = calculator.plus(*self.args)
        self.assertEqual(expected, result)
        print("Running test_plus")

    def test_minus(self):
        expected = 1
        result = calculator.minus(*self.args)
        self.assertEqual(expected, result)
        print("Running test_minus")


# 一、組合成suite測試
suite = unittest.TestSuite()
suite.addTest(CalculatorTestCase("test_plus"))
suite.addTest(CalculatorTestCase("test_minus"))

# 二、使用list定義要測試的項目
# tests = ['test_plus', 'test_minus']
# suite = unittest.TestSuite(map(CalculatorTestCase, tests))

# 三、載入某個 TestCase 子類別中所有 test_xxx 方法
# loader = unittest.TestLoader()
# suite = loader.loadTestsFromTestCase(CalculatorTestCase)


# TextTestRunner 使用測試執行器
# if __name__ == "__main__":
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)

# 透過main執行
if __name__ == "__main__":
    # unittest.main(verbosity=2)
    unittest.main()
