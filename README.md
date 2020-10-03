# scrapy-bot

This project was designed to apply my skills in web crawling (Selenium) and web scraping (Scrapy). 

Concept: 
  - Scraping Imdb's Most popular Movie on (https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm) and then storing them on a database. 
  - Then we will get the movies that have 8+ rating in that list, which will be downloaded on YTS (https://yts.mx/)
  - It is important to note that this project has no unethical intent but was set as an exercise only.
  
 Language used - Python & Mysql (database management)
 Framework 
  - Scrapy (web scraping)
  - Selenium (web crawling)
  - SqlAlchemy (ORM - database request handling)
  
How it works?
  1. Scrapy will scrap Imdb and then get all the movies on https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm
  2. Scrapy will use SqlAchemy to store the data in sql
  3. Once done, SqlAlchemy will request Mysql to send the data colloected 
  4. Selenium will use the same data to download the torrent file of any movie that has a rating above 8
  
It is important to note that I could have filtered the information from start, which could have avoided us to store 100 entries. But I wanted to have all of them so that I can go throug the list anyway in the future.

Very interesting project which helepd to master the concept and OOP, inheritance and other advanced python tools relating to web scraping.
