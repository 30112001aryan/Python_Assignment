# Python program to combine two dictionary

import itertools
import collections

# initializing two dictionaries
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

Cdict = collections.defaultdict(int)

for key, val in itertools.chain(dict1.items(), dict2.items()):
	Cdict[key] += val
	
print(dict(Cdict))
