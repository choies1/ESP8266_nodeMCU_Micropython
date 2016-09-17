# ESP8266_nodeMCU_Micropython
Micropython code for nodeMCU(ESP8266 board)

This is my Micropython test code for nodeMCU(ESP8266-based)

Followings are my board and firmware settings.

## 1. Board:

[nodeMCU(LoLin)](http://www.banggood.com/V3-NodeMcu-Lua-WIFI-Development-Board-p-992733.html)

<img src="/00_ReadMe/nodeMCU_LoLin_v3_small.png" width="200">

## 2. Pin Map
### nodeMCU Board & ESP8266 Pin Map

![nodeMCU Board Pin Map](./00_ReadMe/LoLin_V3_NodeMCU_Pinout.png)

### Summary: NodeMCU Board, ESP8266 IO Map

| nodeMCU Pin| ESP8266 Pin (GPIO)| Function |
| --------|-------|-----|
| D0      | GPIO 16  | GPIO |
| D1      | GPIO 05  | GPIO |
| D2      | GPIO 04  | GPIO |
| D3      | GPIO 00  | GPIO, Flash |
| D4      | GPIO 02  | GPIO, Built-in LED, TXD1|
| D5      | GPIO 14  | GPIO |
| D6      | GPIO 12  | GPIO |
| D7      | GPIO 13  | GPIO, RXD2|
| D8      | GPIO 15  | GPIO, TXD2|
| D9      | GPIO 03  | GPIO, RXD0|
| D10     | GPIO 01  | GPIO, TXD0|
| A0      | A0       | Analog Input |

## 3. Firmware
### Download 1
- 'nodemcu\_float\_0.9.6-dev\_20150704.bin' in
[NodeMCU Firwware](https://github.com/nodemcu/nodemcu-firmware/releases)
- Baudrate: 9600bps

### Download 2
- Online build in [http://nodemcu-build.com/](http://nodemcu-build.com)
- You can select modules and receive it from e-mail.


## 4. NodeMCU Flasher (Firmware Downloader)
- Download and install NodeMCU Flasher for Windows in [http://www.14core.com/downloads-2/](http://www.14core.com/downloads-2/)


## 5.ESPlorer (NodeMCU IDE)
- Download and install ESPlorer in [http://www.14core.com/downloads-2/](http://www.14core.com/downloads-2/)
