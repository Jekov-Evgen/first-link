import openpyxl
from graph import Graph

class Logics:
    def __init__(self, path: str) -> None:
        self.time = []
        self.value = [] 
        self.path = path 
        
    def read_data(self):
        data = openpyxl.open(self.path, read_only=True)
        sheet = data.active
        
        for row in range(1, sheet.max_row + 1):
            time_value = sheet.cell(row=row, column=1).value  
            data_value = sheet.cell(row=row, column=2).value 
            
            if time_value is not None and data_value is not None:
                self.time.append(time_value) 
                self.value.append(data_value)
        
    def draw_graph(self):
        Graph(self.time, self.value)
        
    def calculations(self):
        last_value = self.value[-1]
        call = last_value * 0.63
        
        closest_index = 0
        closest_value = self.value[0]
        min_diff = abs(self.value[0] - call)
        
        for i in range(1, len(self.value)):
            diff = abs(self.value[i] - call)
            if diff < min_diff:
                min_diff = diff
                closest_value = self.value[i]
                closest_index = i
        
        return [last_value, call, closest_index]