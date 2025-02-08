class Solution:
  def checkIfPangram(self, sentence:str):
    unique_char = set(sentence.lower())
    if len(unique_char) < 26:
      return False
    return True
  
      
sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
x = Solution()
print(x.checkIfPangram(sentence))