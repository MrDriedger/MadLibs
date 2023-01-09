#import modules
import random

madLibs = [
    {
        "quote": "The information superhighway showed the average person what some nerd thinks about Star Trek.",
        "oldWords": ["Star Trek"],
        "wordTypes": ["a noun (plural or uncountable)"]
    },
     {
        "quote": "To alcohol! The cause of … and solution to … all of life's problems.",
        "oldWords": ["alcohol"],
        "wordTypes": ["a noun (plural or uncountable)"]
    },
     {
        "quote": "I can't even say the word 'titmouse' without giggling like a schoolgirl.",
        "oldWords": ["titmouse", "schoolgirl"],
        "wordTypes": ["a silly word", "a person"]
    },
     {
        "quote": "Now Bart, since you broke Grandpa's teeth, he gets to break yours.",
        "oldWords": ["teeth"],
        "wordTypes": ["a body part"]
    },
     {
        "quote": "I've gone back in time to when dinosaurs weren't just confined to zoos!",
        "oldWords": ["zoos"],
        "wordTypes": ["a place (plural)"]
    },
     {
        "quote": "I'm not normally a praying man, but if you're up there, please save me, Superman!",
        "oldWords": ["Superman"],
        "wordTypes": ["a fictional charater"]
    },
     {
        "quote": "I saw this movie about a bus that had to speed around a city, keeping its speed over fifty, and if the speed of the bus dropped, it would explode! I think it was called 'The Bus That Couldn't Slow Down'.",
        "oldWords": ["bus", "The Bus That Couldn't Slow Down"],
        "wordTypes": ["a vehicle", "a film name"]
    },
     {
        "quote": "You couldn't fool your mother on the foolingest day of your life, if you had an electrified fooling machine.",
        "oldWords": ["fool"],
        "wordTypes": ["a verb (present tense, not ending in -ing"]
    },
     {
        "quote": "Weaseling out of things is important to learn; it's what separates us from the animals … except the Weasel.",
        "oldWords": ["Weasel"],
        "wordTypes": ["an animal"]
    },
     {
        "quote": "No TV and no beer makes Homer something something.",
        "oldWords": ["TV", "beer"],
        "wordTypes": ["an enjoyable thing", "an even more enjoyable thing"]
    },
     {
        "quote": "When I first heard that Marge was joining the Police Academy, I thought it would be fun and zany, you know like that movie... 'Spaceballs'. But instead it was dark and disturbing, like that movie 'Police Academy'.",
        "oldWords": ["zany", "Spaceballs", "dark"],
        "wordTypes": ["an adjective", "a film name", "another adjective"]
    },
     {
        "quote": "Dear Lord, the gods have been good to me. As an offering, I present these milk and cookies. If you wish me to eat them instead, please give me no sign whatsoever... thy will be done.",
        "oldWords": ["milk", "cookies"],
        "wordTypes": ["a beverage", "some food (plual)"]
    },
     {
        "quote": "Oh yeah, what are you gonna do? Release the dogs? Or the bees? Or the dogs with bees in their mouths and when they bark, they shoot bees at you?",
        "oldWords": ["dogs", "bees"],
        "wordTypes": ["dangerous animals (plural)", "even more angerous animals (plural)"]
    },
     {
        "quote": "Oh my god, space aliens! Please don't eat me! I have a wife and kids. Eat them!",
        "oldWords": ["wife", "kids"],
        "wordTypes": ["a family member", "people (plural)"]
    },
     {
        "quote": "I am so smart! I am so smart! S- M- R- T- … I mean S M A R T!",
        "oldWords": ["S-", "M-", "R-", "T-"],
        "wordTypes": ["a capital letter", "another capital letter", "yet another capital letter", "one last capital letter"]
    },
]

#randomly choose a quote
chosen = random.randint(0, len(madLibs) - 1)
#chosen = 0
print(chosen)
randomMadlib = madLibs[chosen]
finalQuote = randomMadlib["quote"]

#get user input
count = 0
for thisType in randomMadlib["wordTypes"]:
    print("\n" + "Enter " + "\033[1m" + thisType + "\033[0m" + ":")
    newWord = input()

    #create the final quote
    finalQuote = finalQuote.replace(randomMadlib["oldWords"][count], newWord)
    count = count + 1

#output the final quote
print("\n" + finalQuote + "\n")