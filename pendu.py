#! /usr/bin/env python3
# coding: utf-8
import re

from module import save_db, program


#first, loading for saving page
liste = ["maman", "papa", "Ecole", "Village", "ubuntu", "royale"]
players = save_db.get_on_file()

def print_info(object_player):
    print("Reférences : ")
    print("Nom = ", object_player.name)
    print("Score = ", object_player.score)
    print("Essaie restant = ", object_player.trying_chance)


def start_game():
    """Begin game and return word found by player"""
    GenerateWord = program.GenerateWord(liste)
    word_letters = GenerateWord.split_word_shuffle
    print("\nFormer un mot à partir des {} lettres suivantes : {}".format(len(word_letters), word_letters))

    #this variableList is Using in the invite command to show number of a case
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
        #duplicate word_letters to remove used word_letters ĵust inside loop "for"
        #to avoid to break length of initial word_letter
        word_letters = list(word_letters)

        i += 1 #increment by 1 before using "i" because appelation begin by key[1]
        input_letter = input("\nTapez votre {} lettre : ".format(appelation[i]))
        try:
            assert input_letter in word_letters
        except AssertionError:
            print('\nLa lettre {} ne figure pas dans la liste'.format(input_letter))
        else:
            asterics[i2] = input_letter
        finally:
            while input_letter not in word_letters:
                input_letter = input("\nTapez à nouveau votre {} lettre : ".format(appelation[i]))
                asterics[i2] = input_letter
                if input_letter not in word_letters:
                    print('\nLa lettre {} ne figure pas dans la liste'.format(input_letter))
            join_input = "".join(asterics)
            print("Evolution : {}".format(join_input))
        word_letters.remove(input_letter)
        i2 += 1 #increment by 1 after using "i2", because asterics index begin by 0

    word_found = join_input
    return word_found


def main():
    players_list = save_db.get_on_file()

    name = input('Entrez votre nom : ')
    while name == 0:
        print('Le nom utilisé est invalide, Veuillez saisir à nouveau')
        name = input('Entrez votre nom f: ')

    if program.Player(name).is_existed(players_list):
        player_selected = players_list[name]
        player = program.Player(name, player_selected["score"], player_selected["trying_chance"])
    else:
        player = program.Player(name)
        #adding new player in players_lists
        players_list[player.name] = {"score": player.score, "trying_chance": player.trying_chance}
        #saving new players_list with adding new player
        save_db.save_on_file(players_list)
        print("Nouvel utilisateur ajouté avec succès !")

    print_info(player)
    word_found = start_game()

    if word_found in liste:
        word_exist = True
    elif word_found not in liste:
        word_exist = False

    if word_exist == True:
        texte = """
                  #########################################################
                  ############# FELICITATION MOT TROUVE ! #################
                  #########################################################
                """
        print(texte)
        player.boost_score
    else:
        texte = "******************* ECHEC ***********************"
        print(texte)
        player.losing_chance

    print_info(player)
    #adding new player in players_lists
    players_list[player.name] = {"score": player.score, "trying_chance": player.trying_chance}
    #saving new players_list with adding new player
    save_db.save_on_file(players_list)


if __name__ == '__main__':
    main()
