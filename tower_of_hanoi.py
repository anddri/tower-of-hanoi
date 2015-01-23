from sys import argv

script, numberOfDisks = argv

def hanoi(nDisks, fromPeg, toPeg):
	helpPeg = 0
	sol1 = ""
	sol2 = ""
	myStep = ""
	mySol = ""

	if (nDisks == 1):
		return str(fromPeg) + " -> " + str(toPeg) + '\n'

	else:
		helpPeg = 6 - fromPeg - toPeg

		sol1 = hanoi(nDisks - 1, fromPeg, helpPeg)

		myStep = str(fromPeg) + " -> " + str(toPeg) + '\n'

		sol2 = hanoi(nDisks - 1, helpPeg, toPeg)

		mySol = sol1 + myStep + sol2

		return mySol

print hanoi(int(numberOfDisks), 1, 3)