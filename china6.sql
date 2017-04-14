--
-- Description: for logistics server infomations China6
--
-- Author: 		ninja
--
-- Date:		created by 2017-04-11 
--

DROP DATABASE IF EXISTS China6_DB;

CREATE DATABASE China6_DB;

USE China6_DB;


-- for car resource infomation 
CREATE TABLE car_desc
(
	id 				int NOT NULL auto_increment,
	carNum          text,
	carType			text,
	startLocation	text,
	endLocation     text,
	midLocation  	text,
	releaseTime		text,
	driveTime		text,
	price			text,
	comments		text,
	carLen			text,
	carLoad			text,
	carAddr			text,
	carStatus		text,
	carContacts		text,
	phoneNum		text,
	carID			text,


	PRIMARY KEY (id)
)DEFAULT CHARSET=utf8;
