# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"执行时间: {end - start:.4f} 秒")
#         return result
#     return wrapper

# @timer
# def slow_function():
#     for x in range(100):
#         time.sleep(0.1)

# slow_function()



# import sys
# nums_gen = [i for i in range(1_000_000)]
# nums_gen = (i for i in range(1_000_000))
# print(sys.getsizeof(nums_gen))  # bytes





# def read_file(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         for line in f:
#             yield line.strip()

# for line in read_file(".\SycTest.txt"):
#     print(line + '<><><><>')