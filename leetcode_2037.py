def minMovesToSeat(seats, students) -> int:
    # n seats for n students(standing)
    # sort seats + students so that they're both ordered from least to greatest
    # loop through students
    # find the absolute difference between seats + students and add to counter
    seats.sort()
    students.sort()
    moves = 0
    for i in range(len(seats)):
        moves += abs(seats[i] - students[i])
    return moves

print(minMovesToSeat([4,1,5,9], [1,3,2,6]))