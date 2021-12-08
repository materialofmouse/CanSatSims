import Vmodule

sensor = Vmodule.Vmodule('gps',True)

i = 0
while i < 5:
    print(sensor.get_acc())
    print(len(sensor.data_set))
    i += 1