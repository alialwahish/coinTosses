import random
def throwin():
    ran=random.randint(0,1)
    if ran == 1:
        
        return "head"
    else:
        
        return"tail"

heads=0
tails=0
i=0
print("Starting the program")
for i in range(0,5000):
    result=throwin()
    if result =='head':
        heads+=1
    else:
        tails+=1
    print "Attemp #",i,"Throwing a coin...",result,"... Got",heads,"head(s) so far and",tails,"tail(s) so far"
    i+=1
print("End program")