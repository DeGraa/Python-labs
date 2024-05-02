import datetime

x = datetime.datetime(2005, 11, 17)
y = datetime.datetime(2005, 11, 22)

diff = abs(x - y)
print(diff.total_seconds())
