
import psycopg2
from datetime import date

db = psycopg2.connect(
    database='malumotlar',
    user='postgres',
    host='localhost',
    password='1'
)

cursor = db.cursor()

cursor.execute('''
    drop table if exists avtomobillar cascade;
    drop table if exists clientlar cascade;
    drop table if exists buyrtmalar cascade;
    drop table if exists xodimlar cascade;
''')

cursor.execute('''
    create table if not exists avtomobillar(
        id serial primary key,
        nomi varchar(100) not null,
        model text,
        yil integer,
        narx numeric(12,2),
        mavjudmi bool default true
    );
    
    create table if not exists clientlar(
        id serial primary key,
        ism varchar(50) not null,
        familyasi varchar(50),
        telefon char(13),
        manzil text
    );
    
    create table if not exists buyrtmalar(
        buyurtma_id serial primary key,
        avtomobil_id integer references avtomobillar(id),
        client_id integer references mijozlar(id),
        sana date not null,
        umumiy_narx numeric(12,2)
    );
    
    create table if not exists xodimlar(
        id serial primary key,
        ism varchar(50) not null,
        lavozim varchar(50),
        maosh numeric(10,2)
    );
''')

cursor.execute('''
    insert into avtomobillar(nomi, model, yil, narx) values
    ('fd', 'damas', 2020, 5000),
    ('gy', 'neksiya', 2021, 6000);
    
    insert into clientlar(ism, familyasi, telefon, manzil) values
    ('habibullo', 'qurbonov', '+99865432234', 'qoqon'),
    ('bokir', 'oripov', '+99863455434', 'uchkoprik');
    
    insert into buyrtmalar(avtomobil_id, client_id,sana, umumiy_narx) values
    (1, 1,%s, 15000),
    (2, 2, %s,20000);
    
    insert into xodimlar(ism, lavozim, maosh) values
    ('sobir', 'ish yurutuvchi', 600),
    ('bakir', 'sotuvchi', 400);
''',(date.today(),date.today(),))

cursor.execute(''' alter table clientlar rename column ism to new_ism;''')

cursor.execute('''update xodimlar set ism = 'umidjon' where id = 1; ''')
cursor.execute('''update xodimlar set ism = 'habibullo' where id = 2; ''')

cursor.execute('''delete from xodimlar where id = 1 ''')



cursor.execute('select * from avtomobillar;')
print(cursor.fetchall())

cursor.execute('select * from clientlar;')
print(cursor.fetchall())

cursor.execute('select * from buyrtmalar;')
print(cursor.fetchall())

cursor.execute('select * from xodimlar;')
print(cursor.fetchall())


db.commit()
db.close()
