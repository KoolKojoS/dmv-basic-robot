import adafruit_vcnl4020
import board

from wander import BasicWander


if __name__ == "__main__":
    i2c = board.I2C()
    left_proximity_sensor = adafruit_vcnl4020.Adafruit_VCNL4020(i2c, addr=)
    right_proximity_sensor = adafruit_vcnl4020.Adafruit_VCNL4020(i2c, addr=)
    front_proximity_sensor = adafruit_vcnl4020.Adafruit_VCNL4020(i2c, addr=)

    just_wander = BasicWander(left_proximity_sensor,
                              right_proximity_sensor,
                              front_proximity_sensor)
    while True:
        just_wander.step()
