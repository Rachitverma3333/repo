from datetime import datetime
alist = ["rachit", 2515, "verma", "biaora", 564856]
alist.reverse()
print(alist)
print(alist.index("rachit"))



aset = {"rait", 255, 255,  "vera", "biora", 5454}
print(aset)

atuple = ("r", "a", "c", "h","i", "t", 10, 20, 30)
print(atuple)

dtn = {"name" : "rachit", "roll" : 131077, "mob" : 8085456693}
dtn.update({"name" : "bunty", "roll" : 20202020, "mob" : 4646464})
dtn["add"] = "mandi"
print(dtn)
v = dtn.get("add")
print(v)
dt = datetime.today()
print(dt)