def divide(first, second):
    if second != 0:
        a = first / second
        return a
    else:
        return ("Ошибка")

def main():
    op_ = divide(8, 4)
    op_1 = divide(4, 0)
    op_2 = divide(5, 0)
    print(op_)
    print(op_1)
    print(op_2)

if __name__ == "__main__": #не совсем понял этот момент
    main()
