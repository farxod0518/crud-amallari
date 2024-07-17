import threading 
import psycopg2
import time
# 1- masala.



# database = 'postgres'
# user = 'postgres'
# host = 'localhost'
# port = 5432
# password = '0518'

# conn = psycopg2.connect(database=database, user=user, host=host, port=port, password=password)
# cur = conn.cursor()



# create_table_query = '''create table if not exists product(
#                 id serial PRIMARY KEY,
#                 name varchar(100) NOT NULL,
#                 price float NOT NULL ,
#                 color VARCHAR(100) NOT NULL,
#                 image VARCHAR(100) NOT NULL
# );
# '''
# cur.execute(create_table_query)
# conn.commit()
# print("Table created successfully")

# cur.close()
# conn.close()



#  2- masala


# database = 'postgres'
# user = 'postgres'
# host = 'localhost'
# port = 5432
# password = '0518'

# conn = psycopg2.connect(database=database, user=user, host=host, port=port, password=password)
# cur = conn.cursor()


# class Product :
#     def __init__(self , name:str , price: float , color:str , image: str):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image

# def insert_product():

#     name = input("inter name :")
#     color = input("inter color :")
#     image = input("inter image :")
#     price = int(input("inter price :"))
#     create_table_query = '''insert into product ( name , price , color , image)
#      values(%s,%s,%s,%s)
#      ;
#             '''
#     cur.execute(create_table_query , (name , price , color , image))
#     conn.commit()


# def select_all_product(): 
    
#     select_table = f"""
#         select * from product;
#         """  
#     cur.execute(select_table)
#     rows = cur.fetchall() 
#     for row in rows:
#         print(row)        
    

# def delete_product():
#     name = input("uchiriladigan productni name ni kiriting :")
#     delete_table = f"""
#         delete * from product where name = %s
#     """ 
#     cur.execute(delete_table ,(name,))
#     conn.commit()     
  


# def update_product():
#     id = input("uzgartiriladigan product id sini kiriting :")
#     product = Product('olma',1200,"oq","qqq")
#     product.name = input("inter name :")
#     product.color = input("inter color :")
#     product.image = input("inter image :")
#     product.price = int(input("inter price :"))
    
#     create_table_query ='''
#     UPDATE product
#     SET name , color , image , price = %s , %s , %s ,%s ,%s 
#     WHERE id = %s;
#     '''
#     cur.execute(create_table_query , (product.name , product.color , product.image , product.price , id))
#     conn.commit()    
   


# def run_function():
#     while True:
#         choise = int(input(
#             "bulimni tanlang (\n malumot kiritish->1 \n tableni kurish->2 \n tablelarni uzgartirish->3 \n productni uchirish ->4\n chiqish->5  : "))
#         if choise == 1:
#             insert_product()
#         elif choise == 2:
#             select_all_product()
#         elif choise == 4:
#             delete_product()
#         elif choise == 3:
#             update_product()
#         elif choise==5:
#             print("foydalanganingiz uchun rahmat!")
#             break
#         else:
#             print("noto'g'ri bo'limni tanladingiz.")
#             continue


# run_function()
# cur.close()
# conn.close()



#  3- masala


# class Alphabet:
#     def __init__(self, alfabet: list):
#         self.index = 0
#         self.alfabet=alfabet

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.alfabet):
#             raise StopIteration
#         else:
#             temp = self.alfabet[self.index]
#             self.index += 1
#             return temp

# alfabet = ['A','B','C','D','E','F','J','G','L','M','N','O','P','Q','R','S','W','Y','Z']

# MY_ITER = Alphabet(alfabet=alfabet)
# for i in MY_ITER:
#     print(next(MY_ITER))

#  4- masala



# def print_number():

#     for i in range(1,6):
#         print(i)
#         time.sleep(1)


# def print_leters():
#     for i in ("A","B","C","D","E"):
#         print(i)
#         time.sleep(1)


# thread1 = threading.Thread(target=print_number)
# thread2 = threading.Thread(target=print_leters)
# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()


#  5- masala


# class product:
#     def __init__(self,name:str , price:float , color :str, image:str) :
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image

#     def save(self):

#         database = 'postgres'
#         user = 'postgres'
#         host = 'localhost'
#         port = 5432
#         password = '0518'

#         conn = psycopg2.connect(database=database, user=user, host=host, port=port, password=password)
#         cur = conn.cursor()
#         create_table_query = '''insert into product ( name , price , color , image)
#          values(%s,%s,%s,%s)
#          ;
#             '''
#         cur.execute(create_table_query , (self.name , self.price , self.color , self.image))
#         conn.commit()
#         cur.close()
#         conn.close()

# olcha = product('olcha' , 1000 , 'qizil' , 'yuq')
# olcha.save()



#  6- masala

# database ={
# 'database' : 'telefonlar',
# 'user' : 'postgres',
# 'host' : 'localhost',
# 'port' : 5432 ,
# 'password' : '0518'
# }

# class DbConnect:
#     def __init__(self, database):
#         self.database = database

#     def __enter__(self):
#         self.conn = psycopg2.connect(**database)

#         self.cur = self.conn.cursor()
#         return self.conn, self.cur

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.conn:
#             self.conn.close()

#         if self.cur:
#             self.cur.close()



