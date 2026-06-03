class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resdic = defaultdict(list)
        for s in strs:
            sorteds = "".join(sorted(s))
            resdic[sorteds].append(s)
        return list(resdic.values())
        