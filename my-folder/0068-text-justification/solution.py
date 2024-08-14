class Solution(object):
    def fullJustify(self, words, maxWidth):
        
        output = []
        width = 0
        storage = []
        string = ""
        
        i = 0
        while i <= len(words):
            print(string)
            if i == len(words):# Last row
                x = maxWidth - len(string)
                for i in range(x):
                    string += " "
                output += [string]
                break

            elif width == 0:
                string += words[i]
                width += len(words[i])
            else:

                if width + len(words[i]) + 1 <= maxWidth:
                    string += " " + words[i]
                    width += len(words[i]) + 1
                else:
                    x = maxWidth - len(string)
                    storage = string.split()
                    if len(storage) == 1:
                        string = storage[0] + " " * x                
    
                    else:
                        string = string.replace(" ", "")
                        x = maxWidth - len(string) #TOTAL SPACES LEFT
                        string = ""

                        y = x / (len(storage) - 1) #SPACES SPLIT BETWEEN WORDS
                        z = x % (len(storage) - 1) # Left overs
                        print(x, storage)
                        print(x, len(storage) - 1, z)
                        for k in range(len(storage)): #goes through the words in storage
                            string += storage[k] #adds it to the string

                            if k != len(storage) - 1: #if the word is not the last word in storage
                                if z != 0:
                                    string += " "
                                    z -=1
                                    x -= 1
                                for p in range(y): #add padding
                                    string += " "
                                    x -= 1 #remove from total spaces left
                    output += [string]
                    string = ""
                    width = 0
                    continue

            i += 1

        return output
                       
                            
                        


                        

