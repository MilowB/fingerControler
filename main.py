import flicklib
import time

@flicklib.move()
def move(x, y, z):
    print(x)
    # Send z to the server
    pass    

@flicklib.double_tap()
def doubletap(position):
    # get the light state
    # reverse it
    # send the result
    pass

while True:
    time.sleep(0.1)