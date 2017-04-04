```python
'''
Huiluo Chen
2143 OOP Programming
April 4 2017
'''

# create a cell class has attribute of row and col number
class cell(object):
    def __init__(self, row=0, col=0):
        #initialize the row and col number for the cell
        self.row = row
        self.col = col

# method to find the manhattan distance
def distance_find(cell1, cell2):
    row_dist = abs(cell1.row - cell2.row)
    col_dist = abs(cell1.col - cell2.col)
    #remove the duplicated cell
    total_dist = row_dist + col_dist - 1
    return total_dist
```
