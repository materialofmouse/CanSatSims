import Vmodule

gps = Vmodule.Vmodule('gps')

gps.step(1)
gps.volt()
gps.step(1)
print(gps.getLet())
gps.volt()