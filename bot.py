import os
import time
import win32api, win32con
from PIL import ImageOps
from PIL import ImageGrab
from numpy import *

x = 188
y = 220
def screenGrab():
    im = ImageGrab.grab((x,y, x+640, y+480))
    im.save(os.getcwd() + "\\full_snap_" + str(int(time.time())) + ".png", "PNG")
    return im



############ Mouse Controls  ##############

def leftclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('Left down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def mousePos(cord):
    win32api.SetCursorPos((cord[0],cord[1]))

def get_cords():
    x,y =win32api.GetCursorPos()
    print(x,y)



############ Navigate Through Start Menu###############

def StartGame():
    #click on play button
    mousePos((503,421))
    leftclick()
    time.sleep(1)

     #click on Continue button
    mousePos((511,607))
    leftclick()
    time.sleep(1)

     #click on skip button
    mousePos((769,668))
    leftclick()
    time.sleep(1)

     #click on again continue button
    mousePos((501,594))
    leftclick()
    time.sleep(1)


############ Cordinate class  #############

class Cord:
    f_rice=(276,552)
    f_nori=(221,603)
    f_roe=(280,601)

    foldMat=(387,600)

    phone=(746,575)

    menu_toppings=(706,491)
    t_nori=(685,502)
    t_roe=(764,502)
    t_exit=(783,555)

    menu_rice=(710,512)
    buy_rice=(728,503)

    delivery_norm=(679,513)


############ Keeping track of ingredients #############

foodOnHand={'rice':10,'nori':10,'roe':10}

############ Making Sushi ###################
def makeFood(food):
    if food== 'caliroll':
        print('making a caliroll')
        foodOnHand['rice']=1
        foodOnHand['nori']=1
        foodOnHand['roe']=1
        mousePos(Cord.f_rice)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.foldMat)
        leftclick()
        time.sleep(1.5)

    elif food=='onigiri':
        print('making a onigiri')
        foodOnHand['rice']=2
        foodOnHand['nori']=1
        mousePos(Cord.f_rice)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.f_rice)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.foldMat)
        leftclick()
        time.sleep(1.5)

    elif food=='gunkan':
        print('Making a gunkan')
        foodOnHand['rice']=1
        foodOnHand['nori']=1
        foodOnHand['roe']=2
        mousePos(Cord.f_rice)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.f_roe)
        leftclick()
        time.sleep(.1)
        mousePos(Cord.foldMat)
        leftclick()
        time.sleep(1.5)


############ Buy Food /Navigating Phone Menu ##########
def buyFood(food):
    if food=='rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftclick()
        mousePos(Cord.menu_rice)
        time.sleep(.1)
        leftclick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.buy_rice[0]-x,Cord.buy_rice[1]-y))!=(204,172,89):
            print('rice is available')
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftclick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice']+=10
            time.sleep(.1)
            leftclick()
            time.sleep(2.5)
        else:
            print('rice is Not available')
            mousePos(Cord.t_exit)
            leftclick()
            time.sleep(1)
            buyFood(food)

    if food=='nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftclick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftclick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.t_nori[0]-x,Cord.t_nori[1]-y))!=(33,30,11):
            print('nori is available')
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftclick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori']+=10
            time.sleep(.1)
            leftclick()
            time.sleep(2.5)
        else:
            print('nori is Not available')
            mousePos(Cord.t_exit)
            leftclick()
            time.sleep(1)
            buyFood(food)

    if food=='roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftclick()
        mousePos(Cord.menu_toppings)
        time.sleep(.1)
        leftclick()
        s = screenGrab()
        print('test')
        time.sleep(.1)
        if s.getpixel((Cord.t_roe[0]-x,Cord.t_roe[1]-y))!=(127,61,0):
            print('roe is available')
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftclick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe']+=10
            time.sleep(.1)
            leftclick()
            time.sleep(2.5)
        else:
            print('roe is Not available')
            mousePos(Cord.t_exit)
            leftclick()
            time.sleep(1)
            buyFood(food)

###############################################  Clearing the Tables  ########################################


def clear_tables():
    mousePos((266,428))
    leftclick()

    mousePos((362,428))
    leftclick()

    mousePos((466,428))
    leftclick()

    mousePos((572,428))
    leftclick()

    mousePos((673,426))
    leftclick()

    mousePos((773,429))
    leftclick()
    time.sleep(1)



############################## settings New Bounding Boxes  ######################################################
    
def get_seat_one():
    box = (233,278,257,295)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd()+'\\seat_one__'+str(int(time.time()))+'.png', "PNG")
    return a

def get_seat_two():
    box = (333,278,357,295)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd()+'\\seat_two__'+str(int(time.time()))+'.png', "PNG")
    return a

def get_seat_three():
    box = (433,278,457,295)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd()+'\\seat_three__'+str(int(time.time()))+'.png', "PNG")
    return a

def get_seat_four():
    box = (533,278,557,295)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd()+'\\seat_four__'+str(int(time.time()))+'.png', "PNG")
    return a

def get_seat_five():
    box = (633,278,657,295)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd()+'\\seat_five__'+str(int(time.time()))+'.png', "PNG")
    return a

def get_seat_six():
    box = (733,278,757,295)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd()+'\\seat_six__'+str(int(time.time()))+'.png', "PNG")
    return a


#########################  Sushi types Dictionary #############################

sushiTypes = {1244:'onigiri',2015:'caliroll',1378:'gunkan',}

########################### Checking Food Hand  ########################

def checkFood():
    for i,j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j<=4:
                print('%s is low and needs to be replenished' %i)
                buyFood(i)


#####################Putting It All Together  ########## Final Flow  ###########
#Check seats>if customer,make order>check food>if low,
#buy food>clear tables>repeat.
def check_customers():
    s1 = get_seat_one()
    if s1 in sushiTypes:
        print('table 1 is occupied and needs %s' %sushiTypes[s1])
        makeFood(sushiTypes[s1])
    else:
        print('sushi not found\n sushiType = %i' %s1)

    s2 = get_seat_two()
    if s2 in sushiTypes:
        print('table 2 is occupied and needs %s' %sushiTypes[s2])
        makeFood(sushiTypes[s2])
    else:
        print('sushi not found\n sushiType = %i' %s2)

    s3 = get_seat_three()
    if s3 in sushiTypes:
        print('table 3 is occupied and needs %s' %sushiTypes[s3])
        makeFood(sushiTypes[s3])
    else:
        print('sushi not found\n sushiType = %i' %s3)

    s4 = get_seat_four()
    if s4 in sushiTypes:
        print('table 4 is occupied and needs %s' %sushiTypes[s4])
        makeFood(sushiTypes[s4])
    else:
        print('sushi not found\n sushiType = %i' %s4)

    s5 = get_seat_five()
    if s5 in sushiTypes:
        print('table 5 is occupied and needs %s' %sushiTypes[s5])
        makeFood(sushiTypes[s5])
    else:
        print('sushi not found\n sushiType = %i' %s5)

    s6 = get_seat_six()
    if s6 in sushiTypes:
        print('table 6 is occupied and needs %s' %sushiTypes[s6])
        makeFood(sushiTypes[s6])
    else:
        print('sushi not found\n sushiType = %i' %s6)

    clear_tables()
    checkFood()



##################################################################### MAIN FUNCTION  #######################################

def main():
    StartGame()
    while True:
        check_customers()
                        
