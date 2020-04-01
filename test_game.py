import unittest
from character import Character



class TestCharacter(unittest.TestCase):

	def test_is_alive(self):

		char1 = Character(0, 100)
		char2 = Character(50, 50)
		char3 = Character(33.33, 50)

		result = char1.is_alive()
		result2 = char2.is_alive()
		result3 = char3.is_alive()


		self.assertEqual(result, False)
		self.assertEqual(result2, True)
		self.assertEqual(result3, True)


	def test_is_alive_with_negative_healt(self):

		char = Character(-10, 50)
		exc = None

		try:
			char.is_alive()
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Incorrect health.')


	def test_take_damage_when_damage_points_are_more_than_health(self):

		char = Character(30, 50)
		damage_points = 40

		char.take_damage(damage_points)
		result = char.get_health()

		self.assertEqual(result, 0)


	def test_take_damage_when_damage_points_are_less_than_health(self):

		char = Character(50, 50)
		damage_points = 20

		char.take_damage(damage_points)
		result = char.get_health()

		self.assertEqual(result, 30)


	def test_take_damage_when_damage_points_are_equal_to_health(self):

		char = Character(50, 50)
		damage_points = 50

		char.take_damage(damage_points)
		result = char.get_health()

		self.assertEqual(result, 0)


	def test_take_damage_when_damage_points_are_float(self):

		char = Character(50, 50)
		damage_points = 44.44

		char.take_damage(damage_points)
		result = char.get_health()

		self.assertEqual(result, (50-44.44))


	def test_take_healing_when_is_dead(self):

		char = Character(0, 50)

		result = char.take_healing(10)

		self.assertEqual(result, False)


	def test_take_healing_when_healing_points_plus_health_are_more_than_max_health(self):

		char = Character(100, 50)
		char.take_damage(50)

		result_bool = char.take_healing(60)
		result_health = char.get_health()

		self.assertEqual(result_bool, True)
		self.assertEqual(result_health, 100)


	def test_take_healing_when_healing_points_plus_health_are_less_than_max_health(self):

		char = Character(50, 50)
		char.take_damage(20)

		result_bool = char.take_healing(10)
		result_health = char.get_health()

		self.assertEqual(result_bool, True)
		self.assertEqual(result_health, 40)













if __name__ == '__main__':
	unittest.main()