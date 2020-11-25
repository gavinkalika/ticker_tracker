CREATE DATABASE `ticker_tracker` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- Table: ticker
DROP TABLE ticker;
CREATE TABLE ticker (
`id` INT  AUTO_INCREMENT NOT NULL UNIQUE,
`ticker` VARCHAR (64) UNIQUE NOT NULL,
`created_date` DATETIME NOT NULL,
PRIMARY KEY (id));

-- Table: ticker_data
DROP TABLE ticker_data;
CREATE TABLE ticker_data (
id INT (64) UNIQUE AUTO_INCREMENT NOT NULL,
`rank` INT (64) NOT NULL,
`close` DECIMAL (10, 4) NOT NULL,
`dollar_change` DECIMAL (10, 4) NOT NULL,
`percent_change` DECIMAL (10, 4) NOT NULL,
`volume` INT (64) NOT NULL,
`tsi` DECIMAL (10, 4) NOT NULL,
ticker_id INT (64) NOT NULL,
`created_date` DATETIME NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (ticker_id) REFERENCES ticker(id)
);

CREATE TABLE `insert_log` (
  `created_date` date NOT NULL,
  `created_time` varchar(45) NOT NULL,
  PRIMARY KEY (`created_date`),
  UNIQUE KEY `created_date_UNIQUE` (`created_date`),
  UNIQUE KEY `created_time_UNIQUE` (`created_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
