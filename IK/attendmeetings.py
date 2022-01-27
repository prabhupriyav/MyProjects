def can_attend_all_meetings(intervals):
 
    if len(intervals) == 1:
        return 1
    for i in range(len(intervals)):
            if (intervals[i][1] <= intervals[i+1][0]):
                return 1
            else:
               return 0
