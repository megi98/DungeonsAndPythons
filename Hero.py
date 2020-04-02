from character import Character

class Hero(Character):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        Character.__init__(self, health, mana)
        self.title = title
        self.__max_mana = mana
        self.mana = mana #current mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.equiped = None
        self.spell = None

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        return super().is_alive()
        
    def get_health(self):
        return super().get_health()

    def take_damage(self, damage_points):
        super().take_damage(damage_points)

    def get_mana(self):
        return super().get_mana()

    def can_cast(self):
        if self.spell is not None and self.mana > 0:
            return True
        return False

    def take_healing(self, healing_points):
        return super().take_healing()

    def take_mana(self, mana_points=None):
        if mana_points is None:
             mana_points = self.mana_regeneration_rate
        else:
            self.mana += mana_points

        if self.mana > self.start_mana:
            self.mana = self.start_mana

    def equip(self, weapon:Weapon):
        self.equiped = weapon

    def learn(self, spell:Spell):
        self.spell = spell

    def attack(self, by=None):
        if by == 'weapon':
            if self.equiped is not None:
                return self.equiped.damage

        if by == 'magic':
            if self.spell is not None:
                if self.mana >= self.spell.mana_cost:
                    self.mana -= self.spell.mana_cost
                    return self.spell.damage

        return 0