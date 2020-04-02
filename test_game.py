import unittest
from character import Character
from enemy import Enemy
from weaponAndSpell import (Weapon, Spell)
from Hero import Hero

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
		

	def test_can_cast(self):

		char = Character(50, 50)
		mana_cost_1 = 60
		mana_cost_2 = 40
		mana_cost_3 = 50

		result1 = char.can_cast(mana_cost_1)
		result2 = char.can_cast(mana_cost_2)
		result3 = char.can_cast(mana_cost_3)

		self.assertEqual(result1, False)
		self.assertEqual(result2, True)
		self.assertEqual(result3, True)
		
		
	def test_attack_with_weapon(self):

		char = Character(50, 50)
		weapon = Weapon('wep', 20)

		char.equip(weapon)
		result = char.attack(by='weapon')

		self.assertEqual(result, 20)


	def test_attack_with_spell(self):

		char = Character(20, 30)
		spell = Spell('spell', 40, 10, 2)

		char.learn(spell)
		result = char.attack(by='spell')

		self.assertEqual(result, 40)


	def test_attack_with_no_weapon_or_spell(self):

		char = Character(80, 100)

		result1 = char.attack(by='weapon')
		result2 = char.attack(by='spell')

		self.assertEqual(result1, 0)
		self.assertEqual(result2, 0)



class TestEnemy(unittest.TestCase):

	def test_attack_by_its_own_damage(self):

		enemy = Enemy(50, 60, 20)

		result = enemy.attack()

		self.assertEqual(result, 20)


	def test_attack_by_weapon_or_spell(self):

		enemy = Enemy(50, 50, 50)
		weapon = Weapon('wep', 5)

		enemy.equip(weapon)
		result = enemy.attack(by='weapon')

		self.assertEqual(result, 5)

class TestHero(unittest.TestCase):

	def test_known_as(self):
		h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
		expected = 'Bron the Dragonslayer'
		returned = h.known_as()

		self.assertEqual(returned, expected)

	def test_take_mana_but_not_reach_start_value(self):
		h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
		h.mana = 20
		h.take_mana(50)
		self.assertEqual(h.mana, 70)

	def test_take_mana_and_overflow_start_value(self):
		h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
		h.take_mana(100)
		self.assertEqual(h.mana, 100)

	def test_take_mana_without_mana_points(self):
		h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
		h.mana = 70
		h.take_mana()
		self.assertEqual(h.mana, 72)




if __name__ == '__main__':
	unittest.main()
