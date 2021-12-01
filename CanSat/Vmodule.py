from csv import reader
import math

class Vmodule:

    def __init__(self, path):
        self.config_path = './' + path + '.csv'
        self.process = 0
        self.data_set = [0,0,0]

        #csv to list
        with open(self.config_path, 'r') as csv_file:
            csv_reader = reader(csv_file)
            self.process_list = list(csv_reader)
            
    def step(self, n):
        self.data_set = self.process_list[self.process]
        if int(n) < 1:
            print("error: please input number, that greater than 1")
        self.process += int(n)
        

    def getLatitude(self):
        return self.data_set[0]
    
    def getLongitude(self):
        return self.data_set[1]

    def getX(self):
        return self.data_set[0]

    def getY(self):
        return self.data_set[1]
    
    def getZ(self):
        return self.data_set[2]

    def getLet(self):
        dis_now_x = int(self.old_data_set[0]) - int(self.data_set[0])
        dis_now_y = int(self.old_data_set[1]) - int(self.data_set[1])
        dis_goal_x = int(self.goal[0]) - int(self.data_set[0])
        dis_goal_y = int(self.goal[1]) - int(self.data_set[1])
        asin_now = math.degrees(math.atan2(dis_now_y, dis_now_x))
        asin_goal = math.degrees(math.atan2(dis_goal_y, dis_goal_x))
        let = asin_goal - asin_now 
        return let
    
    def volt(self):
        self.old_data_set = self.data_set
