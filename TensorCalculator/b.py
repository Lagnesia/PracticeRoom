import a

print('b.py is runnin')


if __name__=='__main__':
    print('b.py 직접 실행')
else:
    print('b.py 가 import 됨')

a.func()