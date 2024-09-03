import pyfirmata
import time

import pyfirmata.util

class Sense_Soil:
    def __init__(self, sensor_pin, button_pin) -> None:
        self.board = pyfirmata.Arduino('COM5')

        self.sensor_pin_input = self.board.get_pin(f'a:{sensor_pin}:i')
        self.button_pin = self.board.get_pin(f'd:{button_pin}:i')

        # Creating iterator to aviod overflow during continues data reading
        it = pyfirmata.util.Iterator(self.board)
        it.start()

        self.sensor_pin_input.enable_reporting()


    def read_sensor(self):
        sensor_data = self.sensor_pin_input.read()
        if sensor_data is not None:
            sensor_data *= 1023
            return sensor_data
        return None

    def map_to_digital_value(self, sensor_data, analog_min, analog_max, digital_max, digit_min):
        return (sensor_data - analog_min) * (digital_max - digit_min) // (analog_max - analog_min) + digit_min

    def run(self):
        while True:
            sensor_data = self.read_sensor()
            if sensor_data is not None:
                sensor_digital_data = self.map_to_digital_value(sensor_data, 0, 1023, 255, 0)
                print(sensor_digital_data)
                time.sleep(1)

if __name__ == "__main__":
    controller = Sense_Soil(1, 8)
    controller.run()