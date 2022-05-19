
# for i in range(101):
#     glock1 = False
#     clock1 = False
#     glock = i % 3
#     clock = i % 5
#     if glock == 0:
#         print("Fizz")
#         glock1 = True
#     elif i % 5 == 0:
#         print("Buzz")
#         clock1 = True
#     elif glock1 and clock1 == True:
#         print("Fizzbuzz")
#     else:
#         print(i)


# def arrayShifter():
#     array = [1,2,3,4,5,6,7,8,9,0]

#     number = int(input("Move array: "))

#     length = int(len(array))
#     for i in range(length - 1):
#         if i + number > length - 1:
#             array[i] = array[i + number - 10]
#         else:
#             array[i] = array[i + number - 1]

#     print(array)

# arrayShifter()

import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


def main(numero):
    

    franz = ((numero // 10)) + (numero % 10)
    if franz > 9:
        main(franz)
    else:
        print(franz)


numero = int(input("Number:"))
main(numero)
