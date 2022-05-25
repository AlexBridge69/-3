# Подсчитать сумму цифр в вещественном числе.
number = str(input('Задайте первую строку: '))
count_of_symbols = abs(number.find('.') - len(number)) - 1
number = float(number)
number *= 10**count_of_symbols
sum = 0

while number != 0:
    sum += number % 10
    number //= 10
print(int(sum))
