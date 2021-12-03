class GPS:
    def get_data(self):
        if self.is_auto_step:
            self.step(1)
        return self.data_set