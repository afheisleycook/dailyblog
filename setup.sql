-- sets up db for log -- 
create database dailyblog;
create user dailyblog;
grant all to "dailylog"  at dailylog.*;
create table posts(post_id integery primary key autoincrement,post_title varchar(30),post_description varchar(100), post_tag varchar(10) );
