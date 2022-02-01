print(bool(1))#true	
print(bool(0))#false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))#returs false

def myBool_func():
	return True
print(myBool_func())

if myBool_func():
	print("print if func returns true")
else:
	print("false")	

isinstance_method_num = 45j
print(isinstance(isinstance_method_num, complex))#true





