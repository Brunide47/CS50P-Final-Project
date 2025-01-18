### What's the Value?
#### Video Demo:  <URL HERE>
#### Description:



### The Simple Goal of this Program is: find and compare the value of every player!!!

#### Before starting to code "project.py" I create a file called Player.py containing two different classes:

- ___Player___
- ___Player_Sorted___

## Player Class
#### Player class has four different instance variables, but at the moment i will explain only the most important one: self.name


- ##### __SELF.NAME__ This variable has a getter and a setter function. The firt one returns only the value of the variable, the second one has a more complicated setting: infact it uses the requests library to get a json file from an API of the website "transfermarkt"; this website contains all the statisticts on football players, particularly their value and their transfers. After it converts the json file to a pythonic list of dictionary, that contains one dictionary for each player with the last name used by the user in the prompt. All this dictionaries contain keys called "name" with their complete name and one called "marktValue" with their value. So ,because there are many different players with the same name, it asks to the user the first name or the complete name of the player, showing him all the players available. Instead, if there is only one player with this last name or if the user was precise to give the complete name to the prompt, it directly sets the value of the variable name on the complete name of the player.
###### Please Note: The user can also types wrong first names, when he has to choose from the list of names, but the function always asks him to type a different and correct name. If the player typed initially by the user doesn't exist the name setter function raises a ValueError;

- ##### __SELF.LINK__ This variable set, using self.name, the direct link to use with "requests.get" function for obtaining the json file of the specific player from TransferMarkt;

- ##### __SELF.INFO__ This variable (using the get_info method)thought requests and json libraries obtains the single dictionary of the player, using self.name

- ##### __SELF.VALUE__ This variable, thought the get_value method, extracts from self.info dictionary the value of "marktValue" and, by removing the string parts of it (for example "€" or "m"), converts it in a float.

## Player_Sorted class
#### Player_Sorted class has three instance variables and it's a sort of alternative to the Player class with less interaction with the user and so more automation on the research of the player. Also here I starts from the explanation of the most difficult variable: __self.name__

- ##### __SELF.NAME__ This variable is similar to the first one, but in his setter function there is no interaction  with the user. Infact he has only to type the name of the player, also just his last name, and the function will compare all the values of the players with this last name and will choose only the most expensive player;

- ##### __SELF.LINK__ This variable is equal to the Player class one;

- ##### __SELF.VALUE__ This variable, using the get_float method, extracts from the json file converted to dictionary the value of the player and converts it to a float;


# Project
#### After the creation of these two objects, i coded my final project. My idea was to create a program with two different modality:

- #### __Give me the value__  that gives to the user the value of the player chosen by himself;

- #### __This or that__  that gives to the user two alternatives to play:
  - ##### __Random__ in that the user have to guess the most valued player from a comparation of two famous players;

  - ##### __Choose the players__ in that the game is identical but the player compared are chosen by the user himself;

## Functions
- #### **GIVE_ME_VALUE** This function has an attribute that represents the user input (the name of his player). So first it creates an instance using the Player object, with the name of the player. And then returns a string that tells the value of this player, thought the instance variable "self.value";

- #### **GET_RESULT** This function accepts two attributes, which represents two different instances of the object Player or Player_Sorted, and compare the value of the players associated to them, thought the instance variable "self.value";

- #### **RANDOM_PLAYERS** This function, thought the random library, choose randomly two players from the list of the best 100 playes of 2022/2023 season and creates two istance of the object Player_Sorted with them;

- #### **THIS_OR_THAT** The first two attributes of the function are two Player or Player_Sorted instance and the third is the user answer to the game. If the answer is equal to the return value of "get_result" (runned with the same players) it returns True, else False.

## TEST_PROJECT
#### Becaue I create a lot of interactive instance methods and functions I needed a module that allows to me to create a series of personalized inputs to give to the prompts during the pytest. I used a module found on Github, called [tud_test_base.py]("https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491") by "mauricioaniche". Thought this module, and precisely his function "set_keyboard_input", i can create a list of input to give neatly to the prompt automatically during the running of the test. I use also the pytest texture parametrize that allow to me to run a series of test with the same function but with different parametres.
