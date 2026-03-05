def add_nums(*args):
    args = list(args)
    print(args, type(args))
    sum = 0
    for i in args:
        sum += i
    print(f'Addition : {sum}')

add_nums()