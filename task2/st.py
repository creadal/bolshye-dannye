from factor import factorize

count = 0
with open('C:\\Users\\user\\Desktop\\bolshye dannye\\task2\\numbers.txt', 'r') as file:
    number = file.readline()
    while number != '':
        count += len(factorize(int(number)))
        number = file.readline()

print(count)