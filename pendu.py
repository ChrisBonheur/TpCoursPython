#! /usr/bin/env python3
# coding: utf-8
import re

import module.program as program


#first, loading for saving page
liste = ["maman", "papa", "Ecole", "Village", "ubuntu", "royale"]
players = program.get_file()

def print_info(name, score, chance_number):
    print("Reférences : ")
    print("Nom = ", name)
    print("Score = ", score)
    print("Essaie restant = ", chance_number)


def start_game():
    """Begin game and return word found by player"""
    game = program.GameSystem(liste)
    word_letters = game.split_word_shuffle()
    print("Former un mot à partir des {} lettres suivantes : {}".format(len(word_letters), word_letters))

    appelation = {
                    1: "première",
                    2: "deuxième",
                    3: "troisième",
                    4: "quatrième",
                    5: "cinqième",
                    6: "sixième",
                    7: "septième",
                    8: "huitième"
                }

    #Show asterics on no input letters
    asterics = []
    for letter in word_letters:
        asterics.append("*")

    i = 0 # for appellation
    i2 = 0 # for asterics items
    for letter in word_letters:
        i += 1 #incement by 1 before using because appelation begin by key[1]
        input_letter = input("Tapez votre {} lettre : ".format(appelation[i]))
        try:
            assert input_letter in word_letters
        except TypeError as e:
            print('Erreur')
        except AssertionError:
            print('La lettre {} ne figure pas dans la liste'.format(input_letter))
        else:
            asterics[i2] = input_letter
        finally:
            while input_letter not in word_letters:
                input_letter = input("Tapez à nouveau votre {} lettre : ".format(appelation[i]))
                asterics[i2] = input_letter
            join_input = "".join(asterics)
            print("Evolution : {}".format(join_input))
        i2 += 1 #increment by 1 after using it, because starics index begin by 0

    word_found = join_input
    return word_found



def set_player(name):
    """create the player name"""
    player = program.Player(name, players)
    return player

def save_new_player(play):
    player = play
    players[player.name] = {"nom": player.name, "score": player.score, "nombre retant": player.trying_chance}
    program.written_on_file(players)

"""def save_player():
    player = set_player()
    program.written_on_file(players["player.nom"] = {
                                                    "nom": player.nom,
                                                    "score": player.score,
                                                    "nombre restant": player.score
                                                  }
                            )"""

def main():
    name = input('Entrez votre nom : ')
    while name == 0:
        print('Le nom utilisé est invalide, Veuillez saisir à nouveau')
        name = input('Entrez votre nom f: ')
    object_player = set_player(name)

    if object_player.player_exist == False:
        save_new_player(object_player)
        print("Votre nouveau nom a bien été ajouté !")

    print_info(object_player.name, object_player.score, object_player.trying_chance)
    word_found = start_game()

    for word in liste:
        if word_found == word:
            word_exist = True
        elif word_found != word:
            word_exist = False

    if word_exist == True:
        texte = """
                  #########################################################
                  ############# FELICITATION MOT TROUVE ! #################
                  #########################################################
                """
        print(texte)
        object_player.boost_score
    else:
        texte = "******************* ECHEC ***********************"
        print(texte)
        object_player.drop_trying_chance

    print_info(object_player.name, object_player.score, object_player.trying_chance)


if __name__ == '__main__':
    main()
