class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            count = [0] * 26
            for i in s:
                index = ord(i) - ord('a')
                count[index] += 1
            key = tuple(count)

            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]
        return list(result.values())
        