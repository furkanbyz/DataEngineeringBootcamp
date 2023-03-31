# DataEngineeringBootcamp

postgreSql şifre: postgre
localhost: 5432

@@@@@ SQL TEMELLERİ @@@@@
@@@SELECT, WHERE, BETWEEN IN@@@
-- select title, length from film where length<=120 and length>=90
-- select title, length from film where length between 90 and 120
-- yukarıdaki iki komut aynı çıktıyı verir

-- select title, length from film where length not between 90 and 120
-- not between belirtilen aralık dışındakileri verir

-- select title, rental_rate, replacement_cost from film where (rental_rate between 2 and 4) and (replacement_cost between 15 and 20) 

-- in komutu
-- select title,length from film where length in(40, 50 ,60)
-- select title, length from film  where length=40 or length=50 or length=60
-- yukarıdaki iki komut aynı çıktıyı verir

-- select title, replacement_cost from film where replacement_cost=10.99 or replacement_cost=12.99 or replacement_cost=16.99
-- select title, replacement_cost from film where replacement_cost in (10.99, 12.99, 16.99)
-- yukarıdaki iki komut aynı çıktıyı verir
-- select title, replacement_cost from film where replacement_cost not in (10.99, 12.99, 16.99)
-- üç değer dışındakileri verir

-- 1)film tablosunda bulunan tüm sütunlardaki verileri replacement cost değeri 12.99 dan büyük eşit ve 16.99 küçük olma koşuluyla sıralayınız ( BETWEEN - AND yapısını kullanınız.)
-- select title, replacement_cost from film where replacement_cost between  12.99 and 16.99
-- 2)actor tablosunda bulunan first_name ve last_name sütunlardaki verileri first_name 'Penelope' veya 'Nick' veya 'Ed' değerleri olması koşuluyla sıralayınız. ( IN operatörünü kullanınız.)
-- select first_name ,last_name from actor where first_name in ('Penelope' , 'Nick' , 'Ed');
-- değer girerken '' kullanılacak dikkat!
-- 3)film tablosunda bulunan tüm sütunlardaki verileri rental_rate 0.99, 2.99, 4.99 VE replacement_cost 12.99, 15.99, 28.99 olma koşullarıyla sıralayınız. ( IN operatörünü kullanınız.)
-- select rental_rate, replacement_cost from film where rental_rate in(0.99, 2.99, 4.99) and replacement_cost in(12.99, 15.99, 28.99)


@@@LIKE, ILIKE@@
-- select * from customer where first_name='Mary'

-- select * from customer where first_name like 'Ma%'
-- first_name kolonu Ma ile başlayıp herhangi bir şekilde devam eden tüm kayıtları verir

-- select * from customer where first_name like 'A%y'
--  baş harfi A son harfi y olan tüm kayıtlar
-- select * from customer where first_name like 'A%' and last_name like '%b'
-- adının baş harfi A ile başlayıp soyadı b ile biten kayıtlar

-- select * from customer where first_name ilike '%A' 
-- select * from customer where first_name ~~* '%A' 
-- ~~* ile ilike aynı işe yarar, ilike ile büyük küçük harfe bakmaksızın çalışır

-- select * from customer where first_name not like 'A%'
-- A ile başlamayan kayıtlar geldi
-- select * from customer where first_name like 'J_'
-- _ yer tutucu olarak çalışıyor ve J ile başlayıp Jo Ji Ja... gibi ismi olan kayıtları gösterir

-- select * from actor where first_name = 'Penelope'
-- adı Penelope olan kayıtlar geldi
-- select * from actor where first_name like 'P%e'
-- select * from actor where first_name ~~ 'P%e'
-- ~~ ile like aynı işe yarar, adı P...e olan tüm kayıtlar geldi
-- select * from actor where first_name like 'T__'
-- Tim Tom kayıtları geldi

-- 1)country tablosunda bulunan country sütunundaki ülke isimlerinden 'A' karakteri ile başlayıp 'a' karakteri ile sonlananları sıralayınız.
-- select country from country where country like 'A%a'
-- 2)country tablosunda bulunan country sütunundaki ülke isimlerinden en az 6 karakterden oluşan ve sonu 'n' karakteri ile sonlananları sıralayınız.
-- select country from country where (length(country))>5 and (country like '%n')
-- 3)film tablosunda bulunan title sütunundaki film isimlerinden en az 4 adet büyük ya da küçük harf farketmesizin 'T' karakteri içeren film isimlerini sıralayınız.
-- select title from film where  (title ilike '%t%t%t%t%')
-- 4)film tablosunda bulunan tüm sütunlardaki verilerden title 'C' karakteri ile başlayan ve uzunluğu (length) 90 dan büyük olan ve rental_rate 2.99 olan verileri sıralayınız.
-- select title, length, rental_rate from film where (title like 'C%') and (length >89) and (rental_rate=2.99)


