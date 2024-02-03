#다양한 함수의 형태 - (3) return 키워드
#-> 함수 호출한 곳으로 돌아가게 하는 기능.
#-> 결과값이 함께 있다면 결과값을 가지고 돌아감.

# < 함수 생성 문법 >
# def 함수 이름(매개변수 1, 매개변수 2,.., 매개변수 n) : # : 필요
#     조건 코드와 return 값
#     실행코드
#     실행코드
#     return 결과값
#----------------------------------------------------------------
# 함수 기능 : 팩토리얼 계산 후 계산 결과를 반환해 주는 기능.
#           팩토리얼이란? 3! = 3 * 2 * 1

def factorial(x) :
    if not x :
        return 1 # 즉시 함수 종료 후 호출한 곳을 반환. / return 값이 없으면 None //
    ret = 1
    if x :
        for n in range(x, 0, -1) :
            ret *= n
    return ret

print(f'0! = {factorial(0)}')
print(f'3! = {factorial(3)}')