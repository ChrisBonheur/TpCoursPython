import pickle

def save_on_file(player_list):
    """This function write or save information on file player"""
    try:
        with open('data/player', 'wb') as file:
            nom_pickler = pickle.Pickler(file)
            nom_pickler.dump(player_list)
    except KeyError as error:
        print("Warning inexist KEY :", error)
    else:
        print("Save on file !")

def get_on_file():
    """
    this function read in a file player
    and return list players
    """
    try:
        with open('data/player', 'rb') as file:
            nom_pickler = pickle.Unpickler(file)
            players_list = nom_pickler.load()
    except Exception as e:
        raise
    else:
        return players_list

liste = {"antonio": {"score": 8, "trying_chance": 0}, "robert": {"score": 2, "trying_chance": 5}}


def main():
    liste = get_on_file()
    liste["jacque"] = {"score": 8, "trying_chance":3}
    save_on_file(liste)
    print(get_on_file()["antonio"]["score"])


if __name__ == '__main__':
    main()
