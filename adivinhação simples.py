n=0
while n > 9:
    n=[0,1,2,3,4,5,6,7,8,9]
escolha=int(input('um número; '))
if escolha==n:
    print('acertou!')
elif escolha!=n:
    print('tente novamente')
print(n)