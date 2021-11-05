print('hello python basic')
print('{:>10}'.format('nice'))  #10자리 확보하고 format 내 문자열 좌측정렬해서 출력해줘
print('{:<10}'.format('nice'))   #10자리 확보하고 format 내 문자열 우측정렬해서 출력해줘 (47행과 비교)
print('{:6.5}'.format('pythonstudy'))  #10글자의 자리를 확보하는 그중 5개만 출력해줘
print('%4d' % (42))    # , 생략 가능