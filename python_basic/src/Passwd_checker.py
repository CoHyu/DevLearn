class Passwd_checker_1:
    def __init__(self, passwd):
        self.passwd = passwd
        self.secure_lv = 0

    def CheckLength(self):
        if len(self.passwd) > 8:
            self.secure_lv += len(self.passwd) - 8

    def CheckMix(self):
        self.Nnums = 0
        self.Anums = 0
        self.Snums = 0
        self.Cnums = 0
        for i in self.passwd:
            if i.isupper or i.islower:
                self.Cnums += 1
            if i.isdigit:
                self.Nnums += 1
            if i.isalpha:
                self.Anums += 1
            if i in "!@#$%^&*()_+-=[]{}|;:,.<>?/":
                self.Snums += 1
        self.secure_lv += (self.Nnums > 0) // 2 + (self.Anums > 0) // 2 + (self.Snums > 0) // 2 + (self.Cnums > 0) // 2

    def report(self):
        self.secure_lv = 0
        self.CheckLength()
        self.CheckMix()
        report = {
            "你的密码": self.passwd,
            "安全总评级": self.secure_lv,
            "安全强度": "弱" if self.secure_lv < 5 else "中" if self.secure_lv < 8 else "强"
        }
        return report