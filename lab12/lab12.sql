.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  select seven, denero from students;

CREATE TABLE smallest_int AS
  select time, smallest from students
   where smallest>8
   order by smallest
   limit 20;

CREATE TABLE greatstudents AS
  select a.date, a.number, a.pet, b.color, a.color
    from sp16students as a, students as b
    where a.date=b.date and a.number=b.number and a.pet=b.pet;

CREATE TABLE sevens AS
  select students.seven from students, checkboxes
   where students.time=checkboxes.time and students.number=7 and checkboxes.'7'='True';

CREATE TABLE matchmaker AS
  select a.pet,a.song,a.color,b.color
   from students as a, students as b
   where a.time<>b.time and a.pet=b.pet and a.song=b.song;
