class Solution:
    def isAnagram(self, first: str, second: str) -> bool:
        array = [0] * 26

        for letter in first:
            position = (ord(letter) - 97)
            array[position] = array[position] + 1
        
        for letter in second:
            position = (ord(letter) - 97)
            array[position] = array[position] - 1

        return all(x == 0 for x in array)






        
