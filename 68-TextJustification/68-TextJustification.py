# Last updated: 8/12/2026, 12:22:46 PM
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            # Step 1: Greedy pack words into a line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            # Step 2: Build the line
            line_words = words[i:j]
            num_words = j - i
            
            # Last line OR single word → left-justify
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                space_between, extra = divmod(total_spaces, num_words - 1)
                
                line = ""
                for k in range(num_words - 1):
                    line += line_words[k]
                    line += " " * (space_between + (1 if k < extra else 0))
                line += line_words[-1]
            
            res.append(line)
            i = j
        
        return res
