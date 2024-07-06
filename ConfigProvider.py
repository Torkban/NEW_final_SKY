import configparser

g_config = configparser.ConfigParser()
g_config.sections()
g_config.read('test_config.ini')

class ConfigProvide:
    def __init__(self) -> None:
        self.config = g_config
                
    def get_str(self, section: str, val: str):
        return self.config[section].get[val]
    
    def get_uis_url(self):
        return self.config["ui"].get("base_url")
    
    def get_apis_url(self):
        return self.config["api"].get("api_url")
    
    def get_timeout(self):
        return self.config["ui"].getint("timeout")
    def get_choosen_browser(self):
        return self.config["ui"].get("browser_name")