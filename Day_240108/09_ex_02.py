'''
지역변수 & 전역변수
'''
def foo():
    print(x) #전역변수 x

#전역변수 ----------------------------
x=10

# 함수 호출--------------------------
foo()
print(x) #지역변수 x 접근 불가능.
