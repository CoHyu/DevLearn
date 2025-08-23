import hashlib, sys

class MD5FileChecker:
    def __init__(self, chunkSize: int = 8192):
        self.chunkSize = chunkSize

    def __call__(self, *paths):
        if not paths:
            print("Usage: python xxxx.py <filename> [<filename>......]")
            return
        for path in paths:
            try:
                h = hashlib.md5()
                with open(path, 'rb') as f:
                    for chunk in iter(lambda: f.read(self.chunkSize), b""):
                        h.update(chunk)
            except Exception as e:
                print(f"[-] {path} => {e}")
                continue
            print(f"[+] {path} => {h.hexdigest()}")
