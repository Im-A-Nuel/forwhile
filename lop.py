def pentagon(n):
    for i in range(1, n+1):
        bilangan=int(i*(3*i-1)/2)
        print(bilangan, end='\t')



print('Deret n bilangan pentagon')
n=int(input('Masukan n : '))
pentagon(n)
