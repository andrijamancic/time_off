CREATE DATABASE  IF NOT EXISTS `time_off` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `time_off`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: time_off
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `id` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `phone_number` varchar(30) DEFAULT NULL,
  `street_name` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `postal_code` varchar(30) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `days_off` int DEFAULT NULL,
  `holiday_group_id` varchar(50) DEFAULT NULL,
  `superior_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `holiday_group_id` (`holiday_group_id`),
  KEY `superior_id` (`superior_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`holiday_group_id`) REFERENCES `holiday_groups` (`id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`superior_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES ('3677bee5-129d-4df9-80e0-c2d75c392f9c','test@test.com','ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae','Test Ime','Test Prezime','2023-02-15','string','string','string','string','string',18,'cc680fdf-e704-4aee-8202-f27e6711b014','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d','dragisa@itbc.rs','856cb0d74eecf479c16b7a61d5b68ed2692c47ba83b3f540a5500f356bbb6467','Dragisa','Milovanovic','1989-04-14','066412321','Sremska','Nis','18000','Serbia',18,'cc680fdf-e704-4aee-8202-f27e6711b014','87b78973-b145-46fc-93bb-76cb41b2aa49'),('87b78973-b145-46fc-93bb-76cb41b2aa49','admin@itbc.rs','3b612c75a7b5048a435fb6ec81e52ff92d6d795a8b5a9c17070f6a63c97a53b2','Administrator','Administratovic','1980-06-11','0664738221','Dusanova','Nis','18000','Serbia',20,'cc680fdf-e704-4aee-8202-f27e6711b014',NULL),('ddbbb341-300a-481a-b4e3-85e4150a06b7','superior@superior.com','1e0fbef7daf0abddb6aefe932ad275458d86233201dd46be149349795656068c','Superior','nadredjeni','2023-02-15','string','string','string','string','string',20,'cc680fdf-e704-4aee-8202-f27e6711b014',NULL),('f0853f06-0e5f-4632-8ddf-79fde154e806','classic@classic.com','c09b48cc9290cf186d7e040bc5b2c46fdbaf89aedd4beca0c13779973f28100e','string','string','2023-02-20','string','string','string','string','string',20,'cc680fdf-e704-4aee-8202-f27e6711b014','f6d5dba1-6f0c-4c6f-8292-ab7636a017db'),('f6d5dba1-6f0c-4c6f-8292-ab7636a017db','superior1@superior1.com','1e0fbef7daf0abddb6aefe932ad275458d86233201dd46be149349795656068c','string','string','2023-02-20','string','string','string','string','string',20,'cc680fdf-e704-4aee-8202-f27e6711b014',NULL);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holiday_group_dates`
--

DROP TABLE IF EXISTS `holiday_group_dates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `holiday_group_dates` (
  `id` varchar(50) NOT NULL,
  `name` varchar(250) NOT NULL,
  `date` date DEFAULT NULL,
  `holiday_group_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `holiday_group_id` (`holiday_group_id`),
  CONSTRAINT `holiday_group_dates_ibfk_1` FOREIGN KEY (`holiday_group_id`) REFERENCES `holiday_groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holiday_group_dates`
--

LOCK TABLES `holiday_group_dates` WRITE;
/*!40000 ALTER TABLE `holiday_group_dates` DISABLE KEYS */;
INSERT INTO `holiday_group_dates` VALUES ('1255e52b-e9e0-44a4-98e8-d22e79cba419','Christmas','2000-01-07','cc680fdf-e704-4aee-8202-f27e6711b014'),('23857d94-c41f-4a51-9859-fc593af9a4eb','Zadusnice','2023-02-15','ee80a0e9-6492-4102-9cee-252e7639f660'),('d8e3b031-0d43-49be-809d-84f549a4f5c0','Nova Godina','2000-12-31','cc680fdf-e704-4aee-8202-f27e6711b014'),('dd3fbe34-d92a-40f3-8e87-70cf27b2e4ed','Nova Godina dan 2','2000-01-01','cc680fdf-e704-4aee-8202-f27e6711b014'),('e42cf5ea-a921-4efe-a17a-11402fb071e5','Dan posle dan zaljubljenih - Treznjenje','2023-02-15','cc680fdf-e704-4aee-8202-f27e6711b014');
/*!40000 ALTER TABLE `holiday_group_dates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holiday_groups`
--

DROP TABLE IF EXISTS `holiday_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `holiday_groups` (
  `id` varchar(50) NOT NULL,
  `name` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holiday_groups`
--

LOCK TABLES `holiday_groups` WRITE;
/*!40000 ALTER TABLE `holiday_groups` DISABLE KEYS */;
INSERT INTO `holiday_groups` VALUES ('4fbd7f74-d376-4fa2-a55a-e56a66f419f9','Russian National holidays'),('543aa14b-a55a-4db8-9931-ec05c7a11103','Danish National holidays'),('a574c7ae-a024-417a-aac1-6eec00a085b7','Australian National holidays'),('cc680fdf-e704-4aee-8202-f27e6711b014','Serbian Orthodox'),('ee80a0e9-6492-4102-9cee-252e7639f660','US National holidays');
/*!40000 ALTER TABLE `holiday_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_dates`
--

DROP TABLE IF EXISTS `request_dates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `request_dates` (
  `id` varchar(50) NOT NULL,
  `r_date` date DEFAULT NULL,
  `status` enum('pending','approved','denied') DEFAULT NULL,
  `request_id` varchar(50) NOT NULL,
  `employee_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `request_id` (`request_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `request_dates_ibfk_1` FOREIGN KEY (`request_id`) REFERENCES `requests` (`id`),
  CONSTRAINT `request_dates_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_dates`
--

LOCK TABLES `request_dates` WRITE;
/*!40000 ALTER TABLE `request_dates` DISABLE KEYS */;
INSERT INTO `request_dates` VALUES ('0e5cf402-f754-4cb9-8196-57353a67d0e5','2023-02-25','pending','a00f92c0-0f09-4f12-9404-74e315f3af06','87b78973-b145-46fc-93bb-76cb41b2aa49'),('1873c39d-ef73-4d9f-bfd3-ab075f0d210c','2023-02-15','approved','7b1b6999-140c-43b6-8ae1-2bc14e2fa116','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('247c7501-e880-44ba-b7ee-cb0aa167f12d','2023-02-25','pending','2aba5feb-dd40-4898-a193-8e62672a7d26','6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d'),('33a3fb26-2c48-4d88-b7bf-f654c928c69e','2023-02-23','pending','a00f92c0-0f09-4f12-9404-74e315f3af06','87b78973-b145-46fc-93bb-76cb41b2aa49'),('47bf3a49-3e6e-4b83-812b-a04fb977d938','2023-02-19','approved','02677c59-9ede-4eca-91a5-e9279bab960e','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('5c4df359-6a81-451d-838e-d229ff3bacd6','2023-02-15','approved','02677c59-9ede-4eca-91a5-e9279bab960e','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('62cdca2d-8001-48fd-8707-c37db71edb29','2023-02-16','pending','609de20b-436e-49a4-b3de-8a8abdb0dd42','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('7a532635-a94d-45a9-9f78-7a8b88f9fe93','2023-02-24','approved','2aba5feb-dd40-4898-a193-8e62672a7d26','6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d'),('8929eb2a-679e-49cf-a8aa-71fd652fd896','2023-02-18','pending','02677c59-9ede-4eca-91a5-e9279bab960e','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('95320e40-6aa3-4d99-943f-4eb8a73df9fe','2023-02-26','pending','2aba5feb-dd40-4898-a193-8e62672a7d26','6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d'),('a348bd29-d6dd-40d6-8a34-fad7afec9aba','2023-02-22','pending','a9c4fc08-206c-410f-8b63-f01f803a0c8e','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('a580c103-e9dd-4bdc-91d3-0b1b3df05a48','2023-02-27','pending','2aba5feb-dd40-4898-a193-8e62672a7d26','6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d'),('aa9f859b-a095-4f8f-a2e8-abf1a0c88fd3','2023-02-15','approved','b02090b2-7c88-4b53-aa1f-d38b60288d3e','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('c3c93d32-fbee-4d9e-80c8-064d112eb092','2023-02-17','pending','b02090b2-7c88-4b53-aa1f-d38b60288d3e','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('c7a8b1c4-f8f9-4883-8571-a96e0636a7a3','2023-02-28','pending','2aba5feb-dd40-4898-a193-8e62672a7d26','6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d'),('dc2d707a-c824-4ba8-81a9-6ad71faca4e1','2023-02-23','approved','2aba5feb-dd40-4898-a193-8e62672a7d26','6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d'),('e0d6ecae-77f3-417e-927f-43bde8ec1917','2023-02-16','pending','7b1b6999-140c-43b6-8ae1-2bc14e2fa116','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('e6d697e3-9cbf-44b8-8a67-40662471f750','2023-02-16','pending','b02090b2-7c88-4b53-aa1f-d38b60288d3e','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('e7cac779-4a42-4554-bff3-b45b69bd402f','2023-02-24','pending','a00f92c0-0f09-4f12-9404-74e315f3af06','87b78973-b145-46fc-93bb-76cb41b2aa49'),('fba69440-6962-4578-bb2a-873a789cae4e','2000-02-02','pending','25c215d9-adc6-4065-ab71-9d7d0349f490','ddbbb341-300a-481a-b4e3-85e4150a06b7');
/*!40000 ALTER TABLE `request_dates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requests` (
  `id` varchar(50) NOT NULL,
  `type` enum('pto','sick','unpaid') DEFAULT NULL,
  `cancelled` tinyint(1) DEFAULT NULL,
  `message` varchar(250) DEFAULT NULL,
  `superior_message` varchar(250) DEFAULT NULL,
  `request_date` date DEFAULT NULL,
  `response_date` date DEFAULT NULL,
  `employee_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
INSERT INTO `requests` VALUES ('02677c59-9ede-4eca-91a5-e9279bab960e','pto',1,'string','','2023-02-15','2023-02-15','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('25c215d9-adc6-4065-ab71-9d7d0349f490','unpaid',1,'asd','ne moze','2002-01-01','2000-01-01','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('2aba5feb-dd40-4898-a193-8e62672a7d26','unpaid',0,'Idem da radim gradjevinu neki dan, ako moze','','2023-02-22','2023-02-22','6fb2b5fe-5b7f-4453-a7c0-9edcc828c23d'),('47877a96-2baf-44aa-9e7b-dcf79d70a19e','pto',0,'msg','','2023-02-15','2023-02-15','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('609de20b-436e-49a4-b3de-8a8abdb0dd42','pto',0,'string','','2023-02-15','2023-02-15','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('7b1b6999-140c-43b6-8ae1-2bc14e2fa116','pto',0,'string','','2023-02-15','2023-02-15','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('8439f0bb-1a95-4099-894d-d1465df4b683','pto',0,'string','','2023-02-15','2023-02-15','ddbbb341-300a-481a-b4e3-85e4150a06b7'),('a00f92c0-0f09-4f12-9404-74e315f3af06','sick',0,'Uvatila me koronka','','2023-02-22','2023-02-22','87b78973-b145-46fc-93bb-76cb41b2aa49'),('a9c4fc08-206c-410f-8b63-f01f803a0c8e','pto',0,'string','','2023-02-22','2023-02-22','3677bee5-129d-4df9-80e0-c2d75c392f9c'),('b02090b2-7c88-4b53-aa1f-d38b60288d3e','sick',0,'string','string','2023-02-15','2023-02-15','ddbbb341-300a-481a-b4e3-85e4150a06b7');
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 17:27:37
