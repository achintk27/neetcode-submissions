class TimeMap:

    def __init__(self):
        #create an emtpy directory 
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if there is no key assigned , leave empty
        if key not in self.store :
            self.store[key] = []
        
        #if key is there , append the timestamp and vale 
        self.store[key].append((timestamp, value))

        
    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store :
            return ""
        
        #if key is there 
        values = self.store[key]
        left = 0 
        right = len(values) - 1
        answer= ""

        while left <= right :
            middle = (left + right) // 2 
            middle_time , middle_value = values[middle]

            if middle_time <= timestamp :
                #look of timestamp 
                answer = middle_value
                left = middle + 1 
            
            #look for earlier timestamp
            else:
                right = middle - 1

        return answer
        
