class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init_subclass__(cls) -> None:
        super().__init__()
    def swin(self):
        print("Moving in water")
    def breathe(self):
        super().breathe()
        print("Under water")

nemo = Fish()
nemo.swin()
nemo.breathe()