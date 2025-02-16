import adafruit_vcnl4020

from basic_movement import BasicMovement


class BasicWander:
    def __init__(self,
                 left_proximity_sensor: adafruit_vcnl4020.Adafruit_VCNL4020,
                 right_proximity_sensor: adafruit_vcnl4020.Adafruit_VCNL4020,
                 front_proximity_sensor: adafruit_vcnl4020.Adafruit_VCNL4020):
        self.left_sensor = left_proximity_sensor
        self.right_sensor = right_proximity_sensor
        self.front_sensor = front_proximity_sensor
        self.move = BasicMovement()

    def step(self) -> None:
        """
        Send the next movement command based on the current state.
        """
        if self.obstacle_left():
            self.move.right()
        elif self.obstacle_right():
            self.move.left()
        elif self.obstacle_front():
            self.move.left()
        else:
            self.move.forward()
        return
            
    def obstacle_left(self) -> bool:
        """
        Returns whether there is an obstacle to the left of the robot.
        """

        if self.left_sensor.proximity < 500:
            return True
        return False
    
    def obstacle_right(self) -> bool:
        """
        Returns whether there is an obstacle to the right of the robot.
        """

        if self.right_sensor.proximity < 500:
            return True
        return False
    
    def obstacle_front(self) -> bool:
        """
        Returns whether there is an obstacle in front of the robot.
        """

        if self.front_sensor.proximity < 500:
            return True
        return False