import sys
import random
from hero import Hero
from enemy import Enemy
from weaponAndSpell import (Weapon, Spell)



class Dungeons:

	def __init__(self, file):

		self.file = file
		self.gateway = ()
		self.start_points = []
		self.matrix = []
		self.hero_coordinates = ()



	def print_map(self):

		f = open(self.file, 'r')
		lines = f.readlines()
		f.close()

		for line in lines:
			print(line.strip())

		return


	def init_matrix(self):

		f = open(self.file, 'r')
		lines = f.readlines()
		f.close()

		for line in lines:
			self.matrix.append(line.strip())

		return self.matrix


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


	def move_hero(self, directions):
		pass


	@staticmethod
	def pick_treasure():

		treasures = ['health', 'mana', 'spell', 'weapon']
		return random.choice(treasures)





def main():

	d = Dungeons("level1.txt")
	d.print_map()
	print(d.init_matrix())
	print(d.find_start())
	print(d.find_gateway())
	hero = 9
	print(d.spawn(hero))
	print(d.matrix)
	print(d.pick_treasure())


if __name__ == '__main__':
	main()



