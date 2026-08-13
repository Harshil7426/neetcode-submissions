class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        for word in strs:
            key=[0]*26
            for i in word:
                key[ord(i)-97]+=1
            key=tuple(key)
            map[key].append(word)
        return list(map.values())

