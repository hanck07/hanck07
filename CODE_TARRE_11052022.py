import time

#Declaramos la dirección del 953 y 954
D954 = 0x60
D953 = 0x1A
#D953 = 0X18 #Descomentar esta línea para utilizar el RX0
#Definimos el puerto ya sea RX0 o RX1 en la conexión FAKRA DEL 954
P954 = 1





#Generamos un Reset al Dserializer 
board.Write(D954,0x01,0x01)
time.sleep(3)

#Habilitamos la transmisión sobre el puerto seleccionado ???????
board.Write(D954,0x4C,0x12)
time.sleep(0.1)

#Habilitamos la linea de I2C PASS AND 10Mbps BC
board.Write(D954,0x58,0x5A)
time.sleep(0.1)

#CSI ENABLE RELOJ CONTINUO AND 2 DATA LANES
board.Write(D954, 0x33,0x23)
time.sleep(0.1)


board.Write(D954,0xF1,0x02)
time.sleep(0.1)

#HABILITAMOS EL PUERTO RX1 PARA RECIBIR DATOS
board.Write(D954,0x0C,0x92)
time.sleep(0.1)

#SETEAMOS EL FRAME SYNC
board.Write(D954, 0x18, 0x03)
time.sleep(0.1)

#SETEAMOS EL FORDWARING PARA EL PUERTO RX1
board.Write(D954, 0x20, 0x10)
time.sleep(0.1)

#ERROR FLAG FOR DRP-3 LINK ENCODER
board.Write(D954, 0x4A, 0x10)
time.sleep(0.1)

#ENABLE ENCODER
board.Write(D954, 0xBA, 0x83)
time.sleep(0.1)


#SETEAMOS EL SYNC MODE
board.Write(D953, 0x03, 0x48)
time.sleep(0.1)

#BCC CONFIG
board.Write(D953, 0x32, 0x69)
time.sleep(0.1)









print "953 - enable pattern generator"

board.WriteI2C(D953, 0xB0, 0x00)


ed color pattern, 8 color bars, block size of 5"

board.WriteI2C(D953, 0xB1, 0x02)

board.WriteI2C(D953, 0xB2, 0xB1) #fixed color pattern, 8 color bars, block size of 5

time.sleep(0.1)



print "953 - CSI Data Identifier (0x24 = RGB888, 0x2C = RAW12, 0x2B = RAW10)"

board.WriteI2C(D953, 0xB1, 0x03)

board.WriteI2C(D953, 0xB2, 0x24) #CSI Data Identifier (0x24 = RGB888, 0x2C = RAW12, 0x2B = RAW10)

time.sleep(0.1)



board.WriteI2C(D953, 0xB1, 0x01)

board.WriteI2C(D953, 0xB2, 0x01) #enable pattern generator

time.sleep(0.1)





print "953 - fix
print "954 - line size (15:8)"

board.WriteI2C(D953, 0xB1, 0x04)

board.WriteI2C(D953, 0xB2, 0x0F) #line size (15:8)

time.sleep(0.1)



print "953 - line size (7:0)"

board.WriteI2C(D953, 0xB1, 0x05)

board.WriteI2C(D953, 0xB2, 0x00) #line size (7:0)

time.sleep(0.1)



print "953 - bar size (15:8)"

board.WriteI2C(D953, 0xB1, 0x06)

board.WriteI2C(D953, 0xB2, 0x01) #bar size (15:8)

time.sleep(0.1)



print "953 - bar size (7:0)"

board.WriteI2C(D953, 0xB1, 0x07)

board.WriteI2C(D953, 0xB2, 0xD0) #bar size (7:0)

time.sleep(0.1)



print "953 - active lines per frame (15:8)"

board.WriteI2C(D953, 0xB1, 0x08)

board.WriteI2C(D953, 0xB2, 0x04) #active lines per frame (15:8)

time.sleep(0.1)



print "954 - active lines per frame (7:0)"

board.WriteI2C(D953, 0xB1, 0x09)

board.WriteI2C(D953, 0xB2, 0x38) #active lines per frame (7:0)

time.sleep(0.1)



print "953 - total lines per frame (15:8)"

