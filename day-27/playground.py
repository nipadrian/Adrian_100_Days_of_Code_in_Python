def add(*args):
    sum=0
    for n in args:
        sum += n
    print(sum)

add(1,3,5,6,2,20,50)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=5)

