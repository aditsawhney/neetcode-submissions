class TimeMap:

    def __init__(self):
        self.time_map = {}
        # we would store tuples (value, timestamp) at our keys
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        values = self.time_map[key]
        result = ""
        left, right = 0, len(values)-1

        while left <= right:
            mid = (left+right)//2
            val, t = values[mid]    # tuple unpacking
            # since we have to return either the exact or closest lower value, so store the lower value in result, as a possible option, and then try to find a closer match on the right side.

            if t <= timestamp:
                result = val
                left = mid+1
            else:
                right = mid-1
        
        return result