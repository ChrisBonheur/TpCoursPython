#! /usr/bin/env python3
# coding: utf-8

import pickle
import random


def written_on_file(player_list):
    """This function write or save information on file"""
    with open('data/player', 'wb') as file:
        nom_pickler = pickle.Pickler(file)
        nom_pickler.dump(player_list)

def get_file():
    """
    this function read a wriitten file
    and return list players
    """
    with open('data/player', 'rb') as file:
        nom_pickler = pickle.Unpickler(file)
        players_list = nom_pickler.load()
    return players_list


class Player:
    """
    docstring for Player, create a new player or
    existing player.
    """
    LOSE_CHANCE = 1
    def __init__(self, name, list_players):
        self.name = name
        self.score = 0
        self.trying_chance = 8
        self.player_exist = False
        self.players_list = list_players
        self.player_verification()

    def player_verification(self):
        """Verificate if player name exist"""
        players_list = self.players_list
        for key in players_list.keys():
            if self.name == key:
                self.player_exist = True

    @property
    def boost_score(self):
        """Boost score with number of trying chance"""
        self.score += self.trying_chance

    @property
    def drop_trying_chance(self):
        """Drop trying_chance"""
        self.trying_chance -= self.LOSE_CHANCE

    def initialize_game(self):
        self.score = 0
        self.trying_chance = 8

    def set_score(self):
        if self.player_exist == True:
            self.score = self.players_list[self.name][score]
        return self.score

    def set_trying_chance(self):
        if self.player_exist == True:
            self.trying_chance = self.players_list[self.name][chance_number]
        return self.trying_chance


class GameSystem:
    """GameSystem controle the game"""
    def __init__(self, word_list):
        self.word_list = word_list

    @property
    def get_random_item(self):
        """Get random number"""
        len_list = len(self.word_list)
        random_item = random.randint(0, len_list - 1)
        return random_item

    @property
    def get_random_word(self):
        """
        Choice word in random in liste passed as
        class parameter
        """
        return self.word_list[self.get_random_item]

    def split_word_shuffle(self):
        """mix letter of word(from get_random_word) randomly"""
        word = self.get_random_word
        word_in_list = list(word)
        table_word = []
        for letter in word_in_list:
            table_word.append(letter)
            random.shuffle(table_word)
        return table_word




def main():
    pass

if __name__ == '__main__':
    main()
