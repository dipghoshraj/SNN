import sys, os
path = os.path.abspath(__file__ + "/../../")
sys.path.append(path)

from learning.bruteForce.bruteForce import bruteForce

bruteForce()