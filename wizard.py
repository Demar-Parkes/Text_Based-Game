import json

class Player:
    def __init__(self, name=None, characteristics=None, health=None, element=None, AttackLevel=None): # This function initializes the player
        self.name = name
        self.characteristics = characteristics
        self.health = health
        self.element = element
        self.attackLevel = AttackLevel
        self.elements_mastered = [] # To keep track of the elements the player has mastered: At the end of the game, the length of the list must be 3.
        self.win = 0 # Keep track of how much time the player win
        self.lose = 0

    def endGameStats(self): #we can use this function to show the player end results
        print('###########END GAME STATS############')
        results = {
            'Name': self.name,
            'Characteristics': self.characteristics,
            'Health': self.health,
            'Element': self.element,
            'Element_Mastered': self.elements_mastered,
            'Win_Count': self.win
        }

        return json.dumps(results, indent=2)


    def element_info(self): #This function gets the user info (eg: name and characteristics)
        content = {

            'Aggressive': 'Get assigned fire with high attack power but lower life',
            'Relaxed': 'Get water with balanced stats',
            'Protective': 'Get high health but lower attack and life/earth element'

        }

        return json.dumps(content, indent=2)

    
    def set_elements(self, characteristics:str): #We can use this function to store and set all the elements and health level: water,fire,wind,earth
        _elements = ['water', 'fire', 'earth', 'air']
        if characteristics == 'aggressive':
            self.element = _elements[1]
            self.health = 70
            self.attackLevel = 100
        elif characteristics == 'relaxed':
            self.element = _elements[0]
            self.health = 80
            self.attackLevel = 80
        elif characteristics == 'protective':
            self.element = _elements[2]
            self.health = 100
            self.attackLevel = 65


    def getter_setter(self): #This function can be used to set the elements, characteristics and name to a player
        get_name = input('Enter your username: ')
        print(self.element_info())
        get_characteristic = input(f'Enter your character traits {self.character_traits()}: ')
        
        if get_characteristic.lower() in [x.lower() for x in self.character_traits()]:
            self.characteristics = get_characteristic.lower()
            self.set_elements(self.characteristics)
            self.name = get_name

        else:
            print('Enter a valid answer')
            self.getter_setter()

        player_construct = {
            'Name': self.name,
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


game = Player()
print(game.getter_setter())
print("Your journey will now begin young one... the wind breeze is cold from your left, but warm air is coming from your right")
direction_1 = str(input("Right or left?"))
