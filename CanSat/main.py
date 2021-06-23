import Vmodule

gps = Vmodule.Vmodule('gps')
acc = Vmodule.Vmodule('acceleration')

gps.step(1)
gps.step(1)

