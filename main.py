#!/usr/bin/python3

import manager

if __name__ ==  "__main__":
    y = manager.Team("Prem")
    y.addPlayer(manager.Player("cayetano", 17, 10))
    y.addPlayer(manager.Player("arnold", 11, 0))
    y.addPlayer(manager.Player("leo", 26, 100))
    y.newEntreno(1,2)
    y.newEntreno(1,2)
    y.newEntreno(0)
    y.show()
    y.saveTeam()
    
    print("\n\n\n\n")
    z=manager.Team("Hey yo")
    z.loadTeam()
    y.show()
    y.stats()