board.WriteI2C(D953, 0xB1, 0x0a)

board.WriteI2C(D953, 0xB2, 0x04) #total lines per frame (15:8)

time.sleep(0.1)



print "954 - total lines per frame (7:0)"

board.WriteI2C(D953, 0xB1, 0x0b)

time.sleep(0.1)

board.WriteI2C(D953, 0xB2, 0x65) #total lines per frame (7:0)

time.sleep(0.1)



print "954 - line period (15:8)"

board.WriteI2C(D953, 0xB1, 0x0c)

time.sleep(0.1)

board.WriteI2C(D953, 0xB2, 0x0B) #line period (15:8)

time.sleep(0.1)



print "953 - line period (7:0)"

board.WriteI2C(D953, 0xB1, 0x0d)

board.WriteI2C(D953, 0xB2, 0xF2) #line period (7:0)

time.sleep(0.1)



print "953 - vertical back porch"

board.WriteI2C(D953, 0xB1, 0x0e)

board.WriteI2C(D953, 0xB2, 0x01) #vertical back porch

time.sleep(0.1)



print "953 - vertical front porch"

board.WriteI2C(D953, 0xB1, 0x0f)

board.WriteI2C(D953, 0xB2, 0x01) #vertical front porch

time.sleep(0.1)



print "953 - 1st byte of fixed color"

board.WriteI2C(D953, 0xB1, 0x10) 

board.WriteI2C(D953, 0xB2, 0x00) #1st byte of fixed color

time.sleep(0.1)



print "953 - 2nd byte of fixed color"

board.WriteI2C(D953, 0xB1, 0x11)

board.WriteI2C(D953, 0xB2, 0x00) #2nd byte of fixed color

time.sleep(0.1)



print "953 - 3rd byte of fixed color"

board.WriteI2C(D953, 0xB1, 0x12)

board.WriteI2C(D953, 0xB2, 0xFF) #3rd byte of fixed color

time.sleep(0.1)



print "953 - 4th byte of fixed color"

board.WriteI2C(D953,0xB1, 0x13)

board.WriteI2C(D953,0xB2, 0xff) #4th byte of fixed color

time.sleep(0.1)



print "953 - 5th byte of fixed color"

board.WriteI2C(D953,0xB1, 0x14)

board.WriteI2C(D953,0xB2, 0xff) #5th byte of fixed color

time.sleep(0.1)



print "953 - 6th byte of fixed color"

board.WriteI2C(D953,0xB1, 0x15)

board.WriteI2C(D953,0xB2, 0x00) #6th byte of fixed color

time.sleep(0.1)



print "953 - 7th byte of fixed color"

board.WriteI2C(D953,0xB1, 0x16)

board.WriteI2C(D953,0xB2, 0x00) #7th byte of fixed color

time.sleep(0.1)



print "953 - 8th byte of fixed color"

board.WriteI2C(D953,0xB1, 0x17)

board.WriteI2C(D953,0xB2, 0x0f) #8th byte of fixed color

time.sleep(0.1)

#____comment the next lines

board.WriteI2C(D953,0xB1, 0x18)

board.WriteI2C(D953,0xB2, 0xf0) #9th byte of fixed color



board.WriteI2C(D953,0xB1, 0x19)

board.WriteI2C(D953,0xB2, 0x00) #10th byte of fixed color



board.WriteI2C(D953,0xB1, 0x1A)

board.WriteI2C(D953,0xB2, 0x00) #11th byte of fixed color



board.WriteI2C(D953,0xB1, 0x1B)

board.WriteI2C(D953,0xB1, 0x3f) #12th byte of fixed color



board.WriteI2C(D953,0xB1, 0x1C)

board.WriteI2C(D953,0xB2, 0xc0) #13th byte of fixed color



board.WriteI2C(D953,0xB1, 0x1D)

board.WriteI2C(D953,0xB2, 0x00) #14th byte of fixed color



board.WriteI2C(D953,0xB1, 0x1E)

board.WriteI2C(D953,0xB2, 0x00) #15th byte of fixed color



board.WriteI2C(D953,0xB1, 0x1F)

board.WriteI2C(D953,0xB2, 0x00) #16th byte of fixed color