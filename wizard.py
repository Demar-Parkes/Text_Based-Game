import json

class Player:
    def __init__(self, name, characteristics=None, health=None, element=None, AttackLevel=None): # This function initializes the player
        self.name = name
        self.characteristics = characteristics
        self.health = health
        self.element = element
        self.attackLevel = AttackLevel


    
    def set_elements(self, characteristics): #We can use this function to store and set all the elements and health level: water,fire,wind,earth
        _elements = ['water', 'fire', 'earth', 'air']
        if characteristics == 'aggressive':
            self.element = _elements[1]
            self.health = 50
            self.attackLevel = 100
        elif characteristics == 'relaxed':
            self.element = _elements[0]
            self.health = 70
            self.attackLevel = 70
        elif characteristics == 'protective':
            self.element = _elements[2]
            self.health = 100
            self.attackLevel = 50


    def getter_setter(self): #This function can be used to set the elements and characteristics to a player
        get_characteristic = input(f'Enter your character traits {self.character_traits()}: ')
        
        if get_characteristic.lower() in [x.lower() for x in self.character_traits()]:
            self.characteristics = get_characteristic
            self.set_elements(self.characteristics)
        else:
            print('Enter a valid answer')
            self.getter_setter()

        player_construct = {
            'Characteristics': f'{self.characteristics}',
            'Element': f'{self.element}',
            'Health': f'{self.health}%',
            'Attack Level': self.attackLevel
        }

        return json.dumps(player_construct, indent=2)


    def character_traits(self): #We can use this function to get the characteristics of the players
        type_of_characteristics = ['Aggressive', 'Relaxed', 'Protective']

        return type_of_characteristics


    def spell_book(self):
        pass



game = Player('Demar')
print(game.getter_setter())