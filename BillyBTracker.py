import urllib.request, time
import matplotlib.pyplot as plt
import datetime as dt

def get_num():
    site = urllib.request.urlopen("https://www.dur.ac.uk/library/")
    str_ = str(site.read())
    finding = str_[str_.index("donut-segment"):str_.index("donut-segment")+300].replace(" ", "")
    find = finding[finding.index("#552756\">"):finding.index("#552756\">")+20]

    num = find[find.index(">")+1:find.index("<")].replace(",", "")
    
    return num

def get_time(int_ = 0):
    d = dt.datetime.now()
    if int_:
        dString = str(d.hour)+str(d.minute)
    else:
        dString = str(d.hour)+":"+str(d.minute)
    return dString

def plot(x, y):
    plt.plot(x, y)
    ply.show()
    
xdata = []
ydata = []
plt.show()
axes = plt.gca()
axes.set_xlim(int(get_time(1)), 2400)
axes.set_ylim(0, 1800)
line, = axes.plot(xdata, ydata, 'r-')

while 1:
    print("{}: {}".format(get_time(), get_num()))
     
    xdata.append(int(get_time(1)))
    ydata.append(int(get_num()))
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    plt.pause(0.1)
    
    time.sleep(60)
    
        




