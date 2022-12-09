def transformTimeToNum(time: str) -> int:
    hours, minutes = list(map(lambda x: int(x), time.split(':')))
    return hours * 60 + minutes


def transformNumToTime(num: int) -> str:
    hours = num // 60
    minutes = str(num % 60) if len(str(num % 60)) == 2 else f'0{str(num % 60)}'
    return f'{hours}:{minutes}'


def findFreeTimeFrame(*personsCalendar):
    res = [[transformTimeToNum('8:00'), transformTimeToNum('18:00')]]
    for meets in personsCalendar:
        for startTime, endTime in meets:
            startTime = transformTimeToNum(startTime)
            endTime = transformTimeToNum(endTime)
            resAdd = []
            resDel = []
            for index, freeTime in enumerate(res):
                freeStartTime, freeEndTime = freeTime
                if startTime <= freeStartTime <= endTime and startTime <= freeEndTime <= endTime:
                    resDel.append(index)
                elif freeStartTime < startTime < freeEndTime and freeStartTime < endTime < freeEndTime:
                    resAdd = resAdd + \
                        [[freeStartTime, startTime], [endTime, freeEndTime]]
                    resDel.append(index)
                elif freeStartTime < startTime < freeEndTime or freeStartTime < endTime < freeEndTime:
                    if freeStartTime < startTime < freeEndTime:
                        res[index] = [freeStartTime, startTime]
                    else:
                        res[index] = [endTime, freeEndTime]
                else:
                    continue
            for i in resDel:
                del res[i]
            res = res + resAdd
    return list(map(lambda x: [transformNumToTime(x[0]), transformNumToTime(x[1])], res))


print(findFreeTimeFrame(
    [['8:30', '10:00'], ['15:00', '17:00']],
    [['9:00', '10:00'], ['15:00', '17:00']],
    [['10:00', '10:30'], ['15:00', '17:00']]
))
