'''
데이터를 메모리에 저장하는 방법
=> 파이썬 문법 : 변수명 = 저장할 데이터
+변수 : 영어, 숫자, _로 구성 가능.(숫자로 시작X)
파이썬의 변수는 힙영역에 저장된 데이터 주소를 저장하는 변수.
=> 참조 변수(reference variable)
'''
#나이를 메모리에 저장
# => 나이 : 정수 int => 힙 영역에 저장.
# => 변수 age
age = 17 # '데이터'로 변수를 지정하면 데이터로 인식해서 오류 발생.

#이름을 메모리에 저장
# => 이름 : 문자 ==> 힙 영역에 저장.
# = > 변수 name
name = "Peter Parker"
my_name = "홍길동"
name_99 = "Tony Stark"

# 메모리에 저장은 됨. => 저장된 데이터 위치를 알 수 없음. => 다시 사용불가.
2024
"Good Luck"

year = 2024 # 2024 데이터가 저장된 주소를 year이름이 붙은 메모리 저장.
"Good Luck" #

#데이터의 주소를 확인하는 내장함수 = id( 실제 데이터 / 변수명)
print(id(2024))
print(id(year))
year = 2023
print(id(year))
year= '2023'
print(id(year))

#__________
#변수가 저장하고 있는 데이터의 종류, 즉, 데이터의 타입 => type(데이터, 변수명)'
#____________________________________________________________________

print(type(2024))
print(type(4.0))
print(type("4.0:"))
