class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = sorted(zip(position, speed), reverse=True)
        maxtime = 0
        fleet = 0
        for pos, sp in s:
            time = (target - pos)/sp
            if time > maxtime:
                fleet += 1
                maxtime = time
        return fleet

