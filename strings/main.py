# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Create a variable for every player that scored, for example:
playerscored0 = 'Ruud Gullit'
playerscored1 = 'Marco van Basten'
#Create a variable for each minute of the match that a goal was scored in, for example:
goal_0 = 32
goal_1 = 54
#Using the +-operator, create a string that reports on who scored when, according to the format:
scorers = playerscored0 + ' ' + str (goal_0) + ', ' +  playerscored1 + ' ' +str (goal_1)
#Use f-strings or the +-operator to create a single string with information about who scored when in the format:
report = (f'{playerscored0} scored in the {goal_0}nd minute\n{playerscored1} scored in the {goal_1}th minute')

# Choose a player that played in the soccer match and store his name as a string in the variable player.
player = 'Wilbert Suvrijn'

#first_name: use slicing and the find-method (help(opens in a new tab)) to isolate and store the player's first name.
first_name = player [0:player.find (' ')]
first_name_len = len(player[0:player.find (" ")])
#print( first_name_len)
#last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_len = len(player[player.find (" ") +1:])
#name_short: isolate and store the player's name in this format:
name_short = first_name[0:1] + '.' + player[7:15]
#chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. Because Gut has 3 letters in his name, we repeat his name 3 times. Make sure the last character of this string is not a space! For our example player:

chant = (F'{first_name}! ' * len(first_name)) [:-1]

#good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). This variable needs to be a boolean, not a string. You can create the value for this variable by comparing the last character of chant with a space character. Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).

good_chant = chant != '!'
print(good_chant)









#print(scorers)
#print(report) 
#print(first_name)
#print(last_name_len)
#print(name_short)
#print(chant)
