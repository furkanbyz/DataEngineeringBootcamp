-- @@@@@ SQL DAY 1 @@@@@ 
-- *select first_name, salary, salary*12 as salary per a year from hr.employees
-- int türündeki kolonlara işlem yapılıp yeni kolon gibi yazdırılabilir

-- *select last_name, hire_date, hire_date+30 from hr.employees 
-- date türündeki değerler çarpılamaz ama bu şekilde gün eklenebilir

-- *select 6*8, sysdate from dual 
-- *select sysdate-hire_date from hr.employees 
-- *select 'Hoş geldiniz'  "Kolon" from dual 
-- from dual ekrana yazdırmak için kullanılabilir
-- sysdate anlık tarihi verir

-- *select sysdate, round(sysdate-hire_date, 3)   "Day of Working" from hr.employees 
-- as yerine iki boşluk bırakıp "" içine alındı. Alies uygulandı 

-- *select employee_id, first_name || last_name  "Adı Soyadı" from hr.employees 
-- *select employee_id, first_name ||' '|| last_name  "Adı Soyadı" from hr.employees 
-- *select employee_id || 'Merhaba' || salary from hr.employees 
-- || ile iki kolon birleştirilebilir. Concat uygulandı

-- *select distinct department_id from hr.employees
-- distinct unique değerleri verir

-- *describe hr.departments
-- ile tablo bilgilerine bakılabilir




-- @@@@@ SQL DAY 2 @@@@@ 
-- *select * from hr.employees where employee_id=100
-- *select * from hr.employees where last_name='King'
-- *select * from hr.employees where last_name like 'Ki%' 
-- *select first_name, salary from hr.employees where first_name like 'S____' 
-- *select first_name, salary from hr.employees where first_name like 'S%e_'
-- *select * from hr.employees where salary>10000 and job_id like '%MAN%' 
-- çeşitli where filtreleri

-- *select last_name, salary from hr.employees where salary between 2500 and 3500 
-- between ile arasındaki değerleri alır

-- *select last_name, salary from hr.employees where manager_id in (100, 101, 102) 
-- in ile belirtilen değerleri alır

-- *select last_name, manager_id, salary from hr.employees where manager_id is null
-- manager_id kolonu null olan değerleri getirir

-- *select last_name, manager_id, salary from hr.employees where manager_id is not null 
-- manager_id kolonu null olmayan değerleri getirir

-- *select * from hr.employees order by 1
-- *select * from hr.employees order by 2
-- order by 1,2,3 ile sırası verilen kolonları sıralar

-- *select * from hr.employees order by employee_id
-- *select last_name, salary, department_id from hr.employees order by department_id, salary 
-- order by kullanım örnekleri




-- @@@@@ SQL DAY 3 @@@@@ 
-- *select * from hr.employees where lower(last_name) = 'king'
-- *select * from hr.employees where upper(last_name) = 'KING' 
-- db'deki kayıtların büyük küçük harfinden emin değilsek upper lower şeklinde kendimiz belirterek filtreleyebiliriz

-- *select concat(concat(last_name, '''s job category is '), job_id) as "Job" from hr.employees where substr(job_id,4) = 'REP' 
-- iç içe concat metodu kullanılabilir
-- substr ile job_id kolonunun 4. indexinden sonra REP içeren verileri getirir

-- *select last_name, substr(last_name,1,3) from hr.employees 
-- ile baştan 3.index dahil olacak şekilde işlem yapar

-- *select employee_id, concat(first_name,last_name) as "NAME", length(last_name), instr(last_name, 'a') as "Contains 'a'?" from hr.employees where substr(last_name, -1, 1) = 'n'
-- instr ile last_name kolonunda a içeren kayıtları getirir
-- yukarıdaki gibi length değeri alınabilir
-- where kısmındaysa last_name kolonunun son indexi n olan değerleri filtreler

-- *select last_name, upper(concat(substr(last_name,1,8),'_us')) from hr.employees 
-- 8.indexe kadar olan kısım ile _us'u concat eder ve upper ile büyük harflerler yazdırır

-- *select round(45.923,2), round(45.926,0), round(45.923,-1) from dual
-- *select trunc(45.923,2), trunc(45.926,0), trunc(45.923,-1) from dual
-- yuvarlamalar trunc ve round ile yapılabilir, farkına bakılmalı!

-- *select last_name, hire_date from hr.employees where hire_date< '01-FEB-2008' 
-- db'nin tarih formatına bakılarak filtreleme işlemleri yapılabilir




-- @@@@@ SQL DAY 4 @@@@@ 
-- *select sysdate, sessiontimezone, current_date, current_timestamp from dual
-- sysdate anlık tarihi verir
-- sessiontimezone dbnin bağlı olduğu zaman aralığını verir
-- current_date de anlık tarihi verir 
-- current_timestamp ayrıntılı saat ve tarih bilgilerini verir

-- *select last_name, (sysdate- hire_date), (sysdate-hire_date)/7 as weeks from hr.employees
-- tarihler arasında bu tarz işlemler yapılabilir
-- (sysdate- hire_date) çıktısı gün sayısı cinsinden olur

-- *select employee_id, last_name, months_between(sysdate, hire_date) tenure, add_months(hire_date, 6) review, next_day(hire_date, 'FRIDAY'), last_day(hire_date) from hr.employees
-- months_between(sysdate, hire_date) aradaki ay sayısını verir
-- add_months(hire_date, 6) hire_date kolonuna 6 ay ekler
-- next_day(hire_date, 'FRIDAY') hire_date tarihinden sonraki ilk cuma gününün tarihini verir
-- last_day(hire_date) hire_date ayının son gününün tarihini verir

-- *... where months_between(sysdate,hire_date)<750 
-- işe alınma tarihiyle, anlık tarih arasındaki ay farkının 750den küçük olduğu durumlar

-- *select last_name, to_char(hire_date, 'fmDD Month YYYY') as Hiredate from hr.employees
-- to_char istenilen formatta tarihi yazdırmak için kullanıldı
-- fm ile DDnin başındaki sıfırlar silinir
-- Month yerine MM, YYYY yerine Year yazılabilir...
-- MM yerine Month denenebilir, ay yıl gün bildileri arasına ,- konulabilir , 'fmDD-MM,YYYY' 
-- to_char diye aratarak ayrıntılara ulaşılabilir

-- *select last_name Surname, to_char(salary, '99,999,99') from hr.employees 
-- salary kolonundaki maaş değerinin formatı belirlendi
-- to_char(salary, 'l99,999,99') ile local aren'nın para birimi otomatik eklenir
-- to_char(salary, '$99,999,99') şeklinde farklı para birimleri kullanılabilir

-- *select last_name, to_char(hire_date, 'YYYY') as "YIL" from hr.employees where hire_date < to_date('01.02.2005','DD.MM.YYYY') 
-- to_date ile db'nin tarih formatından bağımsız bir şekilde tarih bilgisi girilir ve bu şekilde işlem yapılır, db'nin tarih formatını bilmeye gerek yok

-- *** TO_CHAR ekrana yazdırmak için, TO_DATE ise sadece işlem yapmak için kullanılır.
