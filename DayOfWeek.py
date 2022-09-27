# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Enter your number from 1 to 7: '))
if day < 6 and day > 0:
    print('It is working day')
elif day > 5 and day < 8:
    print('In is a day off')
else:
    print('Read the condition carefully')