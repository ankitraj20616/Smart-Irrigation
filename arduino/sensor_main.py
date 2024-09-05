import pyfirmata
import time

import pyfirmata.util

class Sense_Soil:
    def __init__(self, sensor_pin) -> None:
        self.board = pyfirmata.Arduino('COM5')

        self.sensor_pin_input = self.board.get_pin(f'a:{sensor_pin}:i')

        # Creating iterator to aviod overflow during continues data reading
        
        it = pyfirmata.util.Iterator(self.board)
        it.start()

        self.sensor_pin_input.enable_reporting()


    def read_sensor(self):
        sensor_data = self.sensor_pin_input.read() 
        if sensor_data is not None:
            sensor_data *= 1023
            return int(sensor_data)
        return None

    def run(self):
        while True:
            sensor_data = self.read_sensor()
            if sensor_data is not None:
                if sensor_data > 700 :
                    print("WATER IS NEEDED")
                    print(sensor_data)
                elif sensor_data > 300 and sensor_data < 700 :
                    print("THERE IS SOME MOISTURE")
                    print(sensor_data)
                elif sensor_data < 300 :
                    print("NO WATER IS NEEDED")
                    print(sensor_data)
            time.sleep(1)

if __name__ == "__main__":
    controller = Sense_Soil(1)
    controller.run()