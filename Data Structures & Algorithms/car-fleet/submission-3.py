class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars= sorted(zip(position,speed), reverse=True)
        fleet = list()
        for pos, speed in cars:
            time = (target - pos)/speed
            print(time)
            if fleet and time <= fleet[-1]:
                    continue
            fleet.append(time)


        return len(fleet)

