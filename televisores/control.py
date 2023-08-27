class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self,tv):
        tv.setControl(self)
        self.tv = tv
    def setTv(self,tv):
        self.tv = tv
    def getTv(self):
        return self.tv
    def turnOn(self):
       if self.tv is not None: 
            self.tv.turnOn()
    def turnOff(self):
        if self.tv is not None:
            self.tv.turnOff()
    def volumenUp(self):
        if self.tv is not None:
            self.tv.volumenUp()
    def volumenDown(self):
        if self.tv is not None:
            self.tv.volumenDown()
    def canalUp(self):
        if self.tv is not None:
            self.tv.canalUp()
    def canalDown(self):
        if self.tv is not None:
            self.tv.canalDown()
    def setCanal(self, canal):
        if self.tv is not None:
            self.tv.setCanal(canal)
    def setVolumen(self, volumen):
        if self.tv is not None:
            self.tv.setVolumen(volumen)
    