import random as rand

arithmetic_list = ('+','*')
ARITH = {
    '+':lambda a,b: a+b,
    '*':lambda a,b: a*b
}


def makeData():
    f=open('input.txt','w')

    for i in range(1,50000):
        a = rand.randrange(0,100)
        b = rand.randrange(0,100)
        operation = rand.choice(arithmetic_list)
        ans = ARITH[operation](a,b)
        equation = str(a) + operation + str(b) + '=' + str(ans) +'\n'
        f.write(equation)

    f.close()

def main():
    makeData()
    pass

if __name__ == '__main__':
    main()
