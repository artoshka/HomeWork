

class Car:



    def __init__(self, title, model, max_speed, color):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title}, {self.model}  engine started!')

    def stop_engine(self):
        print(f'{self.title}, {self.model}  engine stoped!')

