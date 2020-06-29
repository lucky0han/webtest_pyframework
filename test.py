import random
import re

import chardet


class A(object):
    def __init__(self):
        self.i = 2


def check(s) -> bool:
    s = s.lower()
    s = re.findall(r"[0-9]|[a-z]|[A-Z]", s)
    num = len(s)
    half_num = int(num / 2)

    for i in range(half_num):
        if s[i] == s[num - i - 1]:
            continue
        else:
            return False
    return True



if __name__ == '__main__':

    i = [0] * 10
    print(i)
