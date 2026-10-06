class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_map_s1: dict = {}
        h_map_s2: dict = {}

        for ch in s:
            if ch in h_map_s1:
                h_map_s1[ch] = h_map_s1[ch] + 1
            else:
                h_map_s1[ch] = 1

        for ch in t:
            if ch not in h_map_s1:
                return False

            if ch in h_map_s2:
                h_map_s2[ch] = h_map_s2[ch] + 1
                if h_map_s2[ch] > h_map_s1[ch]:
                    return False
            else:
                h_map_s2[ch] = 1

        return h_map_s1 == h_map_s2

