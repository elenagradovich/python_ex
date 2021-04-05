import numpy

def generatorLeibniz():
    denominator = 1 #знаменатель
    num = 1.00
    sum = 0
    mark = 1

    while round(sum, 2) != round(numpy.pi / 4, 2):
        if denominator != 0:
            num = round(mark / denominator, 4)
        sum += num
        denominator += 2
        mark *= -1
        # print('sum:', round(sum, 2))
        yield num

for item in generatorLeibniz():
    print(item)
