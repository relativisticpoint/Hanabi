import random
import pyspiel
import numpy as np
from hanabi_learning_environment import pyhanabi
import sys

def random_bot():
    game = pyspiel.load_game('hanabi')
    state = game.new_initial_state()
    i=0
    while not  state.is_terminal() : # tant que le jeu n'est pas terminé (il reste des jetons de vie et le score < 25)
        legal_actions = state.legal_actions() # avoir accès aux actions possibles 
        random_action = np.random.choice(legal_actions) #on tire une action random dans le set des actions possibles 
        state.apply_action(random_action) #on execute l'action qui a été choisie de manière aléatoire 
        i+=1 #simple compteur pour connaître le 
    string = ''
    sys.stdout = open("scores_random.txt",'a')
    print(state)

    print("nombre de tours {}".format(i))

if __name__ == "__main__" :
    for i in range(50000):
        random_bot()
        


