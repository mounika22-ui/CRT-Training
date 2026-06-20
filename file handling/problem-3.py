'''
Word frequency analyzer
A company wants to analyze the text
write a python program:
1.read contents from data.txt
2.count the frequency of each word
3.display most repeated word
4.handle the exceptions 
'''
class WordAnalyzer:
    def analyzer(self):
        try:
            with open("first.txt", "r") as file:
                content=file.read().lower()
            words=content.split()
            frequency = {}
            for word in words:
                if word in frequency:
                    frequency[word]+=1
                else:
                    frequency[word]=1
                print("Word Frequencies:")
            for key, value in frequency.items():
                print(key, ":",value)
            maximum= max(frequency, key=frequency.get)
            print("Most Repeated Word:", maximum)
        except FileNotFoundError as e:
            print("FileNotFoundError")
obj = WordAnalyzer()
obj.analyzer()        