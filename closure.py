#CLOSURE
def multi(n:int):
    def inner():
        return [i * n for i in range(1,11)]
    return inner

table_5 = multi(5)
table_4 = multi(4)

print(table_4())
