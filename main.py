#!/usr/bin/python3

import manager
import sys

if __name__ ==  "__main__":
    y = manager.Team("Prem")
    y.loadTeam()
    y.show()

    sys.stdout.flush()
