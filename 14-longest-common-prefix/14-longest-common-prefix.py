class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ''
        # seperate each word into lists of letters
        letter_strings = []
        for i, word in enumerate(strs):
          letters = [x for x in word]
          letter_strings.append(letters)

        zipped = list(zip(*letter_strings))

        print(zipped)
        for z in zipped:
          if len(set(z)) == 1:
            output += z[0]
          else:
            break

        return output
        