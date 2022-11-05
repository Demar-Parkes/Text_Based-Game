import sys
import json
import os

class Player: # This class is for the game logic, so we can keep the print functions out of it
    def __init__(self, name=None, characteristics=None, health=None, element=None, AttackLevel=None): # This function initializes the player
        self.name = name
        self.characteristics = characteristics
        self.health = health
        self.element = element
        self.attackLevel = AttackLevel
        self.elements_mastered = [] # To keep track of the elements the player has mastered: At the end of the game, the length of the list must be 3.
        self.win = 0 # Keep track of how much time the player win
        self.lose = 0


    def developerCredits(self) -> None: #This function print our name and show that we created the program
        # return '***Made by***\n1.Demar\n2.Ejeah\n3.David'
        # print(" %-*s  %s" % (13,'b', '*'*100))

        print('*'*15, sep=' ')

        print('*  Made By\n*\n*   Demar\n*   Ejeah\n*   David\n*')
        
        print('*\n'*0, end='')

        print('*'*15)

    def clear_screen(self) -> None: #This function is to just simply clear the terminal screen, you can google it: os.system('cls')
        if os.name == 'nt':
            os.system('cls')

        elif os.name == 'posix':
            os.system('clear')

    def endGameStats(self) -> dict: #we can use this function to show the player end results
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
    
    def view_player(self) -> dict: #we can use this function to show the player attributes

        player_construct = {
            'Name': self.name,
            'Characteristics': f'{self.characteristics}',
            'Element': f'{self.element}',
            'Health': f'{self.health}%',
            'Attack Level': self.attackLevel
            }
        
        return json.dumps(player_construct, indent=2)

    def menu(self) -> None:
        print('1.Start Game\n2.Player Info\n3.Credits')
        _menu_choice = input('Enter menu choice: ')

        if _menu_choice == '1':
            self.intro()
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


class Game(Player): # Add scene info within this class
    def __init__(self):
        super().__init__()

    def intro(self):
        print("Your journey will now begin young one... the wind breeze is cold from your left, but warm air is coming from your right")
        direction_1 = input('which direction would you like to turn [[R]ight, [L]eft]: ')


    def scene2(self):
        pass

    def scene3(self):
        pass



if __name__ == '__main__':
    try:
        game = Game()
        print(game.getter_setter())
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(e)