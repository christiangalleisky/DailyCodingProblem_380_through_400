class CharacterFrequency:

    def __init__(self):
        self.sentence = ""
        self.char_blocks = []
        self.charLink = ""
        self.sortedSentence = ""
        self.frequencyList= []

    def collect_Sentence(self):
        print("Enter a sentence!")
        self.sentence = input()

    def make_array_of_chars(self):
        self.char_blocks = self.sentence.split()

    def make_char_link(self):
        for x in self.char_blocks:
            self.charLink += x

    def sort_char_link(self):
        self.sortedSentence = ''.join(sorted(self.charLink))
        print("Semi-sorted sentence = " + self.sortedSentence)

    def build_character_frequency_list(self):
        i = 0
        while True:
            x = self.sortedSentence[i]
            count = self.sortedSentence.count(x)
            self.frequencyList.append([count, x])
            i += count
            if i >= len(self.sortedSentence):
                break;
        self.frequencyList = sorted(self.frequencyList)
        print(self.frequencyList)

    def build_Final_String(self):
        s = ""
        for x, y in self.frequencyList:
            while x > 0:
                s += y
                x -= 1
        s = s[::-1]
        print(s)

obj = CharacterFrequency()
obj.collect_Sentence()
obj.make_array_of_chars()
obj.make_char_link()
obj.sort_char_link()
obj.build_character_frequency_list()
obj.build_Final_String()
