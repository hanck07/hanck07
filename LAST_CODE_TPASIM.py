import time
passthrough_data=0x5a


def board____WriteI2C(addr1, reg1, data1) :
    print("**********REG**************"  + str(hex(addr1))+ " , "  +str(hex(reg1))+ " , "  +str(hex(data1)))
    board.WriteI2C(addr1, reg1, data1) 
    time.sleep(0.2)
def select_CSI_port(addr,port,passthrough_data):
    if (port == 1):
        #board____WriteI2C(addr, 0x4C, 0x01)  #enable r/w of port 0
        #time.sleep(0.5)
        #board____WriteI2C(addr, 0x58, 0x08)  #disable back channel of port 0
        #time.sleep(0.5)
        board____WriteI2C(addr, 0x4c, 0x12)  #enable r/w of port 1 registers  
        time.sleep(0.5)
        board____WriteI2C(addr, 0x58, passthrough_data)  #enable back channel of port 1 @ 2.5mbps ???
        time.sleep(0.5)
        fwd_port=0x10
	    print("ENTRE A 1")
          
    if (port == 0):
        #board____WriteI2C(addr, 0x4C, 0x12)  #enable r/w of port 1
        #time.sleep(0.5)
        #board____WriteI2C(addr, 0x58, 0x08)  #disable back channel of port 0
        #time.sleep(0.5)
        
        board____WriteI2C(addr, 0x4c, 0x01)  #enable r/w of port 0 registers  
        time.sleep(0.5)
        board____WriteI2C(addr, 0x58, passthrough_data)  #enable back channel of port 1 @ 2.5mbps ???
        time.sleep(0.5)
        fwd_port=0x20  
	    print"ENTRE A ZERO"
        
    board____WriteI2C(addr, 0x32, 0x01)
    time.sleep(0.5)
    
    board____WriteI2C(addr,0x33,0x21)
  
    board____WriteI2C(addr,0x21,0x14) # Synchronized Basic_FWD
    board____WriteI2C(addr,0x20,fwd_port) 
    
    board____WriteI2C(addr,0x1F,0x02)
    board____WriteI2C(addr,0x6D,0xfc)


_954Port =1
ADAS954 = 0x60
Alias953  = 0x44
TPASIM953 = 0x42
TPASIM954 = 0x7a
passthrough_data=0x5a
cam=0 


i=0
tst=0

select_CSI_port(ADAS954,_954Port,passthrough_data) 
board____WriteI2C(ADAS954,0x5C,TPASIM953)
board____WriteI2C(ADAS954,0x5D,TPASIM954)  
board____WriteI2C(ADAS954,0x65,TPASIM954) 
board____WriteI2C( ADAS954,0x5e,Alias953)
board____WriteI2C( ADAS954,0x66,Alias953) 
time.sleep(0.5)
board____WriteI2C(TPASIM953, 0x01, 0x02)
time.sleep(3)

board____WriteI2C(TPASIM953, 0x32, 0x69)  #was     0a0    or 0x60 ok
board____WriteI2C(TPASIM953, 0x03, 0x5a) #was 0x5a , 0x5b not work
board____WriteI2C(TPASIM953, 0x02, 0x13)#2 CSI-LANE!!!!!!!!
time.sleep(1.0)

select_CSI_port(TPASIM954,cam,passthrough_data)    
board____WriteI2C(TPASIM954,0x5C,Alias953) 
time.sleep(0.5)
board____WriteI2C(Alias953, 0x01, 0x02)
time.sleep(3)

board____WriteI2C(Alias953, 0x32, 0x69)  #was     0a0    or 0x60 ok
board____WriteI2C(Alias953, 0x03, 0x5a) #was 0x5a , 0x5b not work
board____WriteI2C(Alias953, 0x02, 0x13)#2 CSI-LANE!!!!!!!!
time.sleep(1.0)

#def patern2(board,Alias953) :
delayTime=0.2

board____WriteI2C(Alias953, 0xB0, 0x00)

board____WriteI2C(Alias953, 0xB1, 0x01)
board____WriteI2C(Alias953, 0xB2, 0x01) #enable pattern generator
time.sleep(delayTime)


print "953 - fixed color pattern, 8 color bars, block size of 5"
board____WriteI2C(Alias953, 0xB1, 0x02)
board____WriteI2C(Alias953, 0xB2, 0xB1) #fixed color pattern, 8 color bars, block size of 5
time.sleep(delayTime)

print "953 - CSI Data Identifier (0x24 = RGB888, 0x2C = RAW12, 0x2B = RAW10)"
board____WriteI2C(Alias953, 0xB1, 0x03)
board____WriteI2C(Alias953, 0xB2, 0x24) #CSI Data Identifier (0x24 = RGB888, 0x2C = RAW12, 0x2B = RAW10)
time.sleep(delayTime)

print "954 - line size (15:8)"
board____WriteI2C(Alias953, 0xB1, 0x04)
board____WriteI2C(Alias953, 0xB2, 0x0f) #line size (15:8)  
time.sleep(delayTime)

print "953 - line size (7:0)"
board____WriteI2C(Alias953, 0xB1, 0x05)
board____WriteI2C(Alias953, 0xB2, 0x00) #line size (7:0)
time.sleep(delayTime)

print "953 - bar size (15:8)"
board____WriteI2C(Alias953, 0xB1, 0x06)
board____WriteI2C(Alias953, 0xB2, 0x01) #bar size (15:8)
time.sleep(delayTime)

print "953 - bar size (7:0)"
board____WriteI2C(Alias953, 0xB1, 0x07)
board____WriteI2C(Alias953, 0xB2, 0xd0) #bar size (7:0)  
time.sleep(delayTime)

print "953 - active lines per frame (15:8)"
board____WriteI2C(Alias953, 0xB1, 0x08)
board____WriteI2C(Alias953, 0xB2, 0x04) #active lines per frame (15:8)
time.sleep(delayTime)

print "954 - active lines per frame (7:0)"
board____WriteI2C(Alias953, 0xB1, 0x09)
board____WriteI2C(Alias953, 0xB2, 0x38) #active lines per frame (7:0)
time.sleep(delayTime)

print "953 - total lines per frame (15:8)"
board____WriteI2C(Alias953, 0xB1, 0x0a)
board____WriteI2C(Alias953, 0xB2, 0x04) #total lines per frame (15:8)
time.sleep(delayTime)

print "954 - total lines per frame (7:0)"
board____WriteI2C(Alias953, 0xB1, 0x0b)
time.sleep(delayTime)
board____WriteI2C(Alias953, 0xB2, 0x65) #total lines per frame (7:0)
time.sleep(delayTime)

print "954 - line period (15:8)"
board____WriteI2C(Alias953, 0xB1, 0x0c)
time.sleep(delayTime)
board____WriteI2C(Alias953, 0xB2, 0x0B) #line period (15:8)
time.sleep(delayTime)

print "953 - line period (7:0)"
board____WriteI2C(Alias953, 0xB1, 0x0d)
board____WriteI2C(Alias953, 0xB2, 0xF2) #line period (7:0)
time.sleep(delayTime)

print "953 - vertical back porch"
board____WriteI2C(Alias953, 0xB1, 0x0e)
board____WriteI2C(Alias953, 0xB2, 0x01) #vertical back porch
time.sleep(delayTime)

print "953 - vertical front porch"
board____WriteI2C(Alias953, 0xB1, 0x0f)
board____WriteI2C(Alias953, 0xB2, 0x01) #vertical front porch
time.sleep(delayTime)