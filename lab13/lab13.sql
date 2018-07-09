.read data.sql

-- Q1
create table flight_costs as
 with temp_costs(day, cur, prev) as (
  select 1, 20, 0 union
  select 2, 30, 20 union
  select 3, 40, 30 union
  select day+1, (cur+prev)/2+(day+1)%7*5, cur from temp_costs
  where day<25 and day>2)
 select day as day, cur as price from temp_costs;

-- Q2
create table schedule as
 with temp_arrive(route,now,total, trans) as (
  select departure || ', ' || arrival, arrival, price, 0 from flights
   where departure = 'SFO' union
  select route || ', ' || arrival, arrival, total+price, trans+1
   from flights, temp_arrive
   where temp_arrive.now=flights.departure and trans<1)
  select route, total from temp_arrive
   where now='PDX'
   order by total;

-- Q3
create table shopping_cart as
 with cart(list, last, budget) as (
   select item, price, 60-price from supermarket where price<=60 union
   select list || ', ' || item, price, budget-price from supermarket, cart
    where price>=last and budget>=price)
  select list, budget from cart
   order by budget, list;

-- Q4
create table number_of_options as
  select count(distinct meat) from main_course;

-- Q5
create table calories as
  select count(*) from main_course as m, pies as p where m.calories+p.calories<2500;

-- Q6
create table healthiest_meats as
  select meat, min(m.calories+p.calories) as calories
   from main_course as m, pies as p
   group by meat having max(m.calories+p.calories)<3000;

-- Q7
create table average_prices as
  select category, avg(MSRP) from products
   group by category;

-- Q8
create table lowest_prices as
  select item, store, min(price) from inventory
   group by item;

-- Q9
create table shopping_list as
  select l.item as name, store from products as p, lowest_prices as l
   where l.item=p.name
   group by category having min(MSRP/rating);

-- Q10
create table total_bandwidth as
with temp(name, Mbs) as (
   select shopping.name, stores.Mbs from shopping_list as shopping, stores
    where shopping.store=stores.store)
  select sum(Mbs) from temp;
