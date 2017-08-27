class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"
 
class A(Base):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()
        print "leave A"
 
class B(Base):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"
 
class C(A, B):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"

if __name__ == '__main__':
    #注意self一直指代的是实例本身，这样的话结合mro的意思，就能理解为什么输出是这样了
    c=C()
    mro_list=c.__class__.mro()
    print(mro_list[mro_list.index(C) + 1])
