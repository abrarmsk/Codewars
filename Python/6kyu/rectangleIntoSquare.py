def sort_sides(lng, wdth):
    return sorted([lng, wdth])

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    small, large = sort_sides(lng, wdth)
    squares =[]
    while small > 0:
        squares.append(small)
        new_side = large - small
        small, large = sort_sides(new_side, small)
        return squares
