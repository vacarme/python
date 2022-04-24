class UppercaseException(Exception):
    pass


def access(index:int):
    short = [1,2,3]
    try:
        index = int(index)
        return short[index]
    except IndexError:
        print('please use a good index')
    except ValueError as verr:
        print('use an int', verr)
    print('ca continue dans la fonction')

print(access(2))
print(access(3))
#print(access('alex'))
print('ca continue dans le main')

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError('divisor cannot be 0')
    return a/b

grades = []

print('Welcome')
try:
    average = divide(sum(grades),len(grades))

except ZeroDivisionError as e:
    print(e)
    print('no grade in the list')
else:
    print(f'the average is {average}')
finally:
    print('thank you')
#je pense qu'il faut faire raise l'erreur a la fonction qui a la logique et traiter la catch dans le bout de code qui l'utilise.
