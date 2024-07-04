# class Fibonacci:
#     def __init__(self, stop,first , secend ):
#         self.stop = stop
#         self.first = first
#         self.secend = secend
        

#     def __iter__(self):
#         return self

#     def __next__(self):
        
       
#         if self.stop<self.first:
#             raise StopIteration
#         else:
#             temp = self.first
#             self.first = self.secend
#             self.secend +=temp
#             return temp



    


# my_fibonacci = Fibonacci(100,0,1)

# for i in my_fibonacci:
#     print(i)


class Fibonacci:
    def __init__(self, start, stop, secend):
        self.start = start
        self.stop = stop
        self.secend = secend

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.start >= self.stop:
            raise StopIteration
        else:
            temp = self.start
            self.start = self.secend
            self.secend +=temp
            return temp
        

my_fibonachi = Fibonacci(0 , 100 , 1)
for i in my_fibonachi:
    print(i)

       