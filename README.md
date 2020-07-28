# Penguinpi

Library for communicating with and controlling the [PenguinPi](https://cirrusrobotics.com/products/penguinpi/) robot platform.

**Key features:**
- Motor control and encoder querying
- Access to camera
- Access to HAT and LED screen

# Installing

```
# Python2.7
pip install penguinpi

# Python3
pip3 install penguinpi
```

# Basic usage
```py
import penguinpi
import time
import cv2

address = 'xxx.xxx.xxx.xxx'
port = 8080

bot = penguinpi.PiBot(address, port)

bot.setVelocity(50, 50)
time.sleep(2)
bot.stop()

img = bot.getImage()
cv2.imshow('image', img)
cv2.waitKey(0)
```