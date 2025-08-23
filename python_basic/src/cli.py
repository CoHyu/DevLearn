import argparse
from md5File_sum import MD5FileChecker
from Passwd_checker import Passwd_checker_1
from PDsecret import StrongPasswdSpawn

def main():
    parser = argparse.ArgumentParser(
        prog="z", 
        description="" \
        "Zekk Personel Toolset, just for convenience."
        )
    subparsers = parser.add_subparsers(dest="command")

    md5_parser = subparsers.add_parser("md5", help="计算文件MD5")
    md5_parser.add_argument("files", nargs="+", help="要计算MD5的文件")

    passwd_parser = subparsers.add_parser("passwd", help="检查密码强度")
    passwd_parser.add_argument("password", help="要检查的密码")

    secret = subparsers.add_parser("secret", help="生成强密码")
    secret.add_argument("passwdLength", nargs='?', default=12, type=int, help="密码长度 (默认12位)")

    args = parser.parse_args()

    if args.command == "md5":
        MD5FileChecker()(*args.files)
    elif args.command == "passwd":
        pc = Passwd_checker_1(args.password)
        for k, v in pc.report().items():
            print(f"{k}: {v}")
    elif args.command == "secret":
        generator = StrongPasswdSpawn()
        generator.generate_password(args.passwdLength)
    else:
        parser.print_help()