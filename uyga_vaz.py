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





# CRUD

def CREATE_TABLE(table_name):
    with dataconnect(database) as (conn, cur):
        create_table_query = f'''create table IF NOT EXISTS {table_name} (
        id serial primary key not null 
        );
            '''
        cur.execute(create_table_query)
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

def delete_tables(table_name):
    with dataconnect(database) as (conn, cur):
        try:
            delete_table = f"""
                drop table {table_name}
            """ 
            cur.execute(delete_table)
            conn.commit()     
        except: 
            print("bunday table topilmadi.")      


def update_tables_name(table_name ,new_table_name):
    with dataconnect(database) as (conn, cur):
        try:
            update_table = f"""
                alter table {table_name}
                    rename to {new_table_name}
            """ 
            cur.execute(update_table)
            conn.commit()      
        except:
            print("amalyot bajarilmadi.")     


def run_function():
    while True:
        choise = int(input(
            "bulimni tanlang (\n malumot olish->1 \n table yatatish->2 \n tablelarni o'chirish->3 \n tablelarni nomini o'zgartishish ->4\n chiqish->5  : "))
        if choise == 1:
            table_name = input("inter table_name")
            Read_tables(table_name)
        elif choise == 2:
            table_name = input("inter table_name")
            CREATE_TABLE(  table_name)
        elif choise == 4:
            table_name = input("inter table_name")
            new_tables_name = input("inter new table name")
            update_tables_name(table_name , new_tables_name)
        elif choise == 3:
            table_name = input("inter table_name")
            delete_tables(table_name )
        elif choise==5:
            print("foydalanganingiz uchun rahmat!")
            break
        else:
            print("noto'g'ri bo'limni tanladingiz.")
            continue


run_function()