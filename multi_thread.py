from threading import Thread
import time

def toast_bread():
    print("toasting bread..")
    time.sleep(8)
    print("bread toasted")

def make_some_coffee():
    print("turned on coffee maker..")
    time.sleep(4)
    print("Poured a nice cup of coffee")

def boil_water_and_egg():
    print("boiling water..")
    time.sleep(5.5)
    print("water boiled")

threadlist = []

threadlist.append(Thread(target=toast_bread))
threadlist.append(Thread(target=boil_water_and_egg))
threadlist.append(Thread(target=make_some_coffee))

for t in threadlist:
  t.start()

for t in threadlist:
  t.join()