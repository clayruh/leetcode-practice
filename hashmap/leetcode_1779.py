class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
# hashmapping the index of a valid point to the Manhattan distance, to eventually find the smallest

# initialize dictionary
        dictionary = {}
        smallest_distance = float("inf")
# loop through points
        for i in range(len(points)):
# if point is valid, aka if either current_x = x or current_y = y
            if x == points[i][0] or y == points[i][1]:
# calculate the Manhattan distance
                manhattan_distance = abs(x - points[i][0]) + abs(y - points[i][1])
                smallest_distance = min(manhattan_distance, smallest_distance)
# then store in dictionary manhattan_distance : [list of indexes]
# if the distance already exists in the dictionary, we need to append index
                if manhattan_distance in dictionary:
                    dictionary[manhattan_distance].append(i)
                else:
                    dictionary[manhattan_distance] = [i]
# and as we're adding indexes, incase of the same manhattan_distances, then we just find the first in that list of indexes
        if smallest_distance == float("inf"):
            return -1
        return dictionary[smallest_distance][0]

# if we've gone through all the points, and no valid points, then return -1

{2: [0,1],
 5: [2],
 3: [3,6],
 8: [4,5]}