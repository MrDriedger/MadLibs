#make some space before and after the title
story = "\n\n  -- And the Oscar goes to... --  \n"

#add to the story
story = story + "My friends and I are really into movies, so every year we have a party where we eat "

#stop and ask the user for some input
print("Enter a food:")
food = input()
#add the user's input to the story
story = story + food
story = story + " and watch the Oscars together. This year's ceremony was full of surprises. On the red carpet, the photographers swarmed "

#keep on repeating the cycle of asking the user for input and adding it to the story
print("Enter a famous actor:")
actor = input()
story = story + actor
story = story + " whose date to the ceremony was "

print("Enter a famous singer:")
singer = input()
story = story + singer
story = story + " who wore a very revealing dress made of "

print("Enter a material:")
material = input()
story = story + material
story = story + ". Then of course we all heard about when "

print("Enter a celebrity:")
celebrity = input()
story = story + celebrity
story = story + " slapped "

print("Enter another celebrity:")
celebrity = input()
story = story + celebrity
story = story + " after a particularly mean joke. The real shocker was when the Award for Best Picture went to "

print("Enter a color (capitalized):")
color = input()
story = story + color
story = story + " Panther, but they realized the envelopes got mixed up and it actually should have gone to Spiderman: Far From "

print("Enter a place:")
place = input()
story = story + place
story = story + "."

#finally, after all the input has been gathered, output the completed story to the user
print (story)