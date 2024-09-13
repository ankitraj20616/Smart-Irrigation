import pyfirmata
import time
from Weather_Forecast import FindCurrentWeather
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
            try:
                sensor_data = self.read_sensor()
                if sensor_data is not None:
                    # Soil Contain no moisture
                    if sensor_data > 700 :
                        # print("WATER IS NEEDED")
                        # print(sensor_data)
                        chances_of_raining = FindCurrentWeather()
                        chances_of_raining = chances_of_raining.detectRain()
                        if chances_of_raining:
                            print(f"Soil contain no moisture but rain is going to happen no need to water the plant, sensor data: {sensor_data}")
                        else:
                            print(f"Rain is not going to happen and soil has no moisture, Water the plant, sensor data: {sensor_data}")
                    
                    # Soil contain moisture
                    elif sensor_data < 700 :
                        print(f"NO WATER IS NEEDED, soil contail moisture, sensor data:{sensor_data}")
                        # print(sensor_data)
                time.sleep(1)
            except:
                print("Closing the application")
                return
if __name__ == "__main__":
    controller = Sense_Soil(1)
    controller.run()