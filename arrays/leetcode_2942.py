class Solution(object):
    def findWordsContaining(self, words, x):
        # look for words in `words` that contain character `x`
        # return an array of indices for those words
        arrayOfWords = []
        for i in range(len(words)):
            if x in words[i]:
                arrayOfWords.append(i)
        # could do list comprehension??
        return arrayOfWords
        # return [i for i in range(len(words)) if x in words[i]]
    
    