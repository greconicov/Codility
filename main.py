#Python 3

"""""
##########################################################################################################################################################

                                                        Exercise

##########################################################################################################################################################

A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.

##########################################################################################################################################################

                                                    Solution

##########################################################################################################################################################

"""
def solution (X, Y, D= 30):
    OneJump = 1
    distance = Y-X
    howManyJumps= distance/D

    if X > Y:
        return "Your are already in the place!"
    if X and Y not in range (1,1000000000):
        return "Your are not that guy pal, trust me"

    if howManyJumps % OneJump == 0: #you did the jumps that you need for travel from X to Y
        return "The frog must do {0} jumps as min for travel {1} meters".format(round(howManyJumps), distance)
    if howManyJumps % OneJump != 0: # you didn't do the jumps that you need for reaching Y
        return "The frog must do {0} jumps as min for travel {1} meters".format(round(howManyJumps + OneJump), distance) #so you add +OneJump to arrive Y

print(solution(10, 1000))
print(solution(1, 100000000000000000000))
print(solution(20000000, 212192))
print(solution(11, 190))
