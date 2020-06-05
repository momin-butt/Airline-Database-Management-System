

INSERT INTO AIRPLANE (airplane_code,airline_id,capacity,model) VALUES
			('7TWHM','001',500,'Alaska Airlines Boeing'),
			('A1697','014',250,'Air Canada Boeing 7879 1/200'),
			('N16100','055',300,'American Airlines Boeing 707'),
			('CH06','057',320,'Boeing 747100 Rollout Livery 1/200'),
			('L916','139',750,'British Airways Boeing 747400 1/400'),
			('K2729','205',220,'Delta Airlines Boeing 737800 1/130'),
			('A1310','257',550,'Hawaiian Airlines Airbus A330, New Livery 1/400'),
			('A2708','260',100,'Lockheed L1049SG TWA Super Connie 1/100'),
			('B11120','288',180,'Pan Am Boeing 747100 1/200'),
			('UP72859','555',450,'Postage Stamp Boeing 314 Pan Am 1/350'),
			('NAF033','656',260,'Westjet Boeing 737 MAX8 1/130');

INSERT INTO FLIGHT (flight_id,depart_time,arrive_time,depart_date,arrive_date,depart_aircode,arrive_aircode,airplane_code,status,fare) VALUES 
			('00280','08:00:00','12:00:30','01/02/2017','02/02/2017','ATL','KATL','7TWHM','Landed','$1200'),
			('00281','02:00:00','09:00:30','01/03/2017','02/03/2017','PEK','FRA','A1697','Available','$1750'),
			('00282','04:00:00','07:20:30','02/04/2017','03/04/2017','LAX','PVG','N16100','Taking Off','$1500'),
			('00283','05:00:00','11:35:30','03/05/2017','04/05/2017','HND','WSSS','CH06','Landed','$2200'),
			('00284','10:00:00','12:00:30','03/02/2017','10/02/2017','ATL','KATL','L916','Taking Off','$1000'),
			('00285','03:00:00','01:00:30','05/07/2017','06/07/2017','ORD','BKKK','K2729','Available','$7850'),
			('00286','08:40:00','01:10:30','06/08/2017','06/08/2017','PVG','KUL','A1310','Taking Off','$4300'),
			('00287','08:20:00','06:50:30','07/09/2017','08/09/2017','HKG','JFK','A2708','Landed','$5000'),
			('00288','04:50:00','04:20:30','08/10/2017','09/10/2017','CDG','ATL','B11120','Taking Off','$3450'),
			('00289','11:00:00','02:20:30','09/11/2017','10/11/2017','DFW','SZX','UP72859','Landed','$7200'),
			('00290','12:30:00','03:40:30','21/12/2017','23/12/2017','CAN','BCN','NAF033','Available','$6500');

INSERT INTO PASSENGER (cust_id,name,email,age,address,gender,nationality,contact) VALUES
		    ('35202010101','Mahad','mahad123@gmail.com',24,'LUMS','M','English','03008411111'),
			('35202123456','Momin','monie@gmail.com',21,'Garden Town','M','French','03008421111'),
			('35202537503','Mehreen','meenuxyz@gmail.com',23,'Faisal Town','F','Arabian','03008455555'),
			('35202438924','Mujtaba','muji123@gmail.com',28,'LUMS','M','Lebannese','03218289480'),
			('35202193297','Omer','chowness987@gmail.com',22,'FAST','M','Spanish','03147658493'),
			('35202987654','Punnal','nallzzz@gmail.com',20,'Garden Town','M','Indian','03426541234'),
			('35202134010','Ahmed','mayooo@gmail.com',19,'Model Town','M','Iranian','03004569081'),
			('35202403248','Ayaz','izoo4321@gmail.com',21,'LUMS','M','Egyptian','03111111111'),
			('35202110325','Mustafa','mushu999@gmail.com',24,'UET','M','English','03228777777'),
			('35202113843','Waniya','wanuuu786@gmail.com',23,'PAC','F','Italian','03087234544'),
			('35202345349','Usama','uziii69@gmail.com',19,'Wapda Town','M','Danish','03005512121');

INSERT INTO BOOKING (booking_id,cust_id,flight_id,class,fare) VALUES 
			('12345','35202010101','00280','Business','$1200'),
			('12346','35202123456','00281','Economy','$1750'),
			('12347','35202537503','00282','VIP','$1500'),
			('12348','35202438924','00283','Economy','$2200'),
			('12349','35202193297','00284','Business','$1000'),
			('12350','35202987654','00285','VIP','$7850'),
			('12351','35202134010','00286','Economy','$4300'),
			('12352','35202403248','00287','Business','$5000'),
			('12353','35202010101','00288','VIP','$3450'),
			('12354','35202113843','00289','VIP','$7200'),
			('12355','35202345349','00290','Business','$6500');






