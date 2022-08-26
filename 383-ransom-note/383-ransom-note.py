class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)
        for l in list(ransomNote):
          if l in list(magazine):
            magazine.remove(l)
          else:
            return False
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        