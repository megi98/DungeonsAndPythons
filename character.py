class Character:

	def __init__(self, health, mana):

		self.health = health
		self.mana = mana
		self.start_heal = health
		self.start_mana = mana


	def is_alive(self):

		assert self.health >= 0, 'Incorrect health.'

		if self.health == 0:
			return False
		else:
			return True


	def get_health(self):

		return self.health


	def get_mana(self):

		return self.mana


	def take_healing(self, healing_points):

		if not self.is_alive():
			return False

		if healing_points + self.health > self.start_heal:
			self.health = self.start_heal
		else:
			self.health += healing_points

		return True


	def take_mana(self, mana_points):

		if mana_points + self.mana > self.start_mana:
			self.mana = self.start_mana
		else:
			self.mana += mana_points


	def take_damage(self, damage_points):

		if damage_points > self.health:
			self.health = 0
		else:
			self.health -= damage_points





		

