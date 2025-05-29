import math
from typing import List, Tuple

class ClosestPair:
    @staticmethod
    def FindClosestPair(points: list[Tuple[float, float]]) -> List[Tuple[float, float]]:
        p1,p2 = 0, 1
        shortestDistance = ClosestPair.Distance(points[p1][0], points[p1][1],
                                               points[p2][0], points[p2][1])
        for row in range(len(points)):
            for column in range(row + 1, len(points)):
                distance = ClosestPair.Distance(points[row][0], points[row][1],
                                               points[column][0], points[column][1])
                if shortestDistance > distance:
                    p1, p2 = row, column
                    shortestDistance = distance

        return [points[p1], points[p2]]
    
    @staticmethod
    def Distance(x1: float, y1: float, x2: float, y2: float):
        return math.sqrt((x2 -x1) ** 2) + (y2 -y1) ** 2