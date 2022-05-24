-- 
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE tgdd_phone;

--
-- Create table `mobiphone`
--
CREATE TABLE mobiphone (
  RefID char(36) NOT NULL DEFAULT '',
  Company varchar(100) NOT NULL DEFAULT '',
  Name varchar(255) NOT NULL DEFAULT '',
  Memory int NOT NULL,
  Color varchar(100) DEFAULT NULL,
  OriginPrice int DEFAULT NULL,
  DiscountPrice int DEFAULT NULL,
  DiscountRate float DEFAULT NULL,
  Screen varchar(255) DEFAULT NULL,
  OperatingSystem varchar(255) NOT NULL DEFAULT '',
  FrontCamera varchar(255) DEFAULT NULL,
  BehindCamera varchar(255) DEFAULT NULL,
  Chip varchar(255) NOT NULL DEFAULT '',
  Ram int NOT NULL,
  Sim varchar(100) DEFAULT NULL,
  Pin varchar(100) DEFAULT NULL,
  ImageUrl text DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

CREATE DEFINER = 'root'@'localhost'
PROCEDURE tgdd_phone.Proc_Insert_Phone(IN $RefID CHAR(36), IN $Company VARCHAR(100), IN $Name VARCHAR(255), IN $Memory INT, IN $Color VARCHAR(100), IN $OriginPrice INT, IN $DiscountPrice INT, IN $DiscountRate FLOAT, IN $Screen VARCHAR(255), IN $OperatingSystem VARCHAR(255), IN $FrontCamera VARCHAR(255), IN $BehindCamera VARCHAR(255), IN $Chip VARCHAR(255), IN $Ram INT, IN $Sim VARCHAR(100), IN $Pin VARCHAR(100), IN $ImageUrl text)
BEGIN
  INSERT INTO mobiphone
  (
    RefID
   ,Company
   ,Name
   ,Memory
   ,Color
   ,OriginPrice
   ,DiscountPrice
   ,DiscountRate
   ,Screen
   ,OperatingSystem
   ,FrontCamera
   ,BehindCamera
   ,Chip
   ,Ram
   ,Sim
   ,Pin
   ,ImageUrl
  )
  VALUES
  (
    UUID() 
   ,$Company 
   ,$Name
   ,$Memory
   ,$Color
   ,$OriginPrice
   ,$DiscountPrice
   ,$DiscountRate
   ,$Screen
   ,$OperatingSystem
   ,$FrontCamera
   ,$BehindCamera
   ,$Chip
   ,$Ram
   ,$Sim
   ,$Pin
   ,$ImageUrl
  );
END;


CREATE DEFINER = 'root'@'localhost'
PROCEDURE tgdd_phone.Proc_Update_Phone(IN $RefID CHAR(36), IN $Company VARCHAR(100), IN $Name VARCHAR(255), IN $Memory INT, IN $Color VARCHAR(100), IN $OriginPrice INT, IN $DiscountPrice INT, IN $DiscountRate FLOAT, IN $Screen VARCHAR(255), IN $OperatingSystem VARCHAR(255), IN $FrontCamera VARCHAR(255), IN $BehindCamera VARCHAR(255), IN $Chip VARCHAR(255), IN $Ram INT, IN $Sim VARCHAR(100), IN $Pin VARCHAR(100), IN $ImageUrl text)
BEGIN
  UPDATE mobiphone 
  SET
   Company = $Company 
   ,Name = $Name 
   ,Memory = $Memory 
   ,Color = $Color
   ,OriginPrice = $OriginPrice
   ,DiscountPrice = $DiscountPrice
   ,DiscountRate = $DiscountRate
   ,Screen = $Screen
   ,OperatingSystem = $OperatingSystem
   ,FrontCamera = $FrontCamera
   ,BehindCamera = $BehindCamera
   ,Chip = $Chip
   ,Ram = $Ram
   ,Sim = $Sim
   ,Pin = $Pin
   ,ImageUrl = $ImageUrl
  WHERE
    RefID = $RefID
  ;
END;

