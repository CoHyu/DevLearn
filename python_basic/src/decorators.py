# 这一块只是为了对于一个简单函数的测试可以直接调用……
def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[-] ERRORS => {e}")
    return wrapper

def safe_exec(func):
    try:
        return func()
    except Exception as e:
        print(f"[-] ERRORS => {e}")