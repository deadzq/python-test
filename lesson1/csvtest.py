import csv

# write stocks data as comma-separated values
from filecmp import cmp

writer = csv.writer(open('stocks.csv','wb',buffering=0))
writer.writerows([
    ('YHOO'.encode(),'YaHoo! Inc.'.encode(),27.38,0.33,1.22),
])

# read stocks data, print status messages
stocks = csv.reader(open('stocks.csv','rb'))
status_labels = {-1:'down',0:'unchanged',1:'up'}
for ticker,name,price,change,pct in stocks:
    status = status_labels[cmp(float(change),0.0)]
    print('%s is %s (%s%%)' % (name,status,pct))