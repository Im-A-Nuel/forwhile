def cek_prima(n):
    pembagi=0
    for i in range(1,n+1):
        if n%i==0 :
            pembagi=pembagi+1
    if pembagi ==2:
        return True
    else :
        return False

print('program pengecek bilangan prima')
n=int(input('Masukan bilangan : '))
hasil=cek_prima(n)#TRUE/FALSE
if hasil==True:
    print(f'{n} adalah bilangan prima')
else :
    print(f'{n} bukan bilangan prima')
