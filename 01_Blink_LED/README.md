# Blink LED example

## GPIO On/Off
### Configure Pin
- LED1 = machine.Pin(nodeMCU.D4, machine.Pin.OUT)

### Control Pin
- Pin.high() for GPIO high
- Pin.low() for GPIO low
- LED1.high() =  LED.value(1) = LED.value(True)
- LED1.low() = LED.value(0) = LED.value(False)

# Send file to nodeMCU Board
## Install ampy and  run code using ampy
- Install ampy
: refer to
[https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)

- Run code
```
 ampy --port -p COM4 run 01_Blink_LED.py
```
- You can run code with '--no-output option'
```
 ampy --port -p COM4 run --no-output option 01_Blink_LED.py
```
