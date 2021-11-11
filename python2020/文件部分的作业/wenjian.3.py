# wenjian.3
# coding=utf-8

sum = 0
with open("data_in.txt", 'r') as data_in:
    while True:
        number = data_in.readline()
        if number:
            sum += eval(number)
        else:
            break
        with open("data_out.txt", 'w') as data_out:
            data_out.write(str(sum))
