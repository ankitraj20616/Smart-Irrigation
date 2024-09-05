import pyfirmata
import time


board = pyfirmata.Arduino('COM5')

# to start communicating with board
# iterator = pyfirmata.util.Iterator(board)
# iterator.start()

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)