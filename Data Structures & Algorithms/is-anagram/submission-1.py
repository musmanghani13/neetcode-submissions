class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_map_s1: dict = {}
        h_map_s2: dict = {}

        def fill_map(h_map, s) -> dict:
            for character in s:
                if character in h_map:
                    h_map[character] = h_map[character] + 1
                else:
                    h_map[character] = 1
            return h_map

        h_map_s1 = fill_map(h_map=h_map_s1, s=s)
        h_map_s2 = fill_map(h_map=h_map_s2, s=t)

        return h_map_s1 == h_map_s2

