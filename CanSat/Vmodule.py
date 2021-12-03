from csv import reader
from gps import GPS
from sensor import Sensor
import math

class Vmodule(GPS, Sensor):

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