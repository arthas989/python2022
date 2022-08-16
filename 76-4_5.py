# 76-4
# 正三角型
# 輸入數字代表層數，要產出 1,3,5,7,9……的*三角型


def pyramid(num):
    #stars_list = []
    stars_num = 0
    for i in range(1, num+1, 1):
        stars_num = 2*i-1  # 第i層的*有幾個
        space = 2*num-1 - stars_num  # 第i層的空白有幾個
        space /= 2  # 分左右空白填滿
        # print(stars_num)
        # print(space)
        # 中間*，左右兩邊塞空白
        print(int(space)*" "+stars_num*"*"+int(space)*" ")
        # stars_list.append(stars_num)
    # return stars_list


print("------------- 76-4 -------------")
pyramid(1)
print("------------- 76-4 -------------")
pyramid(2)
print("------------- 76-4 -------------")
pyramid(4)


# 76-5
# 倒三角型
def inversePyramid(num):
    stars_num = 0
    for i in range(num, 0, -1):
        stars_num = 2*i-1  # 第i層的*有幾個
        space = 2*num-1 - stars_num  # 第i層的空白有幾個
        space /= 2  # 分左右空白填滿
        # 中間*，左右兩邊塞空白
        print(int(space)*" "+stars_num*"*"+int(space)*" ")


print("------------- 76-5 -------------")
inversePyramid(4)
