#cells = [3, 0, 6, 2, 10]
cells = [1,2,3]
for count, cell in enumerate(cells):
    if cell > count + 1: 
        cells.remove(cell)
    else: 
        cells.clear()
        
print(cells)