from csv import reader
import math

class Vmodule:

    def __init__(self, path, is_auto_step):
        self.config_path = './' + path + '.csv'
        self.process = 0
        self.data_set = [0,0,0,0,0,0]
        self.goal = [41.833705, 140.770666]
        self.is_auto_step = is_auto_step

        #csv to list
        with open(self.config_path, 'r') as csv_file:
            csv_reader = reader(csv_file)
            self.process_list = list(csv_reader)
            
        self.len = len(self.process_list)
            
    def step(self, n):
        self.data_set = self.process_list[self.process]
        if int(n) < 1:
            print("error: please input number, that greater than 1")
        if self.process < self.len - 1:
            self.process += int(n)
        else:
            self.process = 0

    def get_data(self):
        if self.is_auto_step:
            self.step(1)
        return self.data_set

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
        
    def getLatitude(self):
        return self.data_set[0]
    
    def getLongitude(self):
        return self.data_set[1]

    def getX(self):
        return self.data_set[2]

    def getY(self):
        return self.data_set[3]
    
    def getZ(self):
        return self.data_set[4]
    
    def getMagnet(self):
        return self.data_set[5]
