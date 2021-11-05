# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))  # n의 자료형을 보여줌

# 동시 선언
x = y = z = 700
print(x, y, z)

#선언
var = 75

# 출력
print(var)
print(type(var))

# 재 선언
# C언어와 다르게 자료형 지정 안해줘도됨
# 주의: 똑같은 값이 선언되지 않도록 코딩하면서 잘 keep up해야함
var = "Change Value"    #''으로 선언해줘도 됨

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태 (기억 要)
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔에 출력

# 예1)
print(300)
print(int(300))

# 예2)
n=777

# n은 int형의 오브젝트이다
print(n, type(n))
print()

m = n
#m-> 777 <- n

print(m, n) # , 뒤에는 한 칸 띄워주는 것이 좋음 (권장사항)
print(type(m), type(n))
print()

m = 400

print(m, n) # , 뒤에는 한 칸 띄워주는 것이 좋음 (권장사항)
print(type(m), type(n))
print()

# *****id(identity)확인 : 객체의 고유값 확인****

# m, n 객체의 고유값은 서로 같다
# 파이썬은 똑같은 값을 복사해서 쓰는 것은 비효율적이라 판단해서
# m, n 은 똑같은 하나의 인스턴스로 본다
# -> 최적화 문제(빠른 프로그램의 실행을 위해)
# 같은 object 참조

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# m, n 객체의 고유값은 서로 다르다
m=800
n=655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()



# 다양한 변수 선언
# Camel Case :  numberOfCollegeGraduates  -> Method 선언 방법; 첫글자는 소문자 
# Pascal Case :  NumberOfCollegeGraduates  -> Class 선언 방법; 첫글자부터 대문자
# Snake Case :  number_of_college_graduates  -> 파이썬에서 변수 선언 방법 ; 모든 단어 소문자 및 _으로 연결
 
# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""