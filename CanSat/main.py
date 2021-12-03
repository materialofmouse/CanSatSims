import Vmodule

sensor = Vmodule.Vmodule('gps',True)

i = 0
while i < 10:
    print(sensor.get_acc())
    i += 1