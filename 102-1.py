# module的名稱要注意，例如 import 102-2 會有問題
from another_module import *  # 補充 import可用* 但可讀性差先不要
import another_module_2 as a2  # 補充 若要用別名 要在import中用as
'''
from的用法
from module import fun_1,fun_2 
from package import module_1,module_2
'''
from ch7_main_package import some_code as s1, some_other_code as s2
from ch7_main_package.sub_package import small_code

s1.some_func_1()
s1.some_func_2()
s2.some_other_func_1()
s2.some_other_func_2()
small_code.small_func_1()
small_code.small_func_2()

another_func_1()
another_func_2()
a2.test_as_1()
a2.test_as_2()
