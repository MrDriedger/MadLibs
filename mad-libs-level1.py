#make some space before and after the title
story = "\n\n  -- Best Christmas Ever --  \n"

#write out the story in an list, each list contains a pair of strings that will become the given text and the prompt for the type of word that the user has to provide
original = [
    ["Finally, it was the time I had been waiting for all year: Christmas morning! My ", "a number from 0 to 100"],
    [" siblings and I raced down the stairs as excited as can be. Our family tradition was to all gather around a large ", "a plant"],
    [" in our living room that we had decorated with tinsel and lights. My eyes were drawn to a huge ","a shape"],
    ["-shaped gift wrapped in a bow. It had my name on it! And even better, the tag said it was from my hero: ", "a famous person"],
    [". I opened it up, holding my breath in anticipation, and discovered that the gift was a ", "a noun"],
    ["! It's just what I always wanted! I nearly passed out from feeling so ", "an emotion"]
]

#add a closing line after the last wordType
closing = ". Best Christmas ever!"

#set up a loop that will repeat however many times as there are pairs in the original list
for given, wordType in original:
    print("Enter "+wordType+":")
    suggestion = input()
    story = story + str(given) + suggestion
story = story + closing
print(story)