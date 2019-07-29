
class Field:
    def __init__(self):
        self.cells = {}
        self.cell_size = 3 #size cell in pixel

    
    def field_gen(self,screenSize):
        scx,scy = screenSize
        for i in range(0,scx):
            self.cells = {name:(pos,filled)}

