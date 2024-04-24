def my_function(*args, **kwargs):
    # 处理位置参数 args
    for arg in args:
        print(arg)
    # 处理关键字参数 kwargs
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# 调用函数并传递关键字参数
my_function(1,2,3,name="John", age=30, city="New York")
# 1, 2, 3 按顺序传递，没有使用 key=value 形式，因此被识别为位置参数，并收集到 args 元组中。
# name="John", age=30, city="New York" 使用了 key=value 形式，因此被识别为关键字参数，并收集到 kwargs 字典中。