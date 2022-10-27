houses = [
    ['#','#','#','.','.','.','&','&','.','.','+','.'],
    ['#','#','#','.','=','.','&','&','.','.','+','.'],
    ['#','#','#','.','.','.','.','.','.','.','+','.'],
    ['.','.','.','.','.','&','&','&','.','.','.','.'],
    ['&','&','&','.','.','.','.','.','.','.','=','='],
    ['&','&','&','.','.','.','#','#','#','#','.','.']
]


def find_houses(surf):
    N = len(surf)
    M = len(surf[0])
    result = {}

    for i in range(0, N):
        for j in range(0, M):
            current = surf[i][j]
            if current != '.':
                if result.get(current) == None:
                    result.setdefault(current, 1)
                else:
                    result[current] += 1
                surf = clear_house(surf, i, j)

    return result


def clear_house(surf, i0, j0):
    N = len(surf)
    M = len(surf[0])

    for i in range(i0, N):
        if surf[i][j0] == '.':
            break
        for j in range(j0, M):
            if surf[i][j] == '.':
                break
            surf[i][j] = '.'
    
    return surf


print(find_houses(houses))