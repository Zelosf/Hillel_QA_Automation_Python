import unittest
from homeworks import all_sum_numbers, sum_of_two_numbers, average_list, longest_word_in_list


class TestAllSumNumbers(unittest.TestCase):
	def setUp(self):
		self.correct_value = "1,2,3,4"
		self.correct_value_with_minus = "55,42,-3,4"
		self.incorrect_value = "qwerty1,2,3"

	def test_all_sum_numbers_valid_result(self):
		result_1 = all_sum_numbers(self.correct_value)
		result_2 = all_sum_numbers(self.correct_value_with_minus)

		self.assertEqual(result_1, 10, msg='Результат повинен бути рівним 10!')
		self.assertEqual(result_2, 98, msg='Результат повинен бути рівним 98!')

	def test_all_sum_numbers_negative_result(self):
		result = all_sum_numbers(self.incorrect_value)

		self.assertEqual(result, "Не можу це зробити", msg='Повідомлення про неможливість підрахувати')

	def test_all_sum_numbers_type_result(self):
		result = all_sum_numbers(self.correct_value)

		self.assertIsInstance(result, int, msg='Результат повинен бути числом!')


class TestSumOfTwoNumbers(unittest.TestCase):
	def setUp(self):
		self.value_a = 65
		self.value_b = 77
		self.value_c = -144
		self.value_d = 'a'

	def test_sum_of_two_numbers_valid_result(self):
		result_1 = sum_of_two_numbers(self.value_a, self.value_b)
		result_2 = sum_of_two_numbers(self.value_a, self.value_c)

		self.assertEqual(result_1, 142, msg='Результат повинен бути рівним 142!')
		self.assertEqual(result_2, -79, msg='Результат повинен бути рівним -79!')

	def test_sum_of_two_numbers_invalid_result(self):
		with self.assertRaises(TypeError):
			sum_of_two_numbers(self.value_a, self.value_d)


class TestAverageList(unittest.TestCase):
	def setUp(self):
		self.valid_result = [1, 2, 4, 6, 8, 11]
		self.not_valid_result = [1, 2, 's4', 6, '18', 11]

	def test_average_list_valid_result(self):
		result = average_list(self.valid_result)

		self.assertEqual(result, 5.333, msg='Результат повинен бути рівним 5.333!')

	def test_average_list_invalid_result(self):
		with self.assertRaises(TypeError):
			average_list(self.not_valid_result)


class TestLongestWordInList(unittest.TestCase):
	def setUp(self):
		self.valid_result = ['love', 'time', 'work', 'know', 'tree', 'blue', 'play', 'hope', 'happy', 'great']
		self.empty_result = []
		self.numeric_result = [1, 2, 4, 6, 8, 11]

	def test_longest_word_in_list_valid_result(self):
		result = longest_word_in_list(self.valid_result)

		self.assertEqual(result, 'happy', msg='Результат повинен бути Рівним "happy"!')

	def test_longest_word_in_list_empty_result(self):
		result = longest_word_in_list(self.empty_result)

		self.assertEqual(result, '', msg='Результат повинен бути Пустим!')

	def test_longest_word_in_list_type_result(self):
		result = longest_word_in_list(self.valid_result)

		self.assertIsInstance(result, str, msg='Результат повинен бути str!')

	def test_longest_word_in_list_numeric_result(self):
		with self.assertRaises(TypeError):
			longest_word_in_list(self.numeric_result)

