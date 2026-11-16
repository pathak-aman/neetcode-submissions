class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force
        # s1_permute_set = (...)
        # substrings_of_s2_of_length_s1 = (...)
        # Take intersection 
            # If not null -> return True, else return False

        # s1_permute = {abc, acb, bac, bca, cab, cba} -> O(n!)
        # s2_sub = {lec,eca,cab,abe,bee} -> O(n-k+1)
        # TC: O(n!)


        # Better:
        # Compare frequency
        # s1_freq = counter()
            # freq_s2_substring_of_length_s1 = {}

        if len(s1) > len(s2):
            return False

        k = len(s1)
        s1_freq = [0 for i in range(26)]
        for i in s1:
            s1_freq[ord(i) - 97] += 1
        substring_freq = [0 for i in range(26)]
        l = 0
        r = k-1

        
        for i in range(k):
            substring_freq[ord(s2[i]) - 97] += 1

        while r < len(s2):
            print(r, substring_freq)
            if s1_freq == substring_freq:
                return True
            
            # Slide:
            substring_freq[ord(s2[l]) - 97] -= 1
            l += 1
            r += 1
            if r < len(s2):
                substring_freq[ord(s2[r]) - 97] += 1
            
        
        return False

            


