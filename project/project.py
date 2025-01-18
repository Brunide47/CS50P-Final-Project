from Player import Player, Player_Sorted
import random


"""
Project name: What's the Value?
Name: Riccardo Bruno
Country: Italy
City: Santa Maria Capue Vetere
Age: 17

"""




def main():
    print("1)Give me the value - 2)This or That")
    while True:
        try:
            game: int=int(input("Game Number: "))
            break
        except:
            continue
    if game==1:
        name: str=input("Name of the Player: ")
        print(give_me_value(name))



    elif game==2:
        print("1) Random - 2)Choose the Players")
        while True:
            try:
                mode: int=int(input("Choose the Modality: "))
                break
            except:
                continue



        if mode==1:
            player1,player2=random_players()
            print(f"{player1.name}  or  {player2.name}")
            possible_results=["1","2","same"]
            while True:
                answer=input("Choose between 1,2 or same: ")
                if answer in possible_results:
                    break
                else:
                    continue
            print(this_or_that(player1,player2,answer))





        elif mode==2:
            player1=Player(input("Firt Player: "))
            player2=Player(input("Second Player: "))
            print(f"{player1.name}  or  {player2.name}")
            possible_results=["1","2","same"]
            while True:
                answer=input("Choose between 1,2 or same: ")
                if answer in possible_results:
                    break
                else:
                    continue
            print(this_or_that(player1,player2,answer))












def give_me_value(name) -> str:
    """
    Use Player Class and his istance attribute to see the value of the player

    """
    player=Player(name)
    return f"The Value of {player.name} is {player.value}Mln"





def get_results(player1,player2):
    """
    Compare the value of the two input players and estabilish if the user won


    """
    value1=player1.value
    value2=player2.value
    if value1>value2:
        return "1"
    elif value1<value2:
        return "2"
    else:
        return "same"





def this_or_that(player1,player2,answer):
    result=get_results(player1 , player2)
    if answer==result:
        print(f"{player1.value}Mln  vs  {player2.value}Mln")
        return "True!!!"
    else:
        print(f"{player1.value}Mln  vs  {player2.value}Mln")
        return "False!!!"










def random_players():
    """
    Take to random players from the list of the Top100 ones2

    """
    best_players=[
    "Federico Valverde"
    "Emiliano Martínez",
    "Enzo Fernández",
    "Bukayo Saka",
    "Rafael Leão",
    "Phil Foden",
    "Jamal Musiala",
    "Son Heung-min",
    "Virgil van Dijk",
    "Bruno Fernandes",
    "Bernardo Silva",
    "Olivier Giroud",
    "Josko Gvardiol",
    "Julián Álvarez",
    "Martin Ødegaard",
    "João Cancelo",
    "Ángel Di María",
    "Toni Kroos",
    "Khvicha Kvaratskhelia",
    "Joshua Kimmich",
    "David Alaba",
    "Rúben Dias",
    "Aurélien Tchouaméni",
    "Theo Hernández",
    "Alexis Mac Allister",
    "Rodrigo De Paul",
    "Sofyan Amrabat",
    "Cody Gakpo",
    "Cristiano Ronaldo",
    "Victor Osimhen",
    "Ilkay Gündogan",
    "Antonio Rüdiger",
    "Riyad Mahrez",
    "Marcus Rashford",
    "Luis Díaz",
    "Trent Alexander-Arnold",
    "Gabriel Jesus",
    "Hakim Ziyech",
    "Alphonso Davies",
    "Marquinhos",
    "Dusan Vlahovic",
    "Éder Militão",
    "Marcelo Brozovic",
    "Ousmane Dembélé",
    "Lautaro Martínez",
    "Dominik Livakovic",
    "Cristian Romero",
    "Nicoló Barella",
    "Mike Maignan",
    "Thiago Silva",
    "Hugo Lloris",
    "Mehdi Taremi",
    "Azzedine Ounahi",
    "Kalidou Koulibaly",
    "Lisandro Martínez",
    "Darwin Núñez",
    "Aleksandar Mitrovic",
    "Kyle Walker",
    "Raphaël Varane",
    "Dayot Upamecano",
    "Ciro Immobile",
    "Declan Rice",
    "Frenkie de Jong",
    "Bruno Guimarães",
    "Manuel Neuer",
    "Giorgian de Arrascaeta",
    "Reece James",
    "Serge Gnabry",
    "Sandro Tonali",
    "Andrew Robertson",
    "Leroy Sané",
    "Gabriel Barbosa",
    "Nicolás Otamendi"]
    player1=random.choice(best_players)
    player2=random.choice(best_players)
    player1=Player_Sorted(player1)
    player2=Player_Sorted(player2)
    return player1,player2























if __name__=="__main__":
    main()
