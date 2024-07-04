# car = {
#     "name":"nexia",
#     "model":"chevrolet",
#     "color":"oq",
#     "year":"2009",
#     "price":5000
# }

# car_iterator = iter(car.items())

# while True:
#     try:
#         print(next(car_iterator))
#     except StopIteration:
#         break

# print(type(car.items()))

# car_iter = iter(car)

# while True:
#     try:


class Myrange:
    def __init__(self ,start ,stop ,stamp) -> None:
        self.start = start
        self.stop = stop
        self.stamp = stamp
        now = self.start
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if now>self.stop:
                break
            else:
                now = self.start
                self.start+=self.stamp
                return now
som = Myrange(10,20,2)
for i in som:
    print(i)
    