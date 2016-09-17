import machine
import time

print("Hello Python!!")


class nodeMCU:
    #nodeMCU: ESP8266 Chip
    D0 = 16
    D1 = 5
    D2 = 4
    D3 = 0
    D4 = 2 #built-in LED
    D5 = 14
    D6 = 12
    D7 = 13
    D8 = 15
    D9 = 3
    D10 = 1
    A0 = 0

LED1 = machine.Pin(nodeMCU.D4, machine.Pin.OUT)

# for i in range(1,5):
# # while True:
#     print("Blinking")
#     LED1.high()
#     time.sleep(0.5)
#     LED1.low()
#     time.sleep(0.5)

for i in range(1,5):
# while True:
    print("Blinking")
    LED1.value(0)
    time.sleep(0.5)
    LED1.value(1)
    time.sleep(0.5)
