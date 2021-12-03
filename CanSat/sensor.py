class Sensor:
    def get_acc(self):
        if self.is_auto_step:
            self.step(1)
        return self.data_set
    
    def get_gyro(self):
        if self.is_auto_step:
            self.step(1)
        return self.data_set

    def get_mag(self):
        if self.is_auto_step:
            self.step(1)
        return self.data_set