msg = "Global"

def local():
    global msg
    msg = "Glocal"
    print(msg)

def Ey():
    msg = "Ey ey ey"
    print(msg)
    

local()
Ey()


