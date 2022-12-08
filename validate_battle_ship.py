def getShipCells(ship):
    res = []
    startCell, endCell = ship
    x1, y1 = startCell
    x2, y2 = endCell
    if x1 == x2:
        biggerY, smallerY = [y1, y2] if y1 > y2 else [y2, y1]
        for y in range(smallerY, biggerY + 1):
            res.append([x1, y])
    else:
        biggerX, smallerX = [x1, x2] if x1 > x2 else [x2, x1]
        for x in range(smallerX, biggerX + 1):
            res.append([x, y1])
    return res


def checkBattleGround(ships):
    allShipWithAllCells = list(map(getShipCells, ships))
    allShipsOnBattle = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for index, mainShip in enumerate(allShipWithAllCells):
        if len(mainShip) not in allShipsOnBattle.keys():
            return False
        allShipsOnBattle[len(mainShip)] += 1
        for checkShip in allShipWithAllCells[:index] + allShipWithAllCells[index+1:]:
            for cellInMainShip in mainShip:
                for cellInCheckShip in checkShip:
                    x1, y1 = cellInMainShip
                    x2, y2 = cellInCheckShip
                    if x1 == x2 and y1 == y2:
                        return False
                    if x1 - 1 <= x2 <= x1 + 1 and y1-1 <= y2 <= y1+1:
                        return False
    if allShipsOnBattle[1] != 4 or allShipsOnBattle[2] != 3 or allShipsOnBattle[3] != 2 or allShipsOnBattle[4] != 1 or allShipsOnBattle[5] != 1:
        return False
    return True


print(checkBattleGround([
    [[1, 1], [1, 1]],
    [[1, 3], [1, 3]],
    [[1, 5], [1, 5]],
    [[1, 7], [1, 7]],
    [[1, 10], [2, 10]],
    [[4, 10], [5, 10]],
    [[7, 10], [8, 10]],
    [[10, 10], [10, 8]],
    [[10, 6], [10, 4]],
    [[10, 1], [7, 1]],
    [[3, 3], [3, 7]]
    # [[1, 3], [1, 7]] # False
]))
