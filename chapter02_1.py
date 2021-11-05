# chapter 02-1
# 파이썬 완전 기초 강의
# print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
print('Python Start!')  # 자주 사용
print("Python Start!") 
print()  # 개행
print()
print("""Python Start!""")
print('''Python Start!''')

# separator 옵션 사용
print('P', 'Y', 'T', 'H','O','N', sep='')  # sep 로 각 문자 분리 
print('010', '7777', '7777', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션 사용 : end 옵션에 들어간 문자로 다음 print문에 이어줄수 있다.
# when to use?: 한 문장을 적절하게 한 print문에다 입력함으로써 한 라인에 출력하길 원할 때
print('Welcome To', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션 사용
import sys      # sys 모듈 사용 시 import 해줘야함

print('Learn Python', file=sys.stdout) # ''의 내용을 file로 지정된 파일에 쓸거다. sys.stdout은 콘솔창을 의미함

print()  

# format 사용(d, s, f)  <암기>
# d : 정수형
# s: 문자열
# f: 실수형

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two')) # format 함수 사용(가독성 제일 좋다) 암묵적으로 첫번째 괄호는 0 두번째 괄호는 1이다
print('{1} {0}'.format('one', 'two')) # format 함수 순서 지정해서 사용 가능. 출력결과 two one

# %s
print('%10s' % ('nice',))   # 10개의 자릿수 확보한 다음 우측정렬하여 문자열 출력 (%10s에서 양수가 오면 우측정렬)
print('{:>10}'.format('nice'))  #10자리 확보하고 format 내 문자열 우측정렬해서 출력해줘

print('%-10s' % ('nice',))      # 10개의 자릿수 확보한 다음 좌측정렬하여 문자열 출력 (%10s에서 음수가 오면 좌측정렬)
                                # 46행과 비교
print('{:10}'.format('nice'))   #10자리 확보하고 format 내 문자열 좌측정렬해서 출력해줘 (47행과 비교)
                                # 좌측정렬이 default

print('{:_<10}'.format('nice'))     #10개의 자릿수 확보한 다음 좌측정렬하여 문자열 출력하는데 
                                    # 문자열이 10개 자릿수 미만이면 _로 채워줘
print('{:^10}'.format('nice'))      #10개의 자릿수 확보한 다음 "중앙"정렬하여 문자열 출력 (^:중앙정렬)

print('%.5s' % ('pythonstudy',))    #. 을 붙임으로써 뒤에 오는 숫자만큼 절삭(슬라이싱)
print('%5s' % ('pythonstudy',))     #. 을 안붙이면 5개의 자릿수를 확보했더라도 모두 출력
print('{:.5}'.format('pythonstudy'))    #format 함수 내의 글자개수만큼 자리를 확보하는데 그중에 5개만 출력 
print('{:10.5}'.format('pythonstudy'))  #10글자의 자리를 확보하는 그중 5개만 출력해줘
print('{:6.5}'.format('pythonstudy'))  #6글자의 자리를 확보하는 그중 5개만 출력해줘 (출력결과= pytho)

# %d
print('%d %d' % (1, 2))     # % 까먹지마!
print('{} {}'.format(1, 2)) 

print('%4d' % (42666666666666)) # 4개의 정수형 공간 확보하지만 확보공간 넘는 경우 해당 정수 안짤리고 출력
print('%4d' % (42,))    # , 생략 가능
print('{:4d}'.format(42))   # format함수에서 정수일 경우에는 서식문자 d를 붙여줘야함. (cf) 문자열은 안붙여줘도 됨 )

# %f
print('%f' % (3.141592653589793,))
print('%1.8f' % (3.141592653589793,))   # 정수부분은 한자리만 나오고 소수부분은 소수점이하 8번째자리까지 나와라(9번째 자리에서 반올림)
print('{:f}'.format(3.141592653589793))

print('%06.2f' % (3.141592653589793,))  # 총 자릿수:6, 소수점 이하 2번째 자리까지, 나머지 정수부(공백)는 0으로 채워
print('{:06.2f}'.format(3.141592653589793))








