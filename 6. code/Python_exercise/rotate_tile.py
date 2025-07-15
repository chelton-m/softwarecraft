def solution(A):
    count = [1, 0, 1, 2]
    tile = list(A[0])
    
    for i in range(1, len(A)):
        a = list(A[i])
        for j in range(4):
            if tile[j] == a[0]:
                tile[j] = a[2]
                count[j] += 1
            elif tile[j] == a[1]:
                tile[j] = a[3]
                count[j] += 2
            elif tile[j] == a[2]:
                tile[j] = a[0]
                count[j] += 1
            elif tile[j] == a[3]:
                tile[j] = a[1]
        print(tile)
    return count, min(count)


tiles = ['GBRW', 'WRGB', 'GBRW']
print(solution(tiles))

"""
Example test:   ['WBGR', 'WBGR', 'WRGB', 'WRGB', 'RBGW']
WRONG ANSWER (got 5 expected 4)

Example test:   ['RBGW', 'GBRW', 'RWGB', 'GBRW']
WRONG ANSWER (got 6 expected 2)

Example test:   ['GBRW', 'RBGW', 'BWGR', 'BRGW']
WRONG ANSWER (got 6 expected 2)
"""
