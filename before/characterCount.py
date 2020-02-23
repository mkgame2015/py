import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for chartater in message :
    count.setdefault(chartater,0)
    count[chartater] = count[chartater] + 1
pprint.pprint(count)