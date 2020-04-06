from hero import Hero
from enemy import Enemy


class Fight:

	def __init__(self, hero, enemy):

		self.hero = hero
		self.enemy = enemy
		
		
	def hero_attack(self):

		if self.hero.attack(by='spell') > self.hero.attack(by='weapon') and self.hero.can_cast(self.hero.spell.get_mana_cost()):

			self.enemy.take_damage(self.hero.attack(by='spell'))
			self.hero.take_mana_damage(self.hero.spell.get_mana_cost())
			print(f'Hero casts a {self.hero.spell.name}, hits enemy for {self.hero.spell.get_damage()} dmg. Enemy health is {self.enemy.get_health()}')

		elif self.hero.attack(by='spell') == self.hero.attack(by='weapon') == 0:

			print('Hero does not have anything to attack with. Enemy health is unaffected')

		else:

			self.enemy.take_damage(self.hero.attack(by='weapon'))
			print(f'Hero hits with {self.hero.weapon.name} for {self.hero.weapon.get_damage()} dmg. Enemy health is {self.enemy.get_health()}')


	def enemy_attack(self):

		enemy_damage = self.enemy.attack()
		weapon_damage = self.enemy.attack(by='weapon')
		spell_damage = self.enemy.attack(by='spell')

		if spell_damage > enemy_damage and spell_damage > weapon_damage and self.enemy.can_cast(self.enemy.spell.get_mana_cost()):

			self.hero.take_damage(spell_damage)
			self.enemy.take_mana_damage(self.enemy.spell.get_mana_cost())
			print(f'Enemy casts a {self.enemy.spell.name}, hits hero for {self.enemy.spell.get_damage()} dmg. Hero health is {self.hero.get_health()}')

		elif weapon_damage > enemy_damage:

			self.hero.take_damage(weapon_damage)
			print(f'Enemy hits with {self.enemy.weapon.name} for {self.enemy.weapon.get_damage()} dmg. Hero health is {self.hero.get_health()}')

		else:

			self.hero.take_damage(enemy_damage)
			print(f'Enemy hits hero for {enemy_damage} dmg. Hero health is {self.hero.get_health()}')


	def start_fight(self):

		while self.hero.is_alive() and self.enemy.is_alive():

			self.hero_attack()
			if self.enemy.is_alive():
				self.enemy_attack()

		if self.hero.is_alive() is False:
			print('Hero is dead!')

		else:
			print('Enemy is dead!')
			print('Our hero can continue through the dungeon.')
