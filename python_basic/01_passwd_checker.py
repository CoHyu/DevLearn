from src.Passwd_checker import Passwd_checker_1

if __name__ == "__main__":
    passwd = input("Type in your PASSWD:")
    PC = Passwd_checker_1(passwd)
    for k, v in PC.report().items():
        print(f"{k}: {v}")
