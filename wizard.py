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
        self.spellBook = {}
        self.win = 0 # Keep track of how much time the player win
        self.lose = 0


    
    def newGame(self):
        with open('save_game.json', 'w') as saveFile:
            json.dump(self.view_player(), fp=saveFile)


    def loadGame(self): #This function isn't necessary but if we are going to use it, it should be to load a pervious user *only if they have played the game already and has save data*
        for file in os.listdir('.'):
            if file == 'save_game.json':
                with open('save_game.json', 'r') as saveFile:
                    data = json.load(saveFile)

                for player in data['Player']:
                    self.name = player['Name']
                    self.characteristics = player['Characteristics']
                    self.element = player['Element']
                    self.attackLevel = player['Attack Level']
                    self.spellBook = player['spells']
                print(f'Welcome back {self.name}\n')

                return self.intro()


    def developerCredits(self) -> None: #This function print our name and show that we created the program
        # return '***Made by***\n1.Demar\n2.Ejeah\n3.David'
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
            'Player': [
            {
            'Name': self.name,
            'Characteristics': self.characteristics,
            'Health': self.health,
            'Element': self.element,
            'Element_Mastered': self.elements_mastered,
            'Win_Count': self.win
            }
            ]

        }

        return json.dumps(results, indent=2)
    
    def view_player(self) -> dict: #we can use this function to show the player attributes

        player_construct = {
            "Player": [
            {

            "Name": self.name,
            "Characteristics": f"{self.characteristics}",
            "Element": f"{self.element}",
            "Health": f"{self.health}%",
            "Attack Level": self.attackLevel,
            "spells": self.spellBook

            }
            ]
        }
        
        return player_construct

    def menu(self) -> None:
        files = [file for file in os.listdir('.')]

        if 'save_game.json' not in files:
            print('Before you can load a game, you must start a new game and create a user, after the game ends you can use the load game function\n')


        print('1.New Game\n2.Player Info\n3.Load Game\n4.Credits')
        _menu_choice = input('Enter menu choice: ')

        if _menu_choice == '1':
            self.getter_setter()

        elif _menu_choice == '2':

            if self.name == None:
                print('no user\n')
                return self.menu()
            else:
                print(self.view_player())
                return self.menu()

        elif _menu_choice == '3':
            self.loadGame()
            if self.name == None:
                print('[+]User file not found, create user\n')      
            return self.menu()

        elif _menu_choice == '4':
            self.developerCredits()
            return self.menu()
        
        else:
            print('Enter a valid option\n')
            return self.menu()

    def element_info(self): #This function gets the user info (eg: name and characteristics)
        content = {

            'Aggressive': 'Get assigned fire with high attack power but lower life',
            'Relaxed': 'Get water with balanced stats',
            'Protective': 'Get high health but lower attack and life/earth element'

        }

        return json.dumps(content, indent=2)

    
    def set_elements(self, characteristics:str): #We can use this function to store and set all the elements and health level: water,fire,wind,earth
        _elements = ['water', 'fire', 'earth']
        water_spells = {'water dragon': 10, 'water pellet': 12, 'water shield': 'block'}
        fire_spells = {'dragon flames': 10}
        earth_spells = {}

        if characteristics == 'aggressive':
            self.element = _elements[1]
            self.health = 70
            self.attackLevel = 100
            self.spellBook = fire_spells
        elif characteristics == 'relaxed':
            self.element = _elements[0]
            self.health = 80
            self.attackLevel = 80
            self.spellBook = water_spells
        elif characteristics == 'protective':
            self.element = _elements[2]
            self.health = 100
            self.attackLevel = 65
            self.spellBook = earth_spells


    def getter_setter(self): #This function can be used to set the elements, characteristics and name to a player
        self.clear_screen()
        get_name = input('Enter your username: ')
        print(self.element_info())
        get_characteristic = input(f'Enter your character traits {self.character_traits()}: ')
        
        if get_characteristic.lower() in [x.lower() for x in self.character_traits()]:
            self.characteristics = get_characteristic.lower()
            self.set_elements(self.characteristics)
            self.name = get_name
            self.newGame()
            return self.intro()

        else:
            print('Enter a valid answer')
            self.getter_setter()


    def character_traits(self): #We can use this function to get the characteristics of the players
        type_of_characteristics = ['Aggressive', 'Relaxed', 'Protective']
        return type_of_characteristics




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
        # print(game.getter_setter())
        print(game.menu())
    except KeyboardInterrupt:
        sys.exit()
    except json.JSONDecodeError:
        print('[+]check your save data, made it is corrupt. Try making a new game')
    except Exception as e:
        print(e)