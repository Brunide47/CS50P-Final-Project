import requests
import json


class Player():

    def  __init__(self,name):
        """
        :self.name: the player name
        :self.link:link of tranfermarkt associated to the name
        :self.info:dict with the info of the player
        :self.value: actual value of the player

        """
        self.name=name
        self.link=f"https://transfermarkt-api.vercel.app/players/search/{self.name}"
        self.info: list=self.get_info()
        self.value: str=self.get_value()




    def get_info(self):
        """
        return the json converted to dict with the info about the player
        """


        response=requests.get(self.link)
        info=json.loads(response.text)
        info=info["results"]
        return info[0]

    def get_value(self):
        return float(self.info["marketValue"].replace("€","").replace("m",""))

    def get_age(self):
        return self.info["age"]









    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        """
        Check if the player exist in transfermarkt database and if there are more than one player
        with the same name
        :url:link to obtain the json file
        :response:json file
        :info:json converted to a pythonic dict
        :names:all the name of the player with the same last names
        """
        link=f"https://transfermarkt-api.vercel.app/players/search/{new_name.lower().strip()}"
        response=requests.get(link)
        info=json.loads(response.text)
        #verify if the json exist
        if info["results"]!=[]:
            #verify if there are more then one player
            if len(info["results"])>1:
                #create a list with the different player names
                names=[players["name"] for players in info["results"]]
                for name in names:
                    print(name)
                new_name1=input("Choose the name of your player: ").strip().title()
                while True:
                    #try to see if the user input has first and last name
                    try:
                        first,last=new_name1.split(" ")
                        if new_name1 in names:
                            self._name=new_name1
                            break
                        else:
                            new_name1=input("Retry: ").strip().title()
                    #if the input has only the first name
                    except ValueError:
                        first_names=[]
                        for name in names:
                            try:
                                firts,lasts=name.split(" ")
                                first_names.append(firts)
                            except ValueError:
                                first_names.append(name)

                        if new_name1 in first_names:
                            self._name=f"{new_name1} {new_name.title()}"
                            break
                        else:
                            new_name1=input("Retry: ").title().strip()
                            continue


            #if the name of the player is exact
            else:
                self._name=new_name.title()

        #if there isn't a json file
        else:
            raise ValueError("Player does not exist")















class Player_Sorted:
    def __init__(self,name):
        self.name=name
        self.link=f"https://transfermarkt-api.vercel.app/players/search/{self.name}"
        self.value=self.get_float()





    def get_float(self) -> float:
        response=requests.get(self.link)
        info=json.loads(response.text)
        info=info["results"]
        player=info[0]
        return float(player["marketValue"].replace("€","").replace("m",""))


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        """
        Check if the player exist in transfermarkt database and if there are more than one player
        with the same name
        :url:link to obtain the json file
        :response:json file
        :info:json converted to a pythonic dict
        :names:all the name of the player with the same last names
        """
        link=f"https://transfermarkt-api.vercel.app/players/search/{new_name.lower().strip()}"
        response=requests.get(link)
        info=json.loads(response.text)
        #verify if the json exist
        if info["results"]!=[]:
            #verify if there are more then one player
            if len(info["results"])>1:
                #creating a list called infos with a series of dict, containing one name and one value
                infos=[]
                for player in info["results"]:
                    if player["marketValue"]=="-":
                        continue
                    elif "k" in player["marketValue"]:
                        continue
                    else:
                        name=player["name"]
                        value=float(player["marketValue"].replace("€", "").replace("m",""))
                        infos.append({"name":name, "value": value})

                #sorting the infos list in base of the value
                infos=sorted(infos, key=lambda x: x["value"])
                #getting thge most expensive player dict
                most_expensive=infos[int(len(infos)-1)]
                self._name=most_expensive["name"]


            #if the name of the player is exact
            else:
                info=info["results"]
                info=info[0]
                self._name=info["name"]

        #if there isn't a json file
        else:
            raise ValueError("Player does not exist")




















