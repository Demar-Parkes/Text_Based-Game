import json
import os

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


    def Credits(self): #This function print our name and show that we created the program
        return '***Made by***\n1.Demar\n2.Ejeah\n3.David'

    
    def clear_screen(self): #This function is to just simply clear the terminal screen, you can google it: os.system('cls')
        if os.name == 'nt':
            os.system('cls')

        elif os.name == 'posix':
            os.system('clear')

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
    
    def view_player(self):

        player_construct = {
            'Name': self.name,
            'Characteristics': f'{self.characteristics}',
            'Element': f'{self.element}',
            'Health': f'{self.health}%',
            'Attack Level': self.attackLevel
            }
        
        return json.dumps(player_construct, indent=2)

    def menu(self):
        print('1.Start Game\n2.Player Info\n3.Credits')
        _menu_choice = input('Enter menu choice: ')

        if _menu_choice == '1':
            pass
        elif _menu_choice == '2' and self.name != None:
            return self.view_player()
        elif _menu_choice == '3':
            return self.Credits()


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


    def getter_setter(self): #This function can be used to set the elements, characteristics and name to a player
        self.clear_screen()
        get_name = input('Enter your username: ')
        print(self.element_info())
        get_characteristic = input(f'Enter your character traits {self.character_traits()}: ')
        
        if get_characteristic.lower() in [x.lower() for x in self.character_traits()]:
            self.characteristics = get_characteristic.lower()
            self.set_elements(self.characteristics)
            self.name = get_name
            return self.menu()

        else:
            print('Enter a valid answer')
            self.getter_setter()


    def character_traits(self): #We can use this function to get the characteristics of the players
        type_of_characteristics = ['Aggressive', 'Relaxed', 'Protective']

        return type_of_characteristics


    def spell_book(self):
        pass


game = Player()
print(game.getter_setter())