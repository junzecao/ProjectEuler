# Enter your code here. Read input from STDIN. Print output to STDOUT

# Every 2000 years there are (2000/4)*(365*3+366*1) - 15 = 730485 days, which is divisible by 7

month_day = [None,3,0,3,2,3,2,3,3,2,3,2,3]

def is_leap_year(n):
    if n%4 != 0 or (n%100 == 0 and n%400 != 0):
        return False
    return True

sunday_history = []
def populate_sunday_history():
    year = 1900
    month = 4
    days_remaining = 0
    while year < 3900:
        if days_remaining == 0:
            sunday_history.append([year,month])
        if month == 2 and is_leap_year(year):
            days_remaining += 1
        else:
            days_remaining += month_day[month]
        days_remaining %= 7
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

def counting_sundays(start_date,end_date):
    start_date[0] -= 1900
    start_date[0] %= 2000
    start_date[0] += 1900
    end_date[0] -= 1900
    end_date[0] %= 2000
    end_date[0] += 1900
    if start_date[2] != 1:
        if start_date[1] == 12:
            start_date[1] = 1
            start_date[0] += 1
        else:
            start_date[1] += 1
    count = 0
    if start_date[0] < end_date[0] or (start_date[0] == end_date[0] and start_date[1] <= end_date[1]):
        for i in sunday_history:
            if (start_date[0] < i[0] or (start_date[0] == i[0] and start_date[1] <= i[1])) and (i[0] < end_date[0] or (i[0] == end_date[0] and i[1] <= end_date[1])):
                count += 1
    else:
        for i in sunday_history:
            if (i[0] < end_date[0] or (i[0] == end_date[0] and i[1] <=end_date[1])) or (start_date[0] < i[0] or (start_date[0] == i[0] and start_date[1] <= i[1])):
                count += 1
    return count

populate_sunday_history()
t = int(raw_input().strip())
for a0 in xrange(t):
    start_date = map(int,raw_input().strip().split(' '))
    end_date = map(int,raw_input().strip().split(' '))
    print counting_sundays(start_date,end_date)
