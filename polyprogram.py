def inputPoly():
    p=[]
    while True:
        a= int(input('지수 : '))
        b= int(input('계수 : '))
        c=[a,b]

        if a < 0:
            break


        for i in range(len(p)):
            if p[i][0] == a:
                print('같은 지수 값을 가지는 원소가 있습니다.')
                break

            if i == len(p)-1:
                p.append(c)

        if len(p) == 0:
            p.append(c)

    p.sort()
    p.reverse()

    return p
    




def printPoly(p):
   
    s=''
    for i in range(len(p)):
        for j in range(1, -1 , -1):
            
            if j % 2  == 0:
                if p[i][j] == 1:
                    s+= 'x'
                    continue
                elif p[i][j] == 0:
                    s+= ''
                    continue
                else:
                    s+= 'x^'

            s+= str(p[i][j])
                    
        if i != len(p)-1:
            s+= ' + '
        
    print(s)
   
    return s


    
def evalPoly(p,x):
    
    k=len(p)
    s= [0] *k

    for i in range(k):
        s[i] = pow(x,p[i][0]) *p[i][1]

    res = sum(s)

    return res



def addPoly(a,b):

    if len(a) < len(b):
        a,b = b,a

    i=0
    while i < len(b):
        j=i
        
        while j < len(a):
            
            if a[j][0] == b[i][0]:
                a[j][1] += b[i][1]
                break

            elif a[j][0] < b[i][0]:
                a.insert(j, b[i])
                break
            
            else:
                j+=1

        i+=1

    return a



def multiplyPoly(a,b):

    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            s= [a[i][0] +b[j][0] , a[i][1]*b[j][1]]
            c.append(s)

    c.sort()
    c.reverse()
    
    i=0
    while i < len(c)-1:
        if c[i][0] == c[i+1][0]:
            
            c[i][1]+=c[i+1][1]
            c.remove(c[i+1])
            i-=1
            
        i+=1
        

    return c



m = 1
P = []

while m != 9:
    print('1. 다항식 입력')
    print('2. 다항식 출력')
    print('3. 다항식 계산')
    print('4. 다항식 덧셈')
    print('5. 다항식 곱셈')
    
    m = int(input('메뉴 선택 (종료시는 9) : '))

    
    if m == 1:
        print('다항식 입력 선택\n')
        P = inputPoly()
        print()
        
    elif m == 2:
        print('다항식 출력 선택\n')
        printPoly(P)
        print()
        
    elif m == 3:
        print('다항식 계산 선택\n')
        printPoly(P)
        X = int(input('X = '))
        result = evalPoly(P, X)
        print('계산 결과 : ', result)
        print()
        
    elif m == 4:
        print('다항식 덧셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        printPoly(A)
        printPoly(B)
        C = addPoly(A, B)
        printPoly(C)
        print()
        
    elif m == 5:
        print('다항식 곱셈 선택\n')
        A = inputPoly()
        B = inputPoly()
        printPoly(A)
        printPoly(B)
        C = multiplyPoly(A, B)
        printPoly(C)
        print()
        
    else:
        if m != 9:
            print('메뉴 선택 오류\n')

            
