adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""


adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f"Текст '"'Adwentures of Tom Sawer'"' без помилки:", adwentures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"Текст '"'Adwentures of Tom Sawer'"' без '"'....'"' :", adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f"Текст '"'Adwentures of Tom Sawer'"' з одним пробілом:", adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

h_qty = 0
for char in adwentures_of_tom_sawer:
	if char == 'h':
		h_qty += 1
print(f"Кількість літер '"'h'"':" , h_qty)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

words = adwentures_of_tom_sawer.split()
upper_qty = 0
for word in words:
	if word[0].isupper():
		upper_qty += 1

print(f"Кількість слів які починаються з великої літери:", upper_qty)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

index_tom = adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom")+1)
print(f"Позиція другого слова '"'Tom'"':", index_tom)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print(f"Окремі речення:", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print(f"Четверте речення:",adwentures_of_tom_sawer_sentences[3])
lower_4_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Четверте речення в нижньому регистрі:",lower_4_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

start_sentence = 0
for sentence in adwentures_of_tom_sawer_sentences:
	if sentence.startswith("By the time"):
		start_sentence += 1

if start_sentence != 0:
	print("Є речення яке починається з '"'By the time'"'")
else:
	print("Речення яке починається з '"'By the time'"' відсутнє")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

word_qty = len(adwentures_of_tom_sawer_sentences[-1].split())
print(f"Кількість слів в останньому реченні:",word_qty)