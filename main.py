from cars import create_car, get_car_info

bmw = create_car.Car("BMW", "i8", 321, "white")

bmw.start_engine()
bmw.stop_engine()
get_car_info.car_info(bmw)