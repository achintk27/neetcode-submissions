class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}  #create empty hashmap

        for word in strs:
            key = "".join(sorted(word)) #key is sorted str together , i.e : eat = "aet"

            if key not in group :
                group[key]= [] # crete empty key , groups will be {aet : []}
            group[key].append(word) # saves it as {aet : eat}
            
        return list(group.values())

        