@@@DISTINCT, COUNT@@@
-- select distinct rental_rate from film
-- rental_rate ler arasında unique olanları bulur
-- select distinct replacement_cost from film
-- replacement_cost lar arasında unique olanları bulur
-- select distinct release_year from film
-- tek bir release_year değeri var (2006)

-- select count(*) from actor where first_name = 'Penelope'
-- where içindeki şartı sağlayan kayıt sayısı
-- select count(*) from actor where first_name like 'A%'
-- where içindeki şartı sağlayan kayıt sayısı

-- select count(*) from actor
-- toplam kaç veri var, birbirinden farklı ya da aynı
-- select distinct first_name from actor
-- isimleri birbirinden farklı olan veriler
-- select count(distinct first_name) from actor
-- isimleri birbirinden farklı olan verilerin sayısı

-- 1)film tablosunda bulunan replacement_cost sütununda bulunan birbirinden farklı değerleri sıralayınız.
-- select distinct replacement_cost from film
-- 2)film tablosunda bulunan replacement_cost sütununda birbirinden farklı kaç tane veri vardır?
-- select count(distinct replacement_cost) from film
-- 3)film tablosunda bulunan film isimlerinde (title) kaç tanesini T karakteri ile başlar ve aynı zamanda rating 'G' ye eşittir?
-- select count(*) from film where title like 'T%' and rating ='G'
-- 4)country tablosunda bulunan ülke isimlerinden (country) kaç tanesi 5 karakterden oluşmaktadır?
-- select count(*) from country where length(country)=5
-- 5)city tablosundaki şehir isimlerinin kaç tanesi 'R' veya r karakteri ile biter?
-- select count(*) from city where city ilike '%R'


@@@ORDER BY@@@
-- select title, length from film order by length 
-- select title, length from film order by length asc
-- iki artan şekilde sıralar ve aynı çıktıyı verir
-- select title, length from film order by length desc
-- azalan şekilde sıralar
-- select title, length from film order by title
-- alfabetik sıraya göre sıralar

-- select title, rental_rate, length from film
-- where title like 'A%'
-- order by rental_rate asc, length desc


@@@LIMIT, OFFSET@@@
-- select * from film limit 20
-- 20 adet film gösterir
-- select title, rental_rate from film where rental_rate =4.99 order by length limit 20
-- select * from film where replacement_cost=14.99 and rental_rate=0.99 order by length desc limit 7
-- select * from country offset 6 limit 10
-- ilk 6 veriyi geçip sonraki 10 veriyi gösterir (7-17 arası)
-- select * from actor where first_name = 'Penelope' order by last_name offset 2 limit 1
-- ...

-- 1)film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en uzun (length) 5 filmi sıralayınız.
-- select title, length from film where title like '%n' order by length desc limit 5
-- 2)film tablosunda bulunan ve film ismi (title) 'n' karakteri ile biten en kısa (length) ikinci(6,7,8,9,10) 5 filmi(6,7,8,9,10) sıralayınız.
-- select title, length from film where title like '%n' order by length desc offset 5 limit 5
-- 3)customer tablosunda bulunan last_name sütununa göre azalan yapılan sıralamada store_id 1 olmak koşuluyla ilk 4 veriyi sıralayınız.
-- select last_name, store_id from customer where store_id ='1' order by last_name desc limit 4


@@@AGGREGATE FUNC.@@@
-- select max(replacement_cost) from film
-- select min(replacement_cost) from film
-- select avg(length) from film
-- length sütunun ortalaması
-- select round(avg(length),3) from film
-- round ile float türündeki değerleri 3 basamak ile sınırladık
-- select sum(rental_rate) from film
-- select max(length), sum(replacement_cost) from film
-- select max(length) from film where rental_rate in (0.99, 2.99)

-- 1)film tablosunda bulunan rental_rate sütunundaki değerlerin ortalaması nedir?
-- select round(avg(rental_rate), 3) from film
-- 2)film tablosunda bulunan filmlerden kaç tanesi 'C' karakteri ile başlar?
-- select count(*) from film where title like 'C%'
-- 3)film tablosunda bulunan filmlerden rental_rate değeri 0.99 a eşit olan en uzun (length) film kaç dakikadır?
-- select max(length) from film where rental_rate = 0.99 
-- 4)film tablosunda bulunan filmlerin uzunluğu 150 dakikadan büyük olanlarına ait kaç farklı replacement_cost değeri vardır?
-- select count(distinct replacement_cost) from film where length>150


@@@GROUP BY@@@
-- select rental_rate, count(*), max(length) from film group by rental_rate
-- select rating, count(*)  from film group by rating
-- select min(length), replacement_cost from film group by replacement_cost 
-- select replacement_cost, rental_rate, min(length) from film group by replacement_cost, rental_rate
-- lengthi minimum olan verinin replacement_cost, rental_rate değerleri

-- select replacement_cost, rental_rate, min(length) from film group by replacement_cost, rental_rate order by replacement_cost, rental_rate desc
-- replacement değeri artan, rental değeri azalan şekilde sıralandı


