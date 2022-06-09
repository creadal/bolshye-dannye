from factor import factorize

count = 0
with open('task2\\numbers.txt', 'r') as file:
    number = file.readline()
    while number != '':
        count += len(factorize(int(number)))
        print(len(factorize(int(number))))
        number = file.readline()

print(count)