CREATE DATABASE integration_phone
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

-- 
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE integration_phone;

--
-- Create table `phone`
--
CREATE TABLE phone (
  RefID char(36) NOT NULL DEFAULT '',
  PhoneName varchar(500) DEFAULT NULL,
  Price int DEFAULT NULL,
  Image text DEFAULT NULL,
  Color char(20) DEFAULT NULL,
  Memory int DEFAULT NULL,
  Ram int DEFAULT NULL,
  Chip varchar(255) DEFAULT NULL,
  FrontCamera varchar(500) DEFAULT NULL,
  BehindCamera varchar(500) DEFAULT NULL,
  OperationSystem varchar(255) DEFAULT NULL,
  Screen varchar(255) DEFAULT NULL,
  IdPhone char(20) DEFAULT NULL,
  Producer char(20) DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create table `referencephone`
--
CREATE TABLE referencephone (
  RefID char(36) NOT NULL DEFAULT '',
  ReferenceID char(36) NOT NULL DEFAULT '',
  PhoneName varchar(500) DEFAULT NULL,
  Price int DEFAULT NULL,
  Image text DEFAULT NULL,
  Color char(20) DEFAULT NULL,
  Memory int DEFAULT NULL,
  Ram int DEFAULT NULL,
  Chip varchar(255) DEFAULT NULL,
  FrontCamera varchar(500) DEFAULT NULL,
  BehindCamera varchar(500) DEFAULT NULL,
  OperationSystem varchar(255) DEFAULT NULL,
  Screen varchar(255) DEFAULT NULL,
  IdPhone char(20) DEFAULT NULL,
  Producer char(20) DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE referencephone
ADD CONSTRAINT FK_ReferencePhone_ReferenceID FOREIGN KEY (ReferenceID)
REFERENCES phone (RefID);