# Blink LED example

## GPIO On/Off
### Configure Pin
- LED1 = machine.Pin(nodeMCU.D4, machine.Pin.OUT)

### Control Pin
- Pin.high() for GPIO high
- Pin.low() for GPIO low
- LED1.high() =  LED.value(1) = LED.value(True)
- LED1.low() = LED.value(0) = LED.value(False)
