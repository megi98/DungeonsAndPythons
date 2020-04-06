from character import Character


class Enemy(Character):

	def __init__(self, health, mana, damage):

		super().__init__(health, mana)
		self.damage = damage


	def is_alive(self):

		return super().is_alive()


	def can_cast(self, mana_cost):

		return super().can_cast(mana_cost)


	def get_health(self):

		return super().get_health()


	def get_mana(self):

		return super().get_mana()


	def take_healing(self, healing_points):

		return super().take_healing(healing_points)


	def take_mana(self, mana_points):

		super().take_mana(mana_points)


	def equip(self, weapon):

		super().equip(weapon)


	def learn(self, spell):

		super().learn(spell)


	def attack(self, by=''):

		if by == '':
			return self.damage

		else:
			return super().attack(by)	


	def take_damage(self, damage_points):

		super().take_damage(damage_points)


	def take_mana_damage(self, damage_points):

		super().take_mana_damage(damage_points)
