number_str = input("Введите число: ")

length_1 = len(number_str)
num_list = list(number_str)

count = length_1 // 2


def left(amount, num_lis):
    l_list = []
    while amount > 0:
        l_list += num_lis.pop(0)

        amount -= 1
    return l_list


def right(amount, num_lis):
    r_list = []
    while amount > 0:
        r_list += num_lis.pop(-1)

        amount -= 1
    return r_list


most_left = left(count, num_list)
most_right = right(count, num_list)
sum_l = 0
sum_r = 0

for item in most_left:
    sum_l += int(item)

for item in most_right:
    sum_r += int(item)

if sum_l == sum_r:
    print('Ваше число счастливое =_=')


