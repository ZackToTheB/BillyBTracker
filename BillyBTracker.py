import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime as dt
import urllib.request
import time

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
        dString = str(d.hour)
        if len(str(int((float((d.minute)/60)*100)))) == 1:
            dString += "0"+str(int((float((d.minute)/60)*100)))
        else:
            dString += str(int((float((d.minute)/60)*100)))

    else:
        dString = str(d.hour)+":"  
        if len(str(d.minute)) == 1:
            dString += "0"+str(d.minute)
        else:
            dString += str(d.minute)
            
    return dString
    
xdata = []
ydata = []
plt.show()
plt.figure(num="Spaces Available in the Billy B")
axes = plt.gca()
axes.set_xlim(int(get_time(1)), 2400)
axes.set_ylim(0, 2000)
line, = axes.plot(xdata, ydata, "r-")

run = True

while run:
    try:
        print("{}: {}".format(get_time(), get_num()))
         
        xdata.append(int(get_time(1)))
        ydata.append(int(get_num()))
        line.set_xdata(xdata)
        line.set_ydata(ydata)
        plt.pause(0.1)
        
        if get_time() == "23:59":
            run = False
        
    except Exception as e:
        print("Error: {}".format(e))
    
    for i in range(12):
        time.sleep(5)
    
        




