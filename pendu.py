#! /usr/bin/env python3
# coding: utf-8
import re

import module.program as program


#first, loading for saving page
liste = ["maman", "papa", "Ecole", "Village", "ubuntu", "royale"]
players = program.get_file()



def start_game(name, score, chance_number):
    print("Reférences : ")
    print("Nom = ", name)
    print("Score = ", score)
    print("Essaie restant = ", chance_number)
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
                    8: "huitième"}
    i = 0
    input_word = []
    for letter in word_letters:
        i += 1
        input_letter = input("Tapez votre {} lettre : ".format(appelation[i]))
        try:
            assert input_letter in word_letters
        except TypeError as e:
            print('Erreur')
        except AssertionError:
            while input_letter not in word_letters:
                print('La lettre entée ne figure pas dans la liste')
                input_letter = input("Tapez à nouveau votre {} lettre : ".format(appelation[i]))
        else:
            input_word.append(input_letter)
            def print_evolution_word(*letters):
                pass
            join_input = join()
            print("Evolution : {}".format())



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

    start_game(object_player.name, object_player.score, object_player.trying_chance)


if __name__ == '__main__':
    main()
