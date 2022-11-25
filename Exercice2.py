class MyString:
    def __init__(self,sentence=""):
        self.sentence = sentence
        

    def getSentence(self):
        self.sentence=input("veillez saisi une chaine: ")
        
    
    def printSentence(self):
        print( self.sentence)
p4=MyString()        
p4.getSentence()
p4.printSentence()
print(p4.sentence)

        
        
         