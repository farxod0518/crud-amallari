# class Tub_sonlar:
#     def __init__(self, start: int, stop: int ):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
        
#         if self.start >= self.stop:
#             raise StopIteration
#         else:
#             check = 0
#             for n in range(2 ,self.start):
#                 if self.start%n ==0:
#                     check+=1
#             if check>0:
#                 self.start +=1
#             else:
#                 temp = self.start
#                 self.start+=1
#                 return temp
        


# my_number = Tub_sonlar(6,20)
# for i in my_number:
#     if i ==None:
#         continue
#     print(i)


def Tub_son(stop):
    number = 2

    while True:
        check = 0
        for n in range(1 ,number):
            if number%n==0:
                check+=1
        if number>=stop:
            break
        else:
            if check>=2:
                number+=1
                continue
            else:
                yield number
                number+=1
            


for i in Tub_son(130):
    print(i)
       