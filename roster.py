import pandas as pd
import random

# import roster csv
df = pd.DataFrame.from_csv("roster.csv")

# convert dataframe to dictionary
dictionary = df.to_dict()
dictionary = dictionary["Committee"]


def pair(dictionary):
	# function that randomly pairs people in different committees
	pairings = {}
	while dictionary:

		# obtain random name, committee pair and delete it from dictionary
	    name = random.choice(list(dictionary.keys()))
	    committee = dictionary[name]
	    del dictionary[name]

	    # obtain another random name, committee pair
	    pair_name = random.choice(list(dictionary.keys()))
	    pair_committee = dictionary[pair_name]

	    # check that the committees do not match
	    while pair_committee == committee:
	        pair_name = random.choice(list(dictionary.keys()))
	        pair_committee = dictionary[pair_name]

	    # format names to include committee (to make sure that pairs aren't in same committee)
	    new_name = name + " ({})".format(committee)
	    new_pair_name = pair_name + " ({})".format(pair_committee)

	    # add this pair to the pairings dictionary
	    pairings[new_name] = new_pair_name

	    # delete the second random name
	    del dictionary[pair_name]

	return pairings

def read(dictionary):
	# functions that prints out pairings in an easier to read way
	for i in dictionary:
		print(i, ": ", dictionary[i], "\n")

def main():
	pairs = pair(dictionary.copy())
	read(pairs)

if __name__ == '__main__':
	main()


