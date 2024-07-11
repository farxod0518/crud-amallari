import requests
import json
import threading
import time
import psycopg2



database ={
'database' : 'telefonlar',
'user' : 'postgres',
'host' : 'localhost',
'port' : 5432 ,
'password' : '0518'
}

class dataconnect:
    def __init__(self, database):
        self.database = database

    def __enter__(self):
        self.conn = psycopg2.connect(**database)

        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

        if self.cur:
            self.cur.close()





product_url = requests.get('https://dummyjson.com/products')
user_url = requests.get('https://dummyjson.com/users')



def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as f:
        json.dump(response.json(), f, indent=4)






urls = [
    ('https://dummyjson.com/products', 'products.json'),
    ('https://dummyjson.com/users', 'users.json')
]

threads = [
    threading.Thread(target=download_file, args=(url, filename))
    for url, filename in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()





with dataconnect(database) as (conn, cur):
    create_table_query = f'''create table IF NOT EXISTS products (
    id int not null,
    title varchar(100),
    description text not null,
    category varchar (100),
    price float4 not null ,
    discountPercentage float4 not null,
    rating float4 not null
    );
        '''
    cur.execute(create_table_query)
    conn.commit()

with dataconnect(database) as (conn, cur):
    create_table_query = f'''create table IF NOT EXISTS userss (
    id int not null,
    firstName varchar(100),
    lastName varchar(100) not null,
    maidenName varchar(100),
    age int not null,
    gender varchar(100),
    email varchar(255),
    phone varchar(100),
    username varchar(100),
    password varchar(100),
    birthDate varchar(100),
    image varchar(255),
    bloodGroup varchar(20)
    );
        '''
    cur.execute(create_table_query)
    conn.commit()


product_list = product_url.json()['products']
with dataconnect(database) as (conn, cur):
    query = '''insert into products(id ,title ,description ,category ,price  ,discountPercentage ,rating )
    values(%s,%s,%s,%s,%s,%s,%s);'''
    for product in product_list:
        lists = (product['id'], product['title'], product['description'], product['category'],
                             product['price'], product['discountPercentage'],product['rating'])
        cur.execute(query,lists)
        conn.commit()

    
user_list = user_url.json()['users']
with dataconnect(database) as (conn, cur):
    query = '''insert into userss(id ,firstName ,lastName ,maidenName,age ,gender ,email ,phone ,username ,password ,birthDate ,image ,bloodGroup)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    for user in user_list:
        lists = (user['id'],user['firstName'],user['lastName'],user['maidenName'],user['age'],user['gender'],
                    user['email'],user['phone'],user['username'],user['password'],user['birthDate'],user['image'],user['bloodGroup'])
        cur.execute(query,lists)
        conn.commit()



def Read_tables(table_name):
    with dataconnect(database) as (conn, cur):
        try:
            select_table = f"""
                select * from {table_name}
                """  
            cur.execute(select_table)
            print(cur.fetchall())          
        except:
            print("bunday malumot topilmadi.")

print(Read_tables('userss'))

print(Read_tables('products'))