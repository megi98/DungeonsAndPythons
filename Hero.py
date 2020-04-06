from character import Character
from weaponAndSpell import Weapon, Spell


class Hero(Character):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        
        Character.__init__(self, health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate


    def known_as(self):

        return "{} the {}".format(self.name, self.title)


    def is_alive(self):

        return super().is_alive()


    def get_health(self):

        return super().get_health()


    def take_damage(self, damage_points):

        super().take_damage(damage_points)


    def take_mana_damage(self, damage_points):

        super().take_mana_damage(damage_points)


    def get_mana(self):

        return super().get_mana()


    def can_cast(self, mana_cost):

        return super().can_cast(mana_cost)


    def take_healing(self, healing_points):

        return super().take_healing(healing_points)


    def take_mana(self, mana_points = None):

        #increasing mana in every move
        if mana_points is None:
            mana_points = self.mana_regeneration_rate

        self.mana += mana_points

        if self.mana > self.start_mana:
            self.mana = self.start_mana


    def equip(self, weapon):

        super().equip(weapon)


    def learn(self, spell):

        super().learn(spell)


    def attack(self, by):

        return super().attack(by)
