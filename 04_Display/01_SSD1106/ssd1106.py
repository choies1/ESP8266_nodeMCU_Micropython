# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:23:18 2016

@author: choies

original library source
https://bitbucket.org/thesheep/micropython-ili9341/src/tip/sh1106.py?fileviewer=file-view-default
 + add ( def init_display(self):)

SSD1106(= SH1106) OLED drvier for Micropython & esp8266
"""

import framebuf
import time


# _SET_PAGE_ADDRESS = const(0xB0)
# _DISPLAY_OFF = const(0xAE)
# _DISPLAY_ON = const(0xAF)
# _LOW_COLUMN_ADDRESS = const(0x00)
# _HIGH_COLUMN_ADDRESS = const(0x10)
# _START_LINE_ADDRESS = const(0x40)
# _SET_CONTRAST_CTRL_REG = const(0x81)
# _SET_NORMAL_DISPLAY = const(0xA6) # normal/inverse

# register definitions
DISPLAYOFF          = 0xAE
SETCONTRAST         = 0x81
DISPLAYALLON_RESUME = 0xA4
DISPLAYALLON        = 0xA5
NORMALDISPLAY       = 0xA6
INVERTDISPLAY       = 0xA7
DISPLAYON           = 0xAF
SETDISPLAYOFFSET    = 0xD3
SETCOMPINS          = 0xDA
SETVCOMDETECT       = 0xDB
SETDISPLAYCLOCKDIV  = 0xD5
SETPRECHARGE        = 0xD9
SETMULTIPLEX        = 0xA8
SETLOWCOLUMN        = 0x00
SETHIGHCOLUMN       = 0x10
SETSTARTLINE        = 0x40
MEMORYMODE          = 0x20
COLUMNADDR          = 0x21
PAGEADDR            = 0x22
COMSCANINC          = 0xC0
COMSCANDEC          = 0xC8
SEGREMAP            = 0xA0
CHARGEPUMP          = 0x8D
EXTERNALVCC         = 0x10
SWITCHCAPVCC        = 0x20
SETPAGEADDR         = 0xB0
SETCOLADDR_LOW      = 0x00
SETCOLADDR_HIGH     = 0x10
ACTIVATE_SCROLL                      = 0x2F
DEACTIVATE_SCROLL                    = 0x2E
SET_VERTICAL_SCROLL_AREA             = 0xA3
RIGHT_HORIZONTAL_SCROLL              = 0x26
LEFT_HORIZONTAL_SCROLL               = 0x27
VERTICAL_AND_RIGHT_HORIZONTAL_SCROLL = 0x29
VERTICAL_AND_LEFT_HORIZONTAL_SCROLL  = 0x2A
SETSEGMENTREMAP = 0xA1

class SSD1106:
    width = 128
    height = 64

    def __init__(self, spi, dc, rst, cs):
        self.rate = 10 * 1024 * 1024
        self.spi = spi
        self.cs = cs
        self.dc = dc
        self.rst = rst
        self.cs.init(self.cs.OUT, value=1)
        self.dc.init(self.dc.OUT, value=0)
        self.rst.init(self.rst.OUT, value=1)
        self._buffer = bytearray(self.height // 8 * self.width)
        self._framebuf = framebuf.FrameBuffer1(
            self._buffer, self.width, self.height)
        self.reset()
        self.init_display()

    def reset(self):
        self.rst.low()
        time.sleep_ms(50)
        self.rst.high()
        time.sleep_ms(50)


    def init_display(self):
        for cmd in (
			DISPLAYOFF,
            MEMORYMODE,
            SETHIGHCOLUMN, 0xB0, 0xC8,
            SETLOWCOLUMN, 0x10, 0x40,
            SETCONTRAST, 0x7F,
            SETSEGMENTREMAP,
            NORMALDISPLAY,
            SETMULTIPLEX, 0x3F,
            DISPLAYALLON_RESUME,
            SETDISPLAYOFFSET, 0x00,
            SETDISPLAYCLOCKDIV, 0xF0,
            SETPRECHARGE, 0x22,
            SETCOMPINS, 0x12,
            SETVCOMDETECT, 0x20,
            CHARGEPUMP, 0x14,
            DISPLAYON):
            self._write(cmd)
        self.fill(0)
        self.show()

    def _data(self, data):
        #self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        #self.cs.high()
        self.dc.high()
        self.cs.low()
        self.spi.write(data)
        self.cs.high()

    def _write(self, command, data=None):
        #self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        #self.cs.high()
        self.dc.low()
        self.cs.low()
        self.spi.write(bytearray([command]))
        self.cs.high()
        if data:
            self._data(data)

    # def vscroll(self, dy):
    #     self._write(_START_LINE_ADDRESS | dy & 0x3f)
    #
    # def inverse(self, value):
    #     self._write(_SET_NORMAL_DISPLAY | bool(value))
    #
    # def contrast(self, value):
    #     self._write(_SET_CONTRAST_CTRL_REG, bytearray([value]))
    #
    # def sleep(self, value):
    #     self._write(_DISPLAY_OFF | (not value))

    def vscroll(self, dy):
        self._write(SETSTARTLINE | dy & 0x3f)

    def inverse(self, value):
        self._write(NORMALDISPLAY | bool(value))

    def contrast(self, value):
        self._write(SETCONTRAST, bytearray([value]))

    def sleep(self, value):
        self._write(DISPLAYOFF | (not value))

    def fill(self, col):
        self._framebuf.fill(col)

    def pixel(self, x, y, col):
        self._framebuf.pixel(x, y, col)

    def scroll(self, dx, dy):
        self._framebuf.scroll(dx, dy)

    def text(self, string, x, y, col=1):
        self._framebuf.text(string, x, y, col)

    def show(self):
        for page in range(self.height // 8):
            self._write(SETPAGEADDR | page)
            self._write(SETCOLADDR_LOW | 2)
            self._write(SETCOLADDR_HIGH | 0)
            self._data(self._buffer[
                self.width * page:self.width * page + self.width
            ])
