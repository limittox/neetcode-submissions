class TimeMap:

    def __init__(self):
        self.masterKey = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.masterKey:
            self.masterKey[key] = {timestamp: value}
        else:
            self.masterKey[key][timestamp] = value
        
        # print(self.masterKey)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.masterKey:
            return ""
        timestamps = list(self.masterKey[key].keys())

        # if len(timestamps) == 1:
        #     return self.masterKey[key][timestamp] if timestamp in self.masterKey[key] else ""
        
        l, r = 0, len(timestamps)-1
        mid = -1
        ansIndex = -1

        while l <= r:
            mid = (l+r)//2
            # print(f'{mid=}')
            if timestamps[mid] == timestamp:
                return self.masterKey[key][timestamp]
            
            if timestamps[mid] < timestamp:
                ansIndex = mid
                l = mid + 1
            else:
                r = mid - 1
        # print(f'{mid=}')
        
        if ansIndex == -1:
            return ""
        return self.masterKey[key][timestamps[ansIndex]]
        # return self.masterKey[key][mid] if (mid > 0 and mid < len(timestamps)) else ""


        
"""
dict(dict())

person = dict()
timestamp = dict()

if not person[alice]:
    key_val = dict()
    key_val[1] = happy
    person[alice] = key_val
else:
    person[alice][2] = sad

for get:
    person[alice][2] # sad
"""