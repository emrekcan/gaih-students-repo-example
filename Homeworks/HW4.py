import sys

class Hangman:
    searchingWord = ""
    chList = list()

    def __init__(self):
        pass

    def get_word_from_user(self):
        self.searchingWord = input("Write the word to be found \n")
        self.chList = ['_' for i in range(len(self.searchingWord))]


    def checkCharacter(self, guess):
        counter = 0
        for character in self.searchingWord:
            if guess == character:
                self.chList[counter]= character

            counter += 1

    def writeCharacters(self, word_list):
        for character in self.chList:
            print(character, end=" ")
        print()
        
    def isGameOver(self):
        if "_" not in self.chList:
            print("Congratulations. You won!!!")
            sys.exit()

    def start(self):
       for ch in range(len(self.searchingWord)):
           self.isGameOver()
           print("Retries:", len(self.searchingWord)-ch)
           guessed = input("Your guess:")
           self.checkCharacter(guessed)
           self.writeCharacters(self.chList)
       else:
           print("Your Retries is Over")
           sys.exit()

player = Hangman()
player.get_word_from_user()
player.start()
