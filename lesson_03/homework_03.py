alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
					   '"That depends a good deal on where you want to get to," said the Cat.\n'
					   '"I don\'t much care where ——" said Alice.\n'
					   '"Then it doesn\'t matter which way you go," said the Cat.\n'
					   '"—— so long as I get somewhere," Alice added as an explanation.\n'
					   '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
qty_apostrophes = 0
for character in alice_in_wonderland:
	if character == "'":
		print(character)
		qty_apostrophes += 1
print(f"Кількість апострофів:", qty_apostrophes)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("task 3")
print(alice_in_wonderland)


# Задачі 04 -10:
# Переведіть задачі з книги "Математика, 5 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в п'ятому класі

# task 04

# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?

black_sea_area = 436402
azov_sea_area = 37800
all_sea_area = black_sea_area + azov_sea_area

print("task 4")
print(f"Загальна площа двох морів складає:", all_sea_area, "км2.")

# task 05

# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.

all_product = 375291
first_and_second_warehouse = 250449
second_and_third_warehouse = 222950
first_warehouse = all_product - second_and_third_warehouse
second_warehouse = first_and_second_warehouse - first_warehouse
third_warehouse = all_product - first_and_second_warehouse

print("task 5")
print(f"На першому складі розміщено:",first_warehouse,"товарів")
print(f"На другому складі розміщено:",second_warehouse,"товарів")
print(f"На третьому складі розміщено:",third_warehouse,"товарів")


# task 06

# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.

payment = 1179
month = 18
cost = payment * month
print("task 6")
print(f"Загальна вартість комп’ютера:", cost, "грн")


# task 07

# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9

print("task 7")
print(f"a) 8019 : 8 =", 8019%8)
print(f"b) 9907 : 9 =", 9907%9)
print(f"c) 2789 : 5 =", 2789%5)
print(f"d) 7248 : 6 =", 7248%6)
print(f"e) 7128 : 5 =", 7128%5)
print(f"f) 19224 : 9 =", 19224%9)


# task 08

# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн

pizza_large_price = 274
pizza_large_qty = 4
pizza_mid_price = 218
pizza_mid_qty = 2
juice_price = 35
juice_qty = 4
pie_price = 350
pie_qty = 1
water_price = 21
water_qty = 3

money = (
	pizza_large_qty * pizza_large_price +
	+ pizza_mid_qty * pizza_mid_price +
	+ juice_qty * juice_price +
	+ pie_qty * pie_price +
	+ water_qty * water_price
)

print("task 8")
print(f"Знадобиться", money, "грн")

# task 09

# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?

photo_qty = 232
photo_in_page = 8
qrty_pages = int(photo_qty / photo_in_page)

print("task 9")
print(f"Ігорю знадобиться", qrty_pages, "сторінок.")


# task 10

# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?

distance = 1600
fuel_per_100km = 9
tank_capacity = 48
fuel_volume_need = distance / 100 * fuel_per_100km
refuels = int(fuel_volume_need // tank_capacity)
remaining_fuel = fuel_volume_need % tank_capacity
if remaining_fuel > 0:
	refuels += 1
print("task 10")
print(f"Для такої подорожі знадобиться:", fuel_volume_need, "літрів")
print(f"Щонайменше потрібно буде заїхати на заправку", refuels, "разів")