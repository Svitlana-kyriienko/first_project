#Домашнє завдання:

#Задача 1. Середнє трьох чисел
#Користувач вводить три числа. Обчисли середнє арифметичне.

n4 = int(input("Enter number1: "))
n5 = int(input("Enter number2: "))
n6 = int(input("Enter number3: "))
print ((n4 + n5 + n6) / 3)

#Задача 2. Остача від ділення
#Користувач вводить два числа. Знайди остачу від ділення першого на друге.

n4 = int(input("Enter number1: "))
n5 = int(input("Enter number2: "))
n8 = int(input("Enter number2: "))
print(n7 % n8)


#Задача 3. Подвоєне число
#Користувач вводить число. Виведи подвоєне значення цього числа.

n9 = float(input("Enter number: "))
print (n9 * 2)

#Задача 4. Конвертація хвилин у секунди
#Користувач вводить кількість хвилин. Обчисли, скільки це буде секунд.

minutes = int(input("Enter minutes: "))
print("It's in sekonds ", minutes * 60)

#Задача 5. Кількість яблук на кожного
#Є n яблук і k учнів. Скільки яблук отримає кожен учень, якщо ділити порівну, і скільки залишиться?

n = int(input("Enter the number of apples: "))
k = int(input("Enter the number of students: "))
print("Every studet will receive apples ", n // k)
print("The rest of the apples ", n % k)

#Задача 6. Остання цифра числа
#Користувач вводить число. Виведи його останню цифру.

n10 = int(input("Enter number: "))
print(n10 % 10)

#Задача 7*. Обмін змінних
#Користувач вводить два числа. Після цього потрібно “поміняти” їх місцями і вивести результат.

n11 = int(input("Enter number1: "))
n12 = int(input("Enter number2: "))
n11, n12 = n12, n11
print(n11, n12)