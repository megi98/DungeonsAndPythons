import sys
import random
from hero import Hero
from enemy import Enemy
from weaponAndSpell import (Weapon, Spell)
from fight import Fight



class Dungeons:

	def __init__(self, file):

		self.file = file
		self.gateway = ()
		self.start_points = []
		self.matrix = []
		self.hero = None
		self.hero_coordinates = ()


	def init_matrix(self):

		f = open(self.file, 'r')
		lines = f.readlines()
		f.close()

		for line in lines:
			self.matrix.append(line.strip())


	def get_matrix(self):

		return self.matrix


	def print_map(self):

		for line in self.matrix:
			print(line.strip())


	def find_start(self):

		result = []
		n = len(self.matrix)
		m = len(self.matrix[0])

		for i in range(n):
			for j in range(m):
				if self.matrix[i][j] == 'S':
					self.start_points.append((i, j))

		return self.start_points


	def find_gateway(self):

		result = ()
		n = len(self.matrix)
		m = len(self.matrix[0])

		for i in range(n):
			for j in range(m):
				if self.matrix[i][j] == 'G':
					self.gateway = i, j
					
		return self.gateway


	def spawn(self, hero):

		if len(self.find_start()) == 0:
			return False

		else:
			our_start = self.find_start()[0]
			self.hero_coordinates = our_start
			x = our_start[0]
			self.matrix[x] = self.matrix[x].replace('S', 'H', 1)
			self.find_start().pop(0)
			return True


	def get_hero_coordinates(self):

		return self.hero_coordinates


	@staticmethod
	def pick_treasure():

		#list with the name and the value of the random picked treasure
		picked_treasure = []

		treasures = {
			'health': 30,
			'mana': 20,
			'weapon': Weapon('The Axe of Destiny', 20),
			'spell': Spell('Fireball', 30, 50, 2)
		}
		
		picked_treasure.append(random.choice(list(treasures.keys())))
		picked_treasure.append(treasures[picked_treasure[0]])

		return picked_treasure


	@staticmethod
	def pick_enemy():

		enemies = [Enemy(50, 20, 10), Enemy(100, 50, 20), Enemy(80, 30, 30), Enemy(90, 55, 25)]

		return random.choice(enemies)


	def move_hero(self, direction):

		x = self.hero_coordinates[0]
		y = self.hero_coordinates[1] 
		
		if direction is 'up':

			if x - 1 < 0 or self.matrix[x-1][y] == '#':
				return False

			elif self.matrix[x-1][y] == '.':

				self.matrix[x-1] = list(self.matrix[x-1])
				self.matrix[x] = list(self.matrix[x])
				self.matrix[x-1][y] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x-1] = ''.join(self.matrix[x-1])
				self.matrix[x] = ''.joim(self.matrix[x])
				self.hero_coordinates = x-1, y
				return True

			elif self.matrix[x-1][y] == 'T':

				treasure = self.pick_treasure()
				self.matrix[x-1] = list(self.matrix[x-1])
				self.matrix[x] = list(self.matrix[x])
				self.matrix[x-1][y] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x-1] = ''.join(self.matrix[x-1])
				self.matrix[x] = ''.joim(self.matrix[x])
				self.hero_coordinates = x-1, y

				if treasure[0] is 'health':
					print('Found health potion!')
					self.hero.take_healing(treasure[1])

				elif treasure[0] is 'mana':
					print('Found mana potion!')
					self.hero.take_mana(treasure[1])

				elif treasure[0] is 'weapon':
					print('Found a weapon!')
					self.hero.equip(treasure[1])

				else:
					print('Found a spell!')
					self.hero.learn(treasure[1])

			else:
				enemy = self.pick_enemy()
				fight = Fight(self.hero, enemy)

		elif direction is 'down':

			if x + 1 < 0 or self.matrix[x+1][y] == '#':
				return False

			elif self.matrix[x+1][y] == '.':

				self.matrix[x+1] = list(self.matrix[x+1])
				self.matrix[x] = list(self.matrix[x])
				self.matrix[x+1][y] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x+1] = ''.join(self.matrix[x+1])
				self.matrix[x] = ''.join(self.matrix[x])
				self.hero_coordinates = x+1, y
				return True

			elif self.matrix[x+1][y] == 'T':

				treasure = self.pick_treasure()

				self.matrix[x+1] = list(self.matrix[x+1])
				self.matrix[x] = list(self.matrix[x])
				self.matrix[x+1][y] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x+1] = ''.join(self.matrix[x+1])
				self.matrix[x] = ''.join(self.matrix[x])
				self.hero_coordinates = x+1, y

				if treasure[0] is 'health':
					print('Found health potion!')
					self.hero.take_healing(treasure[1])

				elif treasure[0] is 'mana':
					print('Found mana potion!')
					self.hero.take_mana(treasure[1])

				elif treasure[0] is 'weapon':
					print('Found a weapon!')
					self.hero.equip(treasure[1])

				else:
					print('Found a spell!')
					self.hero.learn(treasure[1])

			else:
				enemy = self.pick_enemy()
				fight = Fight(self.hero, enemy)

		elif direction is 'left':

			if y - 1 < 0 or self.matrix[x][y-1] == '#':
				return False

			elif self.matrix[x][y-1] == '.':

				self.matrix[x] = list(self.matrix[x])
				self.matrix[x][y-1] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x] = ''.join(self.matrix[x])
				self.hero_coordinates = x, y-1
				return True

			elif self.matrix[x][y-1] == 'T':

				treasure = self.pick_treasure()
				self.matrix[x] = list(self.matrix[x])
				self.matrix[x][y-1] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x] = ''.join(self.matrix[x])
				self.hero_coordinates = x, y-1

				if treasure[0] is 'health':
					print('Found health potion!')
					self.hero.take_healing(treasure[1])

				elif treasure[0] is 'mana':
					print('Found mana potion!')
					self.hero.take_mana(treasure[1])

				elif treasure[0] is 'weapon':
					print('Found a weapon!')
					self.hero.equip(treasure[1])

				else:
					print('Found a spell!')
					self.hero.learn(treasure[1])

			else:
				enemy = self.pick_enemy()
				fight = Fight(self.hero, enemy)

		else:

			if y + 1 < 0 or self.matrix[x][y+1] == '#':
				return False

			elif self.matrix[x][y+1] == '.':

				self.matrix[x] = list(self.matrix[x])
				self.matrix[x][y+1] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x] = ''.join(self.matrix[x])

				self.hero_coordinates = x, y+1
				return True

			elif self.matrix[x][y+1] == 'T':

				treasure = self.pick_treasure()

				self.matrix[x] = list(self.matrix[x])
				self.matrix[x][y+1] = 'H'
				self.matrix[x][y] = '.'
				self.matrix[x] = ''.join(self.matrix[x])

				self.hero_coordinates = x, y+1

				if treasure[0] is 'health':
					print('Found health potion!')
					self.hero.take_healing(treasure[1])

				elif treasure[0] is 'mana':
					print('Found mana potion!')
					self.hero.take_mana(treasure[1])

				elif treasure[0] is 'weapon':
					print('Found a weapon!')
					self.hero.equip(treasure[1])

				else:
					print('Found a spell!')
					self.hero.learn(treasure[1])

			else:
				enemy = self.pick_enemy()
				fight = Fight(self.hero, enemy)





def main():

	d = Dungeons("level1.txt")
	d.init_matrix()
	d.print_map()
	print(d.find_start())
	print(d.find_gateway())
	hero = Hero('name', 'title', 100, 50, 2)
	print(d.spawn(hero))
	print(d.get_hero_coordinates())
	d.print_map()
	d.move_hero('right')
	d.move_hero('down')
	d.print_map()


if __name__ == '__main__':
	main()

