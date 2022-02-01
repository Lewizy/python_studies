import datetime

x = datetime.datetime.now()
print("today's date is", x,)
print(x.year) #year
print(x.strftime("%A")) #day

# create personal date objects
y = datetime.datetime(1987, 5, 10); print(y) #1987-05-10 00:00:00
print(y.strftime("the dated century is "+"%C")) #19



