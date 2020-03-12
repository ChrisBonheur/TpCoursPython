#! /usr/bin/env python3
# coding: utf-8
import random

def read_file(dir_file):
    word_list = []
    with open(dir_file, 'r') as file:
        result = file.readlines()
    return result


class Player:
    """
    docstring for Player, create a new player or
    existing player.
    """
    LOSE_CHANCE = 1
    def __init__(self, name, score=0, trying_chance=8):
        self.name = name
        self.score = score
        self.trying_chance = trying_chance
        self.player_exist = False

    def is_existed(self, players_list):
        """Verificate if player name exist"""
        if self.name in players_list:
            self.player_exist = True
        return self.player_exist

    @property
    def boost_score(self):
        """Boost score with number of trying chance"""
        self.score += self.trying_chance

    @property
    def losing_chance(self):
        """Drop trying_chance"""
        self.trying_chance -= self.LOSE_CHANCE

    @property
    def initialize_game(self):
        self.score = 0
        self.trying_chance = 8



class GenerateWord:
    """GameSystem controle the game"""
    def __init__(self, word_list):
        self.word_list = word_list
        #setting attribute to get random word for unique word
        self.word = self.__get_random_word

    @property
    def __get_random_word(self):
        """
        Choice word in random in liste passed as
        class parameter and make sure that random word
        have word with less than 8 letters
        """
        random_word = random.choice(self.word_list)
        while len(random_word) > 8:
            random_word = random.choice(self.word_list)
        return random_word


    @property
    def split_word_shuffle(self):
        """mix letter of word(from get_random_word) randomly"""
        word = self.word
        word_in_list = list(word)
        random.shuffle(word_in_list)
        return word_in_list



liste = ["Diable", "Enfer", "Carma", "Retour", "arivaterebsddazdazda", "jhkqsldhjsqd", "hgkjsqdhjqldqsdk"]

def main():

    word = GenerateWord(liste)
    print(word.word)
    print(word.split_word_shuffle)



if __name__ == '__main__':
    main()
