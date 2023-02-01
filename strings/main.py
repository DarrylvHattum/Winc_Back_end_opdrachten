# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

playerScored0 = 'Ruud Gullit'
playerScored1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54 
scorers = playerScored0 + ' ' + str (goal_0) + ', ' + playerScored1 + ' ' + str (goal_1)
report = playerScored0 + ' scored in the ' + str (goal_0) + 'nd minute\n' + playerScored1 + ' scored in the ' + str (goal_1) + 'th minute' #\n gebruiken met ''
#print(report)
#part 2


player = 'Jan Wouters'
#print (player .find ('Jan'), player .find (' '))

#first_name: use slicing and the find-method (help(opens in a new tab)) to isolate and store the player's first name.
first_name = player [0:3]
first_name_len = len (first_name)
#print( first_name)

#last_name_len: use find, slicing and len to isolate and store the length of their last name.

last= player .find ('W'), player .find('s') #4 , 10 dus je eindigt met 11 ivm einde zin.
name = player[4:11]
lengte = (len (player [4:11]))
last_name_len = len (player [4:11])

#name_short: isolate and store the player's name in this format:

name1 = player [0:3] #0:1 voor J
short = player [3:11]
name_short = player [0:1] + '.' + player [3:11] #3:11 ivm spatie.

#chant: this is what the crowd chants when it looks like your player is going to score a goal --

chant = ((F"{first_name}! ") *first_name_len) [:-1]


good_chant = chant != '!'

print (good_chant)



