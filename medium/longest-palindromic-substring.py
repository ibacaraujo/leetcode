class Solution:
  def longestPalindrome(self, s: str) -> str:
    largest = ''
    for i in range(0, len(s)):
      start = i - len(largest) - 1
      if start < 0:
        sub_str = s[:i+1]
        inv_sub = sub_str[::-1]
        if sub_str == inv_sub:
          if len(sub_str) > len(largest):
            largest = sub_str
            continue
      else:
        # 2 chars longer than current largest
        sub_str = s[start:i+1]
        inv_sub = sub_str[::-1]
        if sub_str == inv_sub:
          if len(sub_str) > len(largest):
            largest = sub_str
            continue
            
        # 1 char longer than current largest
        sub_str = sub_str[1:]
        inv_sub = sub_str[::-1]
        if sub_str == inv_sub:
          if len(sub_str) > len(largest):
            largest = sub_str
            continue
          
    return largest
