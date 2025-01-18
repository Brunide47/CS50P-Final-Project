
#this is an imported module that create a series of personalized input to put in the prompt during the pytest
from input_module import set_keyboard_input
import pytest
from Player import Player
from project import this_or_that , get_results , give_me_value


@pytest.mark.parametrize("initial_name,input_names , expected_name", [
    ("Messi",["Lionel"],"Lionel Messi"),
    ("messi",["lionel"],"Lionel Messi"),
    ("messi",["lio","Leo","Lione","lionel"],"Lionel Messi"),
    ("Anguissa",[],"Anguissa")
    ])
#im'testing the name.setter function with different input from the user
def test_name_setter(initial_name,input_names,expected_name):
    set_keyboard_input(input_names)
    player=Player(initial_name)
    assert player.name==expected_name





@pytest.mark.parametrize("initial_name1, initial_name2, name_inputs, expected_result, wrong_result",[
    ("Messi","Ronaldo",["Lionel","Cristiano"],"1","2"),
    ("Osimhen","Kvaratskhelia",["Khvicha"],"1","2"),
    ("Messi","Messi",["Lionel","Lionel"],"same","1")
    ])
#i'm testing the functuon creating two different player objects with a series of name
def test_this_or_that(initial_name1,initial_name2,name_inputs,expected_result,wrong_result):
    set_keyboard_input(name_inputs)
    player1=Player(initial_name1)
    player2=Player(initial_name2)
    assert get_results(player1,player2)==expected_result
    assert this_or_that(player1,player2,wrong_result)=="False!!!"
    assert this_or_that(player1,player2,expected_result)=="True!!!"



@pytest.mark.parametrize("initial_name, input_names, complete_name, value",[
    ("ronaldo",["cri" , "cr7" , "cristiano"], "Cristiano Ronaldo", 15.0),
    ("leao",["rafa" , "rafael"], "Rafael Leao", 90.0)
    ])
def test_give_me_value(initial_name, input_names, complete_name, value):
    set_keyboard_input(input_names)
    assert give_me_value(initial_name)==f"The Value of {complete_name} is {value}Mln"










