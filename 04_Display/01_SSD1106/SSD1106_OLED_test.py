from machine import SPI, Pin
import ssd1106 #SSD1106(SH1106) OLED

class nodeMCU:
    #nodeMCU: ESP8266 Chip
    D0 = 16
    D1 = 5
    D2 = 4   
    D3 = 0   #Flash button
    D4 = 2   #built-in LED
    D5 = 14  #SPI_CLK
    D6 = 12  #SPI_MISO
    D7 = 13  #SPI_MOSI
    D8 = 15  #SPI_CS
    D9 = 3   #RXD0
    D10 = 1  #TXD0
    A0 = 0   #ADC0

#spi = SPI(mosi=Pin(13, Pin.OUT), sck=Pin(14, Pin.OUT))
#display = ssd1106.SSD1106(spi=spi, dc=Pin(4, Pin.OUT), rst=Pin(5, Pin.OUT), cs=Pin(15, Pin.OUT))

spi = SPI(mosi=Pin(nodeMCU.D7, Pin.OUT), sck=Pin(nodeMCU.D5, Pin.OUT))
display = ssd1106.SSD1106(spi=spi, dc=Pin(nodeMCU.D2, Pin.OUT), rst=Pin(nodeMCU.D1, Pin.OUT), cs=Pin(nodeMCU.D8, Pin.OUT))

display.fill(0)
display.text('<*OLED Test*>', 0,0)
display.text('SSD1106(=SH1106)', 0,10)
display.text('#Resol:128 x 64', 0,20)
display.text('-Micropython', 0,30)
display.text('On ESP8266 -', 0,40)
display.text('*2016-10-15* ', 0,50)

display.show()
