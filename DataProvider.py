import json

#my_file = open('test_data.json', 'r')
#g_data = json.load(my_file)

with open('test_data.json', 'r') as file:
    g_data = json.load(file)
    

class DataProvide:
    def __init__(self) -> None:
        self.data = g_data
                
    def get(self, prop: str) -> str:
        return self.data.get(prop)
    
    def get_token(self):
        return self.data.get("token")
    '''
    def get_timeout(self):
        return self.config["ui"].getint["timeout"]
    def get_choosen_browser(self):
        return self.config["ui"].get["browser_name"]
        '''
        