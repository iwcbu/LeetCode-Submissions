class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        mag_d = {}

        for ch in magazine:
            if ch in mag_d:
                mag_d[ch] += 1
            else:
                mag_d[ch] = 1
        
        for ch in ransomNote:
            if ch not in mag_d:
                return False
            elif mag_d[ch] == 1:
                del mag_d[ch]
            else:
                mag_d[ch] -= 1
            
        return True
