import pandas as pd
import random

df = pd.DataFrame.from_csv("roster.csv")

dictionary = df.to_dict()
dictionary = dictionary["Committee"]


def pair(dictionary):
	pairings = {}
	while dictionary:
	    name = random.choice(list(dictionary.keys()))
	    committee = dictionary[name]
	    del dictionary[name]
	    pair_name = random.choice(list(dictionary.keys()))
	    pair_committee = dictionary[pair_name]
	    while pair_committee == committee:
	        pair_name = random.choice(list(dictionary.keys()))
	        pair_committee = dictionary[pair_name]
	    new_name = name + " ({})".format(committee)
	    new_pair_name = pair_name + " ({})".format(pair_committee)
	    pairings[new_name] = new_pair_name
	    del dictionary[pair_name]
	return pairings

def main():
	pairs = pair(dictionary.copy())
	print(pairs)

if __name__ == '__main__':
	main()