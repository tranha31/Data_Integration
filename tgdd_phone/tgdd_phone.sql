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
  Ram varchar(100) NOT NULL,
  Sim varchar(100) DEFAULT NULL,
  Pin varchar(100) DEFAULT NULL,
  ImageUrl text DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

DELIMITER $$

--
-- Create procedure `Proc_Insert_Phone`
--
CREATE DEFINER = 'root'@'localhost'
PROCEDURE Proc_Insert_Phone (IN $Company varchar(100), IN $Name varchar(255), IN $Memory int, IN $Color varchar(100), IN $OriginPrice int, IN $DiscountPrice int, IN $DiscountRate float, IN $Screen varchar(255), IN $OperatingSystem varchar(255), IN $FrontCamera varchar(255), IN $BehindCamera varchar(255), IN $Chip varchar(255), IN $Ram varchar(100), IN $Sim varchar(100), IN $Pin varchar(100), IN $ImageUrl text)
BEGIN
  INSERT INTO mobiphone (RefID
  , Company
  , Name
  , Memory
  , Color
  , OriginPrice
  , DiscountPrice
  , DiscountRate
  , Screen
  , OperatingSystem
  , FrontCamera
  , BehindCamera
  , Chip
  , Ram
  , Sim
  , Pin
  , ImageUrl)
    VALUES (UUID(), $Company, $Name, $Memory, $Color, $OriginPrice, $DiscountPrice, $DiscountRate, $Screen, $OperatingSystem, $FrontCamera, $BehindCamera, $Chip, $Ram, $Sim, $Pin, $ImageUrl);
END
$$

DELIMITER ;


DELIMITER $$

--
-- Create procedure `Proc_Update_Phone`
--
CREATE DEFINER = 'root'@'localhost'
PROCEDURE Proc_Update_Phone (IN $RefID char(36), IN $Company varchar(100), IN $Name varchar(255), IN $Memory int, IN $Color varchar(100), IN $OriginPrice int, IN $DiscountPrice int, IN $DiscountRate float, IN $Screen varchar(255), IN $OperatingSystem varchar(255), IN $FrontCamera varchar(255), IN $BehindCamera varchar(255), IN $Chip varchar(255), IN $Ram varchar(100), IN $Sim varchar(100), IN $Pin varchar(100), IN $ImageUrl text)
BEGIN
  UPDATE mobiphone
  SET Company = $Company,
      Name = $Name,
      Memory = $Memory,
      Color = $Color,
      OriginPrice = $OriginPrice,
      DiscountPrice = $DiscountPrice,
      DiscountRate = $DiscountRate,
      Screen = $Screen,
      OperatingSystem = $OperatingSystem,
      FrontCamera = $FrontCamera,
      BehindCamera = $BehindCamera,
      Chip = $Chip,
      Ram = $Ram,
      Sim = $Sim,
      Pin = $Pin,
      ImageUrl = $ImageUrl
  WHERE RefID = $RefID
  ;
END
$$

DELIMITER ;

CREATE TABLE phone (
  RefID char(36) NOT NULL DEFAULT '',
  Name varchar(255) DEFAULT NULL,
  Company varchar(100) DEFAULT NULL,
  OriginPrice int DEFAULT NULL,
  DiscountPrice int DEFAULT NULL,
  DiscountRate float DEFAULT NULL,
  Color varchar(100) DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

CREATE TABLE phoneinformation (
  RefID char(36) NOT NULL DEFAULT '',
  PhoneID char(36) DEFAULT NULL,
  Memory int DEFAULT NULL,
  Chip varchar(255) DEFAULT NULL,
  Ram varchar(100) DEFAULT NULL,
  Sim varchar(100) DEFAULT NULL,
  Pin varchar(100) DEFAULT NULL,
  FrontCamera varchar(255) DEFAULT NULL,
  BehindCamera varchar(255) DEFAULT NULL,
  Screen varchar(255) DEFAULT NULL,
  OperatingSystem varchar(255) DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE phoneinformation
ADD CONSTRAINT FK_PhoneInformation_PhoneID FOREIGN KEY (PhoneID)
REFERENCES phone (RefID);

CREATE TABLE phoneimage (
  RefID char(36) NOT NULL DEFAULT '',
  PhoneID char(36) DEFAULT NULL,
  ImageUrl text DEFAULT NULL,
  PRIMARY KEY (RefID)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_0900_ai_ci;

--
-- Create foreign key
--
ALTER TABLE phoneimage
ADD CONSTRAINT FK_PhoneImage_PhoneID FOREIGN KEY (PhoneID)
REFERENCES phone (RefID);

