from src.decorators import *

@catch_errors
def divide(a, b):
    return a / b

print(divide(10, 2))  # 正常
print(divide(10, 0))  # 会捕获异常并输出 [-] ERRORS => division by zero

safe_exec(lambda: print(10 / 0))

# @catch_errors
# def open2print_file(path):
#     with open(path, 'r', encoding='gbk') as f:
#         lines = f.readlines()
#         for line in lines:
#             print(line.strip())

# open2print_file(r't:\App\movable\NewDesktop\DevLearn\python_basic\11_decorators_try.py')  # 正常
# open2print_file('12313')