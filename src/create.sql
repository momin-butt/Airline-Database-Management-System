DROP DATABASE Flights;
CREATE DATABASE Flights;
USE Flights;

CREATE TABLE PASSENGER (

	cust_id char(11) NOT NULL,
	name varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	age INT NOT NULL,
	address varchar(255) NOT NULL,
	gender char(1) NOT NULL,
	nationality varchar(255) NOT NULL,
	contact varchar(11) NOT NULL
	-- username varchar(20) NOT NULL,
	-- password varchar(20) NOT NULL
);


CREATE TABLE BOOKING(

	booking_id char(5) NOT NULL,
	cust_id char(11) NOT NULL,
	flight_id char(5) NOT NULL,
	class varchar(20) NOT NULL,
	fare varchar(15) NOT NULL

);

CREATE TABLE FLIGHT(

	flight_id char(5) NOT NULL,
	depart_time varchar(20) NOT NULL,
	arrive_time varchar(20) NOT NULL,
	depart_date varchar(20) NOT NULL,
	arrive_date varchar(20) NOT NULL,
	depart_aircode char(20) NOT NULL,
	arrive_aircode char(20) NOT NULL,
	airplane_code varchar(20) NOT NULL,
	status varchar(20) NOT NULL,
	fare varchar(15) NOT NULL

);


CREATE TABLE AIRPLANE(

	airplane_code varchar(20) NOT NULL,
	airline_id varchar(6) NOT NULL,
	capacity INT NOT NULL,
	model varchar(255) NOT NULL
);

-- CREATE TABLE ADMINISTRATOR(

-- 	username varchar(20) NOT NULL,
-- 	password varchar(20) NOT NULL 
-- );


ALTER TABLE PASSENGER
	ADD PRIMARY KEY(cust_id);
ALTER TABLE BOOKING
	ADD PRIMARY KEY(booking_id);
ALTER TABLE FLIGHT
	ADD PRIMARY KEY(flight_id);
ALTER TABLE AIRPLANE
	ADD PRIMARY KEY(airplane_code);
-- ALTER TABLE ADMINISTRATOR
-- 	ADD PRIMARY KEY(username);



-- ALTER TABLE BOOKING
-- 	MODIFY booking_id INT NOT NULL AUTO_INCREMENT;
-- ALTER TABLE FLIGHT
-- 	MODIFY flight_id INT NOT NULL AUTO_INCREMENT;


ALTER TABLE BOOKING
	ADD FOREIGN KEY(cust_id) REFERENCES PASSENGER(cust_id),
 	ADD FOREIGN KEY(flight_id) REFERENCES FLIGHT(flight_id) ON DELETE CASCADE;
ALTER TABLE FLIGHT
 	ADD FOREIGN KEY(airplane_code) REFERENCES AIRPLANE(airplane_code);




