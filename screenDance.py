# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 

totalL = 10
for i1 in range(totalL):
    # print out some text 
    print('\n') 
    for i2 in range(totalL):
        if i1 == i2:
            print("*",end="")
        else:
            print("-",end="")
    print('\n',i1,i2) 
    # sleep for 2 seconds after printing output 
    sleep(1) 

    # now call function we defined above 
    clear() 
