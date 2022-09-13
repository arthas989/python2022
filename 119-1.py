def new_decorator(original_func):
    def wrap_func():
        print("before original function")
        original_func()  # 包在裡面要執行的
        print("after original function")
    return wrap_func  # decorator的return，不是wrap的return


def func_needs_decorator():
    print("I am a function that needs decorator.")


decorated_function = new_decorator(func_needs_decorator)
decorated_function()