@@@HAVİNG@@@
-- select rental_rate, count(*) from film group by rental_rate having count(*)>325
-- rental_rate e göre gruplandırılmış verilere koşul ekler
-- where satır bazlı gruplama, having sütun bazlı gruplama

-- select staff_id, count(amount) from payment group by staff_id having count(*)>7300
-- select customer_id, sum(amount) from payment group by customer_id having sum(amount)>100 order by sum(amount) desc

-- 1)film tablosunda bulunan filmleri rating değerlerine göre gruplayınız.
-- select rating from film group by rating
-- 2)film tablosunda bulunan filmleri replacement_cost sütununa göre grupladığımızda film sayısı 50 den fazla olan replacement_cost değerini ve karşılık gelen film sayısını sıralayınız.
-- select replacement_cost, count(*) from film group by replacement_cost having count(*)>50
-- 3)customer tablosunda bulunan store_id değerlerine karşılık gelen müşteri sayılarını nelerdir? 
-- select store_id, count(*) from customer group by store_id
-- 4)city tablosunda bulunan şehir verilerini country_id sütununa göre gruplandırdıktan sonra en fazla şehir sayısı barındıran country_id bilgisini ve şehir sayısını paylaşınız.
-- select country_id, count(city) from city group by country_id order by count desc limit 1


@@@ALIES(AS), CONCAT@@@
-- select first_name as isim, last_name as soyisim from customer
-- select first_name isim, last_name soyisim from customer
-- select first_name "isim test", last_name "soyisim test" from customer

-- select count(*) as "aktor sayısı" from actor
-- as ailas'ın kısaltması ve geçisi isim verir

-- select first_name, last_name from actor
-- select concat(first_name,' ',last_name) as "İsim ve Soyisim" from actor
-- concat fonk ile ad ve soyad birleştirildi as ile de geçici isim verildi.



@@@@@ TABLOLARLA ÇALIŞMAK @@@@@
@@@TABLO OLUŞTURMAK@@@
-- create table author(
-- 	id serial primary key,
-- 	first_name varchar(50) not null,
-- 	last_name varchar(50) not null,
-- 	email varchar(100),
-- 	birthday date
-- )

-- insert into author(first_name, last_name, email, birthday)
-- values
-- 	('Sabahattin','Ali','ali@gmail.com','1925-10-10'),
-- 	('Halide Edip','Adıvar','halideedip@gmail.com','1929-7-19'),
-- 	('Reşat Nuri','Güntekin','reşat@gmail.com','1938-8-18'),
-- 	('Nihal','Atsız','nihalatsız@gmail.com','1932-9-21')

-- create table author2 (like author)
-- tablonun içeriğini değil, yalnızca taslağını yani kolon yapılarını aldı
-- insert into author2 select * from author where first_name = 'Sabahattin'
-- author tablosundan author2 tablosuna veri kopyaladık

-- create table author3 as select * from author
-- author tablosundaki veriler ve kolon yapısının aynıları author3 tablosu oluşturulup kopyalandı

-- drop table author4
-- author4 does not exists hatası verir
-- drop table if exists author4
-- if exists yapısı kullanılabilir

-- drop table author3
-- drop table author2
-- oluşturulan tablolar silindi


@@@VERİLERİ GÜNCELLEMEK@@@
-- mockaroo sitesi ile random veri üretilip author tablosuna çekildi

-- update author set first_name = 'Emrah Safa', last_name='Gurkan', email ='emrah@gmail.com', birthday = ' 1975-11-11' where id =7
-- ile id'si 7 olan veriler güncellendi ve tablonun altına eklendi

-- update author
-- set first_name = 'XXXX',
-- 	last_name = 'YYYY'
-- where first_name like 'A%'
-- ile adı A ile başlayan yazalar güncellendi, güncellenen veriler tablonun altına eklenir

-- update author
-- set last_name='Updated'
-- where first_name = 'Gabrila'
-- returning *
-- adı Gabrila olan verinin soyadı Updated diye güncellendi ve returning * ile select edildi

-- delete from author where id = 6 
-- delete from author where id>15 returning *

-- 1)test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.
-- create table employee( 
-- 	id integer,
-- 	name varchar(50),
-- 	birthday date,
-- 	email varchar(100)
-- )
-- 2)Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.
-- select * from employee
-- 3)Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.
-- update employee
-- set name = 'Furkan', birthday = '1999-09-15', email = 'furkan@gmail.com'
-- where name like 'Penny%';
-- update employee set name = 'Nurşinsu Mağın', birthday = '2000-06-03', email = 'beybilotam@gmail.com' where name ='Cheslie Bulle'
-- update employee set name = 'Onu Çoook Seviyorumm', birthday = '2001-07-04', email = 'bayılıyorum@gmail.com' where name like 'Blythe%'
-- 4)Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.
-- delete from employee where name ilike 'a%'
-- delete from employee where name ilike 'd%' returning *