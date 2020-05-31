n = input("10진수의 한 지릿수 입력 >> ")
print('두 지릿수 정수에서 최소 한 지릿수가 %s인 정수 찿기: '% n)
print('결과'.center(50, '='))

for i in range(10,100):
    snum = str(i)
    if n in snum:
        print(i, end= ' ')
