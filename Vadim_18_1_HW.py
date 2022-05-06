class Car:


    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
         print(f'{self.title}, {self.model}  engine started!')

    def stop_engine(self):
        print(f'{self.title}, {self.model}  engine stoped!')

    def info(self):
        print(f'All Info: {self.title}  {self.model} {self.weight} {self.hp} {self.nm} {self.max_speed} {self.color}')

toyota = Car("toyota", "supra", 1410, 280, 432, 250, "silver")
nissan = Car("Nissan",  "GT-R R35", 1769, 570, 637, 320, "orenge")

nissan.start_engine()
toyota.start_engine()


nissan.stop_engine()
toyota.stop_engine()

nissan.info()
toyota.info()