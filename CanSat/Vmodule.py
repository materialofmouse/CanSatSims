from csv import reader

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

