class A(object):
    def __init__(self):
        self.l1 = []


class B(object):
    a = A()

    def __init__(self):
        self.a.l1.append(1)


if __name__ == '__main__':
    b1 = B()
    b2 = B()
    b3 = B()
    print(b2.a.l1)