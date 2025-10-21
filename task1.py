#Сума двох чисел: Написати програму, яка зчитує два цілих числа та виводить їх суму.

# n1 = int(input("Enter number1: "))
# n2 = int(input("Enter number2: "))
# print(n1 + n2)

#Гіпотенуза: За двома катетами прямокутного трикутника знайти довжину його гіпотенузи.

# cathetus1 = int(input("Enter the length of cathetus1: "))
# cathetus2 = int(input("Enter the length of cathetus2: "))
# sum = cathetus1 ** 2 + cathetus2 ** 2
# print("Lenght of the hypoteenuse: ", str(sum ** 0.55))

##Двічі: Написати програму, яка зчитує ціле число та виводить його двічі.

# n3 = (int(input("Enter number: ")))
# print((str(n3) + " ") * 2)

#Привіт, <ім'я>: Написати програму, яка запитує ім'я користувача і виводить привітання.

# name1 = input("Enter yor Name: ")
# print("Hallo, " + str(name1))

#Прощавай, <ім'я>: Написати програму, яка запитує ім'я користувача і виводить прощання.

# name2 = input("Enter yor Name: ")
# print("Goodbye, " + str(name2))

#Вік через рік: Напишіть програму, яка запитує ім'я користувача та його вік. Потім виведіть повідомлення, яке повідомляє, скільки йому буде років через рік.

# name3 = input("Enter yor Name: ")
# age = int(input("Enter yor age: "))
# print(name3, ", ","in a year your age ", str(age + 1))

#Площа прямокутника: Напишіть програму, яка запитує довжину та ширину прямокутника, а потім обчислює та виводить його площу.

# lehgth = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area = lehgth * width
# print("Area of a rectangle: ", str(area))

#Конвертер валют: Запропонуйте користувачеві ввести суму в одній валюті (наприклад, доларах), а потім виведіть цю суму в іншій валюті (наприклад, євро), використовуючи заздалегідь визначений коефіцієнт обміну.

# usd = (int(input("Enter amount in usd: ")))
# k = 0.85
# eur = usd * k
# print("Amount in usd ", str(eur))

#Вартість покупки: Запитайте користувача назву товару, його ціну та кількість. Обчисліть загальну вартість покупки та виведіть її на екран.

product = input("Enter the product name: ")
price = float(input("Enter the price: "))
quantity = float(input("Enter the quantity: "))
shopping = price * quantity
print("Total purchase price")

#Температура: Напишіть програму, яка перетворює температуру з градусів Цельсія на Фаренгейт. Запитайте користувача температуру в градусах Цельсія.

#Ви придбали товар на певну суму s. Скільки купюр різного номіналу треба віддати продавцю, якщо починати платити з найбільших? У вас є 1, 2, 5, 10, 100, 500 гриве#нь.