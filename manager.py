import json
import datetime
import os

class Player:
    def __init__(self, name, num, lvl):
        self.name = name
        self.num = num
        self.lvl = lvl
        self.faltas = 0.0
        self.dayslost = []

    def show(self):
        """
        print("------------------------")
        print("Nombre: ", self.name)
        print("Dorsal:", self.num)
        print("Nivel: ", self.lvl)
        print("Asistencia: " + str(((1 - self.faltas//self.sessions["Num"])*100)) + "%")
        """


    def encode(self):
        return dict({"Name" : self.name, "Num" : self.num, "Lvl" : self.lvl, "Faltas" : self.faltas, "Dias faltados" : self.dayslost})

class Team:
    def __init__(self, name):
        self.name =  name
        self.team = {}
        self.jugs = 0
        self.sessions = {"Num" : 0}

    def addPlayer(self, player):
        self.team["JUGADOR " + str(self.jugs)] = player.encode()
        self.jugs += 1

    def show(self):
        """
#        os.system('clear')
        print("Nº de jugadores: ", self.jugs)

        for i in range(self.jugs):
            x = self.team["JUGADOR "+ str(i)]
            print("------------------------")
            print("Nombre: ", x["Name"])
            print("Dorsal: ", x["Num"])
            print("Nivel: ", x["Lvl"])
            if self.sessions["Num"] == 0:
                div = 1
            else:
                div = self.sessions["Num"]
                res = ("{0:.2f}".format((1.0 - (x["Faltas"]/div))*100))
                print("Asistencia: " + str(res) + "%")
            print("Dias faltados : ", x["Dias faltados"])
        """
        tmp = self.team
        tmp["jugs"] = self.jugs
        tmp["name"] = self.name
        tmp["sessions"] = self.sessions
        print(json.dumps(tmp))



    def saveTeam(self):
        tmp = self.team
        tmp["jugs"] = self.jugs
        tmp["name"] = self.name
        tmp["sessions"] = self.sessions
        f = open('data.dat', 'w')
        f.write(json.dumps(tmp, indent = 4, sort_keys=True))
        f.close()

    def loadTeam(self):
        f = open('data.dat', 'r')
        tmp = f.read()
        tmp = json.loads(tmp)
        self.jugs = tmp["jugs"]
        del tmp["jugs"]
        self.name = tmp["name"]
        self.sessions =  tmp["sessions"]
        del tmp["name"]
        del tmp["sessions"]
        self.team = tmp

    def newEntreno(self, *args):
        self.sessions["Entreno " + str(self.sessions["Num"])] = datetime.datetime.now().strftime("%d %m %Y")
        self.sessions["Num"] += 1
        if len(args) > 1:
            print("session: ", self.sessions["Num"])
            for x in args:
                print("x -> ",x)
                tmp = self.team["JUGADOR "+str(x)]
                tmp["Faltas"] += 1
                print(tmp["Name"] + " : " + str(tmp["Faltas"]))
                tmp["Dias faltados"].append(datetime.datetime.now().strftime("%d %m %Y"))
        else:
            print("Ninguna baja!!!")

    def stats(self):
        print("Equipo: ", self.name)
        print("Nº jugadores, ", self.jugs)
        print("Nº de entrenos:", self.sessions["Num"])


