import adafruit_vcnl4020
import board


if __name__ == "__main__":
    i2c = board.I2C()
    proximity_sensor = adafruit_vcnl4020.Adafruit_VCNL4020(i2c)
    while True:
        print(proximity_sensor.proximity)
