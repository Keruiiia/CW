/*
You are given a denormalized database table called world_population with columns id, country, year, and population. The table contains population data for various countries over the years.

Your task is to write a SQL query that finds the top 5 countries with the highest population increase strictly between the years 2000 and 2020, inclusive. The result should show the country name and the population increase in millions, rounded to 2 decimal places. The query should group the results by country and sort them in descending order based on the population increase.

Notes:
population_increase should be obtained by dividing the result by 1,000,000 to convert the number to millions, rounding it to 2 decimal places and afterwards by adding an abbreviation for millions, "M", to the end of result.
for the sample test is used static actual data taken from the United Nations, for the final solution - random test.
for this task there is no data missing, so you don't need to take into account that data for a year for some countries may be lacking
to avoid ambiguety: by "increase" is simply meant "population at year y1 - population at year y2".
Schema:
world_population table:
Column      | Type          | Modifiers
------------+---------------+-----------
id          | integer       | not null
country     | varchar(255)  | not null
population  | bigint        | not null
year        | smallint      | not null
Desired Output
The desired output should look like this:

country      | population_increase
-------------+-------------------+
China        | 436.55 M          |
India        | 195.85 M          | 
*/

with stats as (
  select country,
     sum(case year when 2020 then population when 2000 then -population end) as increase
  from world_population
  group by country
)
select country,
       cast(round(increase / 1e6, 2) as text) || ' M' population_increase
from stats
order by increase desc
limit 5