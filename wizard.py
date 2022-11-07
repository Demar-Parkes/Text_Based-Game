import sys
import json
import os
import time

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


    
    def newGame(self): #Create a new game and save to a json file
        with open('save_game.json', 'w') as saveFile:
            json.dump(self.view_player(), fp=saveFile)


    def loadGame(self): #If the player already played our game, they are going to have a save game to be loaded into the program
        for file in os.listdir('.'):
            if file == 'save_game.json':
                with open(file, 'r') as saveFile:
                    data = json.load(saveFile)

                for player in data['Player']:
                    self.name = player['Name']
                    self.characteristics = player['Characteristics']
                    self.element = player['Element']
                    self.attackLevel = player['Attack Level']
                    self.health = player['Health']
                    self.spellBook = player['spells']
                print(f'\n[+]Loading Player: {self.name}\n')
                time.sleep(1)
                print(f'Welcome back, {self.name}\n')

                return self.menu()
    
    def changeFeature(self, user_name=None, element=None): #User can use this function to change attributes about themselves
        for file in os.listdir('.'):
            if file == 'save_game.json':
                with open(file, 'r') as fp:
                    data = json.load(fp)

                for player in data['Player']:
                    if user_name is not None:
                        player['Name'] = user_name
                        self.name = user_name
                    if element is not None:
                        player['Characteristics'] = element
                        self.characteristics = element
                with open(file, 'w') as fp2:
                    json.dump(self.view_player(), fp2, indent=2)


    def developerCredits(self) -> None: #This function print our name and show that we created the program
        print('*'*15, sep=' ')

        print('*  Made By\n*\n*   Demar\n*   Ejeah\n*   David\n*')
        
        print('*\n'*0, end='')

        print('*'*15)


    def clear_screen(self) -> None: #This function is to just simply clear the terminal screen, you can google it: os.system('cls')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def endGameStats(self) -> dict:
        print('###########END GAME STATS############')
        results = {
            'Player': [
            {
            'Name': self.name,
            'Characteristics': self.characteristics,
            'Health': self.health,
            'Element': self.element,
            'Elements_Mastered': self.elements_mastered,
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
            print('[1].New Game\n[2].Player Info\n[3].Load Game\n[4].Credits\n[6].Exit')

        elif 'save_game.json' in files and self.name != None:
            print('[1].New Game\n[2].Player Info\n[3].Load Game\n[4].Credits\n[5].Edit User\n[6].Exit')

        else:
            print('[1].New Game\n[2].Player Info\n[3].Load Game\n[4].Credits\n[6].Exit')

        _menu_choice = input('Enter menu choice: ')

        if _menu_choice == '1':
            self.getter_setter()

        elif _menu_choice == '2':

            if self.name == None:
                print('\n[-]NO USER\n')
                return self.menu()
            else:
                print(json.dumps(self.view_player(), indent=2))
                return self.menu()

        elif _menu_choice == '3':
            self.loadGame()
            count = 0
            if self.name == None and count < 2:
                print('[-]User file not found, create user\n') 
                count +=1    
            return self.menu()

        elif _menu_choice == '4':
            self.developerCredits()
            return self.menu()
        
        elif _menu_choice == '5':
            if self.name != None:
                new_name = input('\nEnter a new name, leave blank if you dont wanna change: ')
                new_characteristics = input(f'\nEnter a new element, leave blank if you dont wanna change {self.character_traits()}: ')

                if new_characteristics == '' and new_name == '':
                    self.changeFeature(self.name, self.characteristics)
                else:
                    self.changeFeature(new_name, self.set_elements(new_characteristics))
                
                return self.menu()
            else:
                print('\n[-]NO USER\n')
                return self.menu()

        elif _menu_choice == '6':
            if self.name == None:
                print('GoodBye! You')
                time.sleep(1)
                sys.exit()
            else:
                print(f'GoodBye! {self.name}')
                time.sleep(1)
                sys.exit()
        
        else:
            print('\n[-]ENTER A VALID OPTION\n')
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
            return characteristics
        elif characteristics == 'relaxed':
            self.element = _elements[0]
            self.health = 80
            self.attackLevel = 80
            self.spellBook = water_spells
            return characteristics
        elif characteristics == 'protective':
            self.element = _elements[2]
            self.health = 100
            self.attackLevel = 65
            self.spellBook = earth_spells
            return characteristics
        else:
            print('\n[-]Unknown characteristics\n')


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
            print('[-]ENTER A VALID ANSWER')
            self.getter_setter()


    def character_traits(self): #We can use this function to get the characteristics of the players
        type_of_characteristics = ['Aggressive', 'Relaxed', 'Protective']
        return type_of_characteristics




class Game(Player): # Add scene info within this class
    def __init__(self):
        super().__init__()

    def intro(self):
        print("Your journey will now begin young one... the wind breeze is cold from your left, but warm air is coming from your right")
        _direction_1 = input('which direction would you like to turn [[R]ight, [L]eft]: ')
        if _direction_1.lower() == 'l':
            pass
        elif _direction_1.lower() == 'r':
            pass

    def scene2(self):
        pass

    def scene3(self):
        pass



if __name__ == '__main__':
    try:
        game = Game()
        print(game.menu())
    except KeyboardInterrupt:
        sys.exit()
    except json.JSONDecodeError:
        print('[+]check your save data, made it is corrupt. Try making a new game')
    except Exception as e:
        print(e)
