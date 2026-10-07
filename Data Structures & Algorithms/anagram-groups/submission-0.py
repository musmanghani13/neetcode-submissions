class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagrams: list = []
        h_map: dict[str, list] = {}
        for current_str in strs:
            sorted_current_string = "".join(sorted(current_str))
            if sorted_current_string in h_map:
                h_map[sorted_current_string].append(current_str)
            else:
                h_map[sorted_current_string] = [current_str]

        for strs in h_map.values():
            anagrams.append(strs)

        return anagrams
