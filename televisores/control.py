class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self,tv):
        tv.setControl(self)
        self._tv = tv
    def setTv(self,tv):
        self._tv = tv
    def getTv(self):
        return self.tv
    def turnOn(self):
       if self._tv is not None: 
            self.tv.turnOn()
    def turnOff(self):
        if self._tv is not None:
            self._tv.turnOff()
    def volumenUp(self):
        if self._tv is not None:
            self._tv.volumenUp()
    def volumenDown(self):
        if self._tv is not None:
            self._tv.volumenDown()
    def canalUp(self):
        if self._tv is not None:
            self._tv.canalUp()
    def canalDown(self):
        if self._tv is not None:
            self._tv.canalDown()
    def setCanal(self, canal):
        if self._tv is not None:
            self._tv.setCanal(canal)
    def setVolumen(self, volumen):
        if self._tv is not None:
            self._tv.setVolumen(volumen)
    