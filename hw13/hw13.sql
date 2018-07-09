create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select a.name, b.size 
   from dogs as a, sizes as b
   where a.height>b.min and a.height<=b.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select p.child
   from parents as p, dogs as d
   where p.parent=d.name
   order by d.height desc;

-- Sentences about siblings that are the same size
create table sentences as
with siblings as (select a.child as first,b.child as second
   from parents as a, parents as b
   where a.parent=b.parent and a.child<b.child)
  select siblings.first || ' and ' || siblings.second 
         || ' are ' || size_of_dogs_a.size || ' siblings'
   from siblings, size_of_dogs as size_of_dogs_a, size_of_dogs as size_of_dogs_b
   where siblings.first=size_of_dogs_a.name and siblings.second=size_of_dogs_b.name 
         and size_of_dogs_a.size=size_of_dogs_b.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  select a.name || ', ' || b.name || ', ' || c.name || ', ' || d.name ,
         a.height+b.height+c.height+d.height as total_height
   from dogs as a, dogs as b, dogs as c, dogs as d
   where a.height<b.height and b.height<c.height and c.height<d.height
         and total_height>=170
   order by total_height;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
with
    grandparents(grandog, grandpup) as (
    select a.parent, b.child
     from parents as a, parents as b 
     where a.child=b.parent),
    ancestors(ancestor, descendent) as (
     select grandog, grandpup from grandparents union
     select ancestor, child from ancestors, parents
       where parent=descendent),
    relations(first, second) as (
     select ancestor, descendent from ancestors union
     select descendent, ancestor from ancestors)
  select first, second
   from relations, dogs as c, dogs as d
   where c.name=first and d.name=second
   order by c.height-d.height;


create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
    select a.n, count(*) as count
     from ints as a, ints as b
      where a.n>=b.n and a.n % b.n =0
      group by a.n;

create table primes as
    select n from divisors
     where count=2;
