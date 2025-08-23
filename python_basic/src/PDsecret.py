import secrets
import string

class StrongPasswdSpawn:
    """强密码生成器类"""
    
    def __init__(self):
        # 字符集：大小写 + 数字 + 常见符号
        self.UPPER = string.ascii_uppercase  # ABC…Z
        self.LOWER = string.ascii_lowercase  # abc…z
        self.DIGITS = string.digits  # 0123456789
        # self.SYMBOLS = r"""!#$%&()*+,-./:;<=>?@[\]^_{|}~"""  # 32 个安全符号
        self.SYMBOLS = r"""(.@$!%*#_~?&^)"""  # 简化版安全符号
        self.CHARSET = self.UPPER + self.LOWER + self.DIGITS + self.SYMBOLS
    
    def generate_password(self, length: int = 12) -> str:
        """
        生成一个随机密码（默认 12 位，上限 12 位）
        length 取值范围：4 ~ 12
        """
        try:
            if not (4 <= length <= 12):
                raise ValueError("length 必须在 4~12 之间")

            # 确保满足"4 类字符至少各出现 1 次"
            password = [
                secrets.choice(self.UPPER),
                secrets.choice(self.LOWER),
                secrets.choice(self.DIGITS),
                secrets.choice(self.SYMBOLS),
            ]
            # 剩余位数随机补齐
            remaining = length - 4
            password += [secrets.choice(self.CHARSET) for _ in range(remaining)]

            # 打乱顺序，防止前 4 位固定模式
            secrets.SystemRandom().shuffle(password)
        
            print(f"[+] YourPASSWORD: " + ''.join(password))
        except Exception as e:
            print(f"[-] {e}")