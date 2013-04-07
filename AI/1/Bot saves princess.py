#!/bin/python
# Head ends here
def displayPathtoPrincess(m,grid):
    for i in xrange(0, m):
        for j in xrange(0, len(grid[i])):
            if grid[i][j] == 'm':
                n1 = i
                m1 = j
            if grid[i][j] == 'p':
                n2 = i
                m2 = j
    
    if n1 > n2:
        for i in range(n1 - n2):
            print 'UP'
    else:
        for i in range(n2 - n1):
            print 'DOWN'
    
    if m1 > m2:
        for i in range(m1 - m2):
            print 'LEFT'
    else:
        for i in range(m2 - m1):
            print 'RIGHT'
    
    return ""

# Tail starts here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
