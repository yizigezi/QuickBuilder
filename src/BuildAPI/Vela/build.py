# Vela JS App BuildAPI

class buildProcess:
    def __init__(self, 
                 designWidth: list, 
                 jsc:bool=False, 
                 custom_component:bool=False, 
                 protobuf:bool=False,
                 env:str='debug'):
        self.designWidth = designWidth
        self.env = env
        self.buildProps = []
        if jsc:
            self.buildProps.append('--enable-jsc')
        if custom_component:
            self.buildProps.append('--enable-custom-component')
        if protobuf:
            self.buildProps.append('--enable-protobuf')

    def sideload(self):
        pass