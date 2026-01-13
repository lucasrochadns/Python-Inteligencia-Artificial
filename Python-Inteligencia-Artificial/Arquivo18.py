#test lambda exp

listNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x ** 2, listNumber)))

def mult (xy):
    return xy ** 2
print(list(map(mult, listNumber)))

quad = lambda x: x ** 2
print(list(map(quad, listNumber)))