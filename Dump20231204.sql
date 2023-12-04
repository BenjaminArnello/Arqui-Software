-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `busqueda_remedios`
--

DROP TABLE IF EXISTS `busqueda_remedios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `busqueda_remedios` (
  `id_remedio` int NOT NULL,
  `link` varchar(100) DEFAULT NULL,
  `ultima_busqueda` date DEFAULT NULL,
  `precio` int DEFAULT NULL,
  PRIMARY KEY (`id_remedio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `busqueda_remedios`
--

LOCK TABLES `busqueda_remedios` WRITE;
/*!40000 ALTER TABLE `busqueda_remedios` DISABLE KEYS */;
INSERT INTO `busqueda_remedios` VALUES (1,'https://www.drsimi.cl/paracetamol-500-mg-16-comprimidos/p','2023-11-18',480),(2,'https://www.drsimi.cl/ibuprofeno-400-mg-20-comprimidos-recubiertos/p','2023-11-18',950),(3,'https://www.drsimi.cl/aspirina-acido-acetilsalicilico-500-mg-20-comprimidos/p','2023-11-15',999),(4,'https://www.drsimi.cl/loratadina-10-mg-30-comprimidos/p','2023-11-15',999);
/*!40000 ALTER TABLE `busqueda_remedios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `camas`
--

DROP TABLE IF EXISTS `camas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `camas` (
  `id_cama` int NOT NULL AUTO_INCREMENT,
  `id_salas` varchar(45) NOT NULL,
  `ocupada` tinyint NOT NULL,
  PRIMARY KEY (`id_cama`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camas`
--

LOCK TABLES `camas` WRITE;
/*!40000 ALTER TABLE `camas` DISABLE KEYS */;
INSERT INTO `camas` VALUES (1,'1',1),(2,'1',1),(3,'1',1),(4,'1',0),(5,'1',1),(6,'2',1),(7,'2',1),(8,'2',1),(9,'3',1),(10,'3',1),(11,'3',1),(12,'3',1),(13,'3',1),(14,'3',1),(15,'3',1),(16,'3',1),(17,'3',0),(18,'3',0),(19,'4',0),(20,'4',0),(21,'4',0),(22,'4',0),(23,'4',1),(24,'5',0),(25,'5',0),(26,'5',0),(27,'5',0),(28,'5',0),(29,'5',0),(30,'5',0),(31,'5',0),(32,'5',0),(33,'5',0),(34,'5',0);
/*!40000 ALTER TABLE `camas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control_visitas`
--

DROP TABLE IF EXISTS `control_visitas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `control_visitas` (
  `id_visita` int NOT NULL AUTO_INCREMENT,
  `id_paciente` int NOT NULL,
  `hora_llegada` varchar(8) NOT NULL,
  `hora_salida` varchar(8) NOT NULL,
  `fecha` varchar(10) NOT NULL,
  `nombre_visita` varchar(100) NOT NULL,
  `rut_visita` varchar(11) NOT NULL,
  `confirmado` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_visita`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control_visitas`
--

LOCK TABLES `control_visitas` WRITE;
/*!40000 ALTER TABLE `control_visitas` DISABLE KEYS */;
INSERT INTO `control_visitas` VALUES (1,1,'14:31:00','16:31:00','2023-11-24','Benjamin Arnello','20550477-K',1),(2,1,'14:33:00','16:33:00','2023-11-24','Benjamin Arnello','20550477-K',1),(3,1,'14:34:00','16:34:00','2023-11-24','Benjamin Arnello','20550477-K',1),(4,1,'14:36:00','16:36:00','2023-11-24','Benjamin Arnello','20550477-K',0),(5,1,'14:38:00','16:38:00','2023-11-24','Benjamin Arnello','20550477-K',0),(6,1,'14:39:00','16:39:00','2023-11-24','Benjamin Arnello','20550477-K',0),(7,1,'22:22','00:22','2023-11-24','Benjamxc3xadn Arnello','20550477-K',0),(8,1,'18:56','20:56','2023-12-3','Gonzalo Gonzales','11111111-1',0),(9,11,'18:58','20:58','2023-12-4','Juanito Perez','11111111-1',1);
/*!40000 ALTER TABLE `control_visitas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctores`
--

DROP TABLE IF EXISTS `doctores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctores` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `especialidad` varchar(45) DEFAULT NULL,
  `numero` varchar(9) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctores`
--

LOCK TABLES `doctores` WRITE;
/*!40000 ALTER TABLE `doctores` DISABLE KEYS */;
INSERT INTO `doctores` VALUES (1,'Garcia Perez','Cardiologia','123456789'),(2,'Martinez Lopez','Neurologia','987654321'),(3,'Fernandez Gonzalez','Pediatra','456789123'),(4,'Lopez Rodriguez','Dermatologia','789123456'),(5,'Sanchez Gomez','Oftalmologia','321654987'),(6,'Perez Hernandez','Gastroenterologia','654987321'),(7,'Gomez Martinez','Ortopedia','852963741'),(8,'Gonzalez Sanchez','Endocrinologia','159263478'),(9,'Rodriguez Fernandez','Psiquiatria','369852147'),(10,'Hernandez Perez','Oncologia','147258369'),(11,'Martin Gomez','Ginecologia','258369147'),(12,'Jimenez Fernandez','Urologia','632541978'),(13,'Diaz Gonzalez','Nefrologia','741852963'),(14,'Munoz Sanchez','Hematologia','985632741'),(15,'Castro Rodriguez','Radiologia','369147852'),(16,'Blanco Gomez','Oncologia','123987456'),(17,'Ramos Diaz','Neumologia','456321987'),(18,'Morales Fernandez','Cardiologia','789654123'),(19,'Vega Perez','Gastroenterologia','214365879'),(20,'Flores Gonzalez','Endocrinologia','987123654');
/*!40000 ALTER TABLE `doctores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fichas`
--

DROP TABLE IF EXISTS `fichas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fichas` (
  `id_ficha` int NOT NULL AUTO_INCREMENT,
  `id_paciente` int NOT NULL,
  `texto` varchar(200) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_ficha`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fichas`
--

LOCK TABLES `fichas` WRITE;
/*!40000 ALTER TABLE `fichas` DISABLE KEYS */;
INSERT INTO `fichas` VALUES (4,2,'Paracetamol 400mg 1 vez al dia, Clorfenamina 2 veces al dia','2023-11-19 18:11:31'),(5,2,'Paracetamol 400mg 1 vez al dia','2023-11-19 18:11:31'),(39,1,'Dolor de Cabeza','2023-11-24 22:05:59'),(40,1,'Malestar General,nausea','2023-11-24 22:06:17'),(41,1,'Molestias estomacales','2023-11-24 22:06:56'),(42,1,'Inflamaci\\xc3\\xb3n Ojo','2023-12-04 15:55:52'),(43,1,'aa','2023-12-04 16:06:11'),(44,11,'aa','2023-12-04 16:10:40'),(45,1,'aaa','2023-12-04 16:16:51'),(46,1,'inflamacion','2023-12-04 16:17:03'),(47,1,'inflamacion2','2023-12-04 16:20:10'),(48,1,'aaa','2023-12-04 16:36:51'),(49,12,'obs','2023-12-04 18:47:01'),(50,11,'Presenta malestar general y dolores de cabeza','2023-12-04 18:59:51');
/*!40000 ALTER TABLE `fichas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horarios`
--

DROP TABLE IF EXISTS `horarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horarios` (
  `horario_id` int NOT NULL AUTO_INCREMENT,
  `doctor_id` int NOT NULL,
  `dia` int NOT NULL,
  `inicio` varchar(8) NOT NULL,
  `fin` varchar(8) NOT NULL,
  PRIMARY KEY (`horario_id`,`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horarios`
--

LOCK TABLES `horarios` WRITE;
/*!40000 ALTER TABLE `horarios` DISABLE KEYS */;
INSERT INTO `horarios` VALUES (1,1,1,'08:00 AM','05:00 PM'),(2,1,2,'08:30 AM','04:30 PM'),(3,1,3,'09:00 AM','06:00 PM'),(4,1,4,'08:00 AM','03:00 PM'),(5,1,5,'07:30 AM','02:30 PM'),(6,1,6,'10:00 AM','05:30 PM'),(7,1,7,'11:00 AM','04:00 PM'),(8,2,1,'09:00 AM','06:00 PM'),(9,2,2,'09:30 AM','05:30 PM'),(10,2,3,'10:00 AM','06:30 PM'),(11,2,4,'08:30 AM','04:30 PM'),(12,2,5,'08:00 AM','03:00 PM'),(13,2,6,'11:00 AM','06:00 PM'),(14,2,7,'12:00 PM','05:00 PM'),(15,3,1,'08:00 AM','04:00 PM'),(16,3,2,'08:30 AM','05:00 PM'),(17,3,3,'09:00 AM','06:00 PM'),(18,3,4,'08:00 AM','03:00 PM'),(19,3,5,'08:30 AM','04:30 PM'),(20,3,6,'10:00 AM','05:00 PM'),(21,3,7,'11:00 AM','04:00 PM'),(22,4,1,'09:00 AM','05:00 PM'),(23,4,2,'09:30 AM','06:00 PM'),(24,4,3,'10:00 AM','06:30 PM'),(25,4,4,'08:30 AM','04:30 PM'),(26,4,5,'08:00 AM','03:00 PM'),(27,4,6,'11:00 AM','06:00 PM'),(28,4,7,'12:00 PM','05:00 PM'),(29,5,1,'08:00 AM','04:00 PM'),(30,5,2,'08:30 AM','05:00 PM'),(31,5,3,'09:00 AM','06:00 PM'),(32,5,4,'08:00 AM','03:00 PM'),(33,5,5,'08:30 AM','04:30 PM'),(34,5,6,'10:00 AM','05:00 PM'),(35,5,7,'11:00 AM','04:00 PM'),(36,6,1,'09:00 PM','05:00 AM'),(37,6,2,'09:30 PM','06:00 AM'),(38,6,3,'10:00 PM','06:30 AM'),(39,6,4,'08:30 PM','04:30 AM'),(40,6,5,'08:00 PM','03:00 AM'),(41,6,6,'11:00 PM','06:00 AM'),(42,6,7,'12:00 AM','05:00 AM'),(43,7,1,'08:00 PM','04:00 AM'),(44,7,2,'08:30 PM','05:00 AM'),(45,7,3,'09:00 PM','05:30 AM'),(46,7,4,'08:00 PM','03:00 AM'),(47,7,5,'07:30 PM','02:30 AM'),(48,7,6,'10:00 PM','05:30 AM'),(49,7,7,'11:00 PM','04:00 AM'),(50,8,1,'07:00 PM','03:00 AM'),(51,8,2,'07:30 PM','04:30 AM'),(52,8,3,'08:00 PM','05:00 AM'),(53,8,4,'07:00 PM','02:00 AM'),(54,8,5,'06:30 PM','01:30 AM'),(55,8,6,'09:00 PM','04:30 AM'),(56,8,7,'10:00 PM','03:00 AM'),(57,6,1,'09:00 PM','05:00 AM'),(58,6,2,'09:30 PM','06:00 AM'),(59,6,3,'10:00 PM','06:30 AM'),(60,6,4,'08:30 PM','04:30 AM'),(61,6,5,'08:00 PM','03:00 AM'),(62,6,6,'11:00 PM','06:00 AM'),(63,6,7,'12:00 AM','05:00 AM'),(64,7,1,'08:00 PM','04:00 AM'),(65,7,2,'08:30 PM','05:00 AM'),(66,7,3,'09:00 PM','05:30 AM'),(67,7,4,'08:00 PM','03:00 AM'),(68,7,5,'07:30 PM','02:30 AM'),(69,7,6,'10:00 PM','05:30 AM'),(70,7,7,'11:00 PM','04:00 AM'),(71,8,1,'07:00 PM','03:00 AM'),(72,8,2,'07:30 PM','04:30 AM'),(73,8,3,'08:00 PM','05:00 AM'),(74,8,4,'07:00 PM','02:00 AM'),(75,8,5,'06:30 PM','01:30 AM'),(76,8,6,'09:00 PM','04:30 AM'),(77,8,7,'10:00 PM','03:00 AM'),(78,9,1,'08:00 PM','04:00 AM'),(79,9,2,'08:30 PM','05:00 AM'),(80,9,3,'09:00 PM','05:30 AM'),(81,9,4,'08:00 PM','03:00 AM'),(82,9,5,'07:30 PM','02:30 AM'),(83,9,6,'10:00 PM','05:30 AM'),(84,9,7,'11:00 PM','04:00 AM'),(85,10,1,'07:00 PM','03:00 AM'),(86,10,2,'07:30 PM','04:30 AM'),(87,10,3,'08:00 PM','05:00 AM'),(88,10,4,'07:00 PM','02:00 AM'),(89,10,5,'06:30 PM','01:30 AM'),(90,10,6,'09:00 PM','04:30 AM'),(91,10,7,'10:00 PM','03:00 AM'),(92,11,1,'08:00 AM','05:00 PM'),(93,11,2,'08:30 AM','05:30 PM'),(94,11,3,'09:00 AM','06:00 PM'),(95,11,4,'08:30 AM','05:30 PM'),(96,11,5,'08:00 AM','05:00 PM'),(97,11,6,'09:30 AM','04:30 PM'),(98,11,7,'10:30 AM','03:30 PM'),(99,12,1,'08:30 AM','05:30 PM'),(100,12,2,'09:00 AM','06:00 PM'),(101,12,3,'09:30 AM','06:30 PM'),(102,12,4,'09:00 AM','06:00 PM'),(103,12,5,'08:30 AM','05:30 PM'),(104,12,6,'10:00 AM','05:00 PM'),(105,12,7,'11:00 AM','04:00 PM'),(106,13,1,'09:00 AM','06:00 PM'),(107,13,2,'09:30 AM','06:30 PM'),(108,13,3,'10:00 AM','07:00 PM'),(109,13,4,'09:30 AM','06:30 PM'),(110,13,5,'09:00 AM','06:00 PM'),(111,13,6,'10:30 AM','05:30 PM'),(112,13,7,'11:30 AM','04:30 PM'),(113,14,1,'09:30 AM','06:30 PM'),(114,14,2,'10:00 AM','07:00 PM'),(115,14,3,'10:30 AM','07:30 PM'),(116,14,4,'10:00 AM','07:00 PM'),(117,14,5,'09:30 AM','06:30 PM'),(118,14,6,'11:00 AM','06:00 PM'),(119,14,7,'12:00 PM','05:00 PM'),(120,15,1,'10:00 AM','07:00 PM'),(121,15,2,'10:30 AM','07:30 PM'),(122,15,3,'11:00 AM','08:00 PM'),(123,15,4,'10:30 AM','07:30 PM'),(124,15,5,'10:00 AM','07:00 PM'),(125,15,6,'11:30 AM','06:30 PM'),(126,15,7,'12:30 PM','05:30 PM'),(127,16,1,'08:00 AM','05:00 PM'),(128,16,2,'08:00 PM','04:00 AM'),(129,16,3,'08:00 AM','05:00 PM'),(130,16,4,'08:00 PM','04:00 AM'),(131,16,5,'08:00 AM','05:00 PM'),(132,16,6,'08:00 PM','04:00 AM'),(133,16,7,'08:00 AM','04:00 PM'),(134,17,1,'09:00 AM','06:00 PM'),(135,17,2,'09:00 PM','05:00 AM'),(136,17,3,'09:00 AM','06:00 PM'),(137,17,4,'09:00 PM','05:00 AM'),(138,17,5,'09:00 AM','06:00 PM'),(139,17,6,'09:00 PM','05:00 AM'),(140,17,7,'09:00 AM','05:00 PM'),(141,18,1,'10:00 AM','07:00 PM'),(142,18,2,'10:00 PM','06:00 AM'),(143,18,3,'10:00 AM','07:00 PM'),(144,18,4,'10:00 PM','06:00 AM'),(145,18,5,'10:00 AM','07:00 PM'),(146,18,6,'10:00 PM','06:00 AM'),(147,18,7,'10:00 AM','06:00 PM'),(148,19,1,'11:00 AM','08:00 PM'),(149,19,2,'11:00 PM','07:00 AM'),(150,19,3,'11:00 AM','08:00 PM'),(151,19,4,'11:00 PM','07:00 AM'),(152,19,5,'11:00 AM','08:00 PM'),(153,19,6,'11:00 PM','07:00 AM'),(154,19,7,'11:00 AM','07:00 PM'),(155,20,1,'12:00 PM','09:00 PM'),(156,20,2,'12:00 AM','08:00 AM'),(157,20,3,'12:00 PM','09:00 PM'),(158,20,4,'12:00 AM','08:00 AM'),(159,20,5,'12:00 PM','09:00 PM'),(160,20,6,'12:00 AM','08:00 AM'),(161,20,7,'12:00 PM','08:00 PM');
/*!40000 ALTER TABLE `horarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `idlogin` int NOT NULL AUTO_INCREMENT,
  `rut` varchar(10) DEFAULT NULL,
  `pass` mediumtext,
  PRIMARY KEY (`idlogin`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'12345678-9','983487d9c4b7451b0e7d282114470d3a0ad50dc5e554971a4d1cda04acde670b');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pacientes`
--

DROP TABLE IF EXISTS `pacientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pacientes` (
  `id_paciente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellidoPaterno` varchar(45) NOT NULL,
  `apellidoMaterno` varchar(45) NOT NULL,
  `rut` varchar(11) NOT NULL,
  `id_cama` int DEFAULT '0',
  `sexo` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id_paciente`,`rut`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pacientes`
--

LOCK TABLES `pacientes` WRITE;
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
INSERT INTO `pacientes` VALUES (1,'Juan','García','López','12345678-5',6,'M'),(2,'María','Martínez','Pérez','98765432-1',4,'F'),(3,'Pedro','Rodríguez','Sánchez','45678901-2',6,'M'),(4,'Ana','Fernández','Gómez','78901234-5',0,'F'),(5,'Carlos','López','González','23456789-0',10,'M'),(6,'Cristobal','López','Lopez','23456729-0',0,'M'),(11,'Benjamin','Arnello','Riquelme','20550477-K',16,'M'),(12,'Erika','Riquelme','Carvajal','08540247-1',13,'F'),(14,'Benjamin','Sapiain','Aguayo','20677936-5',0,'M');
/*!40000 ALTER TABLE `pacientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recetas`
--

DROP TABLE IF EXISTS `recetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas` (
  `id_receta` int NOT NULL AUTO_INCREMENT,
  `id_paciente` int DEFAULT NULL,
  `texto` mediumtext,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_receta`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (1,1,'Loratadina 100 mg Aspirina 400 mg, dos veces por dia durante 5 dias','2023-11-19 20:10:26'),(2,1,'111','2023-11-24 21:17:22'),(3,1,'1','2023-11-24 21:17:38'),(4,1,'1','2023-11-24 21:20:03'),(5,1,'222','2023-11-24 21:22:28'),(6,1,'Paracetamol 500mg','2023-11-24 22:33:30'),(7,11,'ibuprofeno 500mg','2023-12-04 16:51:09'),(8,11,'Paracetamol 100mg','2023-12-04 18:13:56'),(9,11,'paracetamol 200mg','2023-12-04 18:14:31'),(10,11,'Loratadina','2023-12-04 18:19:17'),(11,11,'Aspirina','2023-12-04 18:24:40'),(12,11,'aaa','2023-12-04 18:28:21'),(13,11,'aspirina2','2023-12-04 18:30:34'),(14,11,'Aspirina 100mg','2023-12-04 19:00:06');
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remedios`
--

DROP TABLE IF EXISTS `remedios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remedios` (
  `id_remedio` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `cantidad` int DEFAULT NULL,
  PRIMARY KEY (`id_remedio`,`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remedios`
--

LOCK TABLES `remedios` WRITE;
/*!40000 ALTER TABLE `remedios` DISABLE KEYS */;
INSERT INTO `remedios` VALUES (1,'Paracetamol 500mg',93),(2,'Ibuprofeno 400mg',0),(3,'Aspirina 500mg',115),(4,'Loratadina 10mg',0),(5,'Omeprazol 20mg',75),(6,'Amoxicilina 500mg',110),(7,'Cetirizina 5mg',85),(8,'Diclofenaco 50mg',70),(9,'Ranitidina 150mg',95),(10,'Metformina 850mg',105),(11,'Clonazepam 0.5mg',65),(12,'Atorvastatina 20mg',85),(13,'Prednisona 5mg',100),(14,'Losartán 50mg',80),(15,'Sildenafil 50mg',75),(16,'Metoclopramida 10mg',90),(17,'Levotiroxina 100mcg',110),(18,'Codeína 30mg',70),(19,'Sertralina 50mg',95),(20,'Enalapril 10mg',105);
/*!40000 ALTER TABLE `remedios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salas`
--

DROP TABLE IF EXISTS `salas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salas` (
  `id_sala` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(45) DEFAULT NULL,
  `numero` varchar(45) NOT NULL,
  `cantidad_camas` int DEFAULT NULL,
  PRIMARY KEY (`id_sala`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salas`
--

LOCK TABLES `salas` WRITE;
/*!40000 ALTER TABLE `salas` DISABLE KEYS */;
INSERT INTO `salas` VALUES (1,'Hospitalizacion','101',5),(2,'Hospitalizacion','102',3),(3,'Hospitalizacion','103',10),(4,'UCI','201',5),(5,'UCI','202',10);
/*!40000 ALTER TABLE `salas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-04 19:09:40
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: especialistas
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `especialistas`
--

DROP TABLE IF EXISTS `especialistas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialistas` (
  `especialista_id` int NOT NULL,
  `nombre` text,
  `especialidad` text,
  `hospital` text,
  `numero` text,
  PRIMARY KEY (`especialista_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especialistas`
--

LOCK TABLES `especialistas` WRITE;
/*!40000 ALTER TABLE `especialistas` DISABLE KEYS */;
INSERT INTO `especialistas` VALUES (1,'Maria Rodriguez','Cardiologia','Hospital Metropolitano','951234567'),(2,'Juan Perez','Dermatologia','Hospital Clínico UC','956789012'),(3,'Ana Gomez','Pediatria','Hospital del Salvador','958765432'),(4,'Carlos Lopez','Gastroenterologia','Hospital Padre Hurtado','955432109'),(5,'Sofia Torres','Neurologia','Hospital San Juan de Dios','959012345'),(6,'Diego Martinez','Oftalmologia','Hospital Luis Calvo Mackenna','957654321'),(7,'Valentina Castro','Ginecologia','Hospital Sótero del Río','954321098'),(8,'Luis Fernandez','Ortopedia','Hospital de Niños Roberto del Río','951098765'),(9,'Isabel Jimenez','Urologia','Hospital Clínico Mutual de Seguridad','953210987'),(10,'Andres Medina','Endocrinologia','Hospital San Borja Arriarán','958765432'),(11,'Miguel Silva','Oncologia','Hospital Barros Luco Trudeau','954321098'),(12,'Elena Gonzalez','Hematologia','Hospital Clínico UC','959012345'),(13,'Javier Vargas','Nefrologia','Hospital Padre Hurtado','955432109'),(14,'Carmen Soto','Psiquiatria','Hospital del Salvador','951234567'),(15,'Hugo Ramirez','Radiologia','Hospital San Juan de Dios','956789012'),(16,'Lucia Herrera','Neumologia','Hospital San José','953210987'),(17,'Francisco Orellana','Dermatologia','Hospital Clínico Las Condes','951098765'),(18,'Marta Diaz','Cardiologia','Hospital de Carabineros','957654321'),(19,'Pedro Castro','Pediatria','Hospital de la Fuerza Aérea','959012345'),(20,'Sara Lopez','Geriatria','Hospital del Trabajador','954321098'),(21,'Roberto Torres','Reumatologia','Hospital Barros Luco Trudeau','956789012'),(22,'Paula Garcia','Dermatologia','Hospital Clínico UC','955432109'),(23,'Andrea Morales','Neurologia','Hospital Padre Hurtado','951234567'),(24,'Antonio Vega','Cardiologia','Hospital Metropolitano','953210987'),(25,'Catalina Rodriguez','Pediatria','Hospital del Salvador','957654321'),(26,'Jorge Sanchez','Gastroenterologia','Hospital San Juan de Dios','951098765'),(27,'Gloria Muñoz','Neurologia','Hospital San José','959012345'),(28,'Manuel Gonzalez','Oftalmologia','Hospital Clínico Mutual de Seguridad','954321098'),(29,'Rosa Perez','Cardiologia','Hospital de Niños Roberto del Río','956789012'),(30,'Emilio Fernandez','Oncologia','Hospital del Trabajador','955432109');
/*!40000 ALTER TABLE `especialistas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horarios`
--

DROP TABLE IF EXISTS `horarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horarios` (
  `horario_id` int NOT NULL AUTO_INCREMENT,
  `especialista_id` int DEFAULT NULL,
  `dia` int DEFAULT NULL,
  `inicio` text,
  `fin` text,
  PRIMARY KEY (`horario_id`),
  KEY `especialista_id` (`especialista_id`),
  CONSTRAINT `horarios_ibfk_1` FOREIGN KEY (`especialista_id`) REFERENCES `especialistas` (`especialista_id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horarios`
--

LOCK TABLES `horarios` WRITE;
/*!40000 ALTER TABLE `horarios` DISABLE KEYS */;
INSERT INTO `horarios` VALUES (1,1,1,'09:00 AM','04:00 PM'),(2,1,2,'10:00 AM','05:00 PM'),(3,1,3,'08:30 AM','03:30 PM'),(4,1,4,'09:30 AM','04:30 PM'),(5,1,5,'08:00 AM','03:00 PM'),(6,2,1,'12:00 AM','03:00 PM'),(7,2,2,'12:30 AM','03:30 PM'),(8,2,3,'01:00 AM','09:00 AM'),(9,2,4,'05:30 PM','06:30 PM'),(10,2,5,'09:30 AM','04:30 PM'),(11,3,1,'10:00 AM','04:00 PM'),(12,3,2,'10:00 AM','05:00 PM'),(13,3,3,'11:30 AM','03:30 PM'),(14,3,4,'01:30 PM','04:30 PM'),(15,3,5,'08:00 AM','03:00 PM'),(16,4,1,'12:00 PM','03:00 AM'),(17,4,2,'12:30 PM','03:30 AM'),(18,4,3,'01:00 PM','09:00 AM'),(19,4,4,'05:30 PM','06:30 PM'),(20,4,5,'09:30 PM','04:30 AM'),(21,5,1,'04:00 PM','10:00 PM'),(22,5,2,'04:00 PM','12:00 PM'),(23,5,3,'04:30 PM','19:30 PM'),(24,5,4,'04:30 PM','10:30 PM'),(25,5,5,'06:00 PM','11:00 PM'),(26,6,1,'08:00 AM','01:00 PM'),(27,6,2,'07:30 AM','02:30 PM'),(28,6,3,'08:00 AM','02:00 PM'),(29,6,4,'10:30 AM','02:30 PM'),(30,6,5,'09:30 AM','01:30 PM'),(31,7,1,'04:00 PM','10:00 PM'),(32,7,2,'04:00 PM','12:00 PM'),(33,7,3,'04:30 PM','19:30 PM'),(34,7,4,'04:30 PM','10:30 PM'),(35,7,5,'06:00 PM','11:00 PM'),(36,8,1,'08:00 AM','01:00 PM'),(37,8,2,'07:30 AM','02:30 PM'),(38,8,3,'08:00 AM','02:00 PM'),(39,8,4,'10:30 AM','02:30 PM'),(40,8,5,'09:30 AM','01:30 PM'),(41,9,1,'01:00 PM','10:00 PM'),(42,9,2,'01:00 PM','12:00 PM'),(43,9,3,'01:30 PM','19:30 PM'),(44,9,4,'02:30 PM','10:30 PM'),(45,9,5,'01:00 PM','11:00 PM'),(46,10,1,'08:00 AM','01:00 PM'),(47,10,2,'07:30 AM','04:30 PM'),(48,10,3,'08:00 AM','04:00 PM'),(49,10,4,'10:30 AM','04:30 PM'),(50,10,5,'09:30 AM','01:30 PM'),(51,11,1,'01:00 PM','10:00 PM'),(52,11,2,'01:00 PM','12:00 PM'),(53,11,3,'01:30 PM','19:30 PM'),(54,11,4,'02:30 PM','10:30 PM'),(55,11,5,'01:00 PM','11:00 PM'),(56,12,1,'08:00 AM','01:00 PM'),(57,12,2,'07:30 AM','04:30 PM'),(58,12,3,'08:00 AM','04:00 PM'),(59,12,4,'10:30 AM','04:30 PM'),(60,12,5,'09:30 AM','01:30 PM'),(61,13,1,'03:00 PM','09:00 PM'),(62,13,2,'03:00 PM','07:00 PM'),(63,13,3,'03:30 PM','08:30 PM'),(64,13,4,'03:30 PM','05:30 PM'),(65,13,5,'03:00 PM','01:00 AM'),(66,14,1,'11:00 AM','05:00 PM'),(67,14,2,'11:30 AM','06:30 PM'),(68,14,3,'11:00 AM','07:00 PM'),(69,14,4,'10:30 AM','08:30 PM'),(70,14,5,'09:30 AM','06:30 PM'),(71,15,1,'03:00 PM','09:00 PM'),(72,15,2,'03:00 PM','07:00 PM'),(73,15,3,'03:30 PM','08:30 PM'),(74,15,4,'03:30 PM','05:30 PM'),(75,15,5,'03:00 PM','01:00 AM'),(76,16,1,'11:00 AM','05:00 PM'),(77,16,2,'11:30 AM','06:30 PM'),(78,16,3,'11:00 AM','07:00 PM'),(79,16,4,'10:30 AM','08:30 PM'),(80,16,5,'09:30 AM','06:30 PM'),(81,17,1,'11:00 PM','07:00 AM'),(82,17,2,'11:00 PM','07:00 AM'),(83,17,3,'11:30 PM','07:30 AM'),(84,17,4,'11:30 PM','07:30 AM'),(85,17,5,'11:00 PM','07:00 AM'),(86,18,1,'07:00 AM','05:00 PM'),(87,18,2,'07:30 AM','06:30 PM'),(88,18,3,'07:00 AM','07:00 PM'),(89,18,4,'07:30 AM','08:30 PM'),(90,18,5,'07:30 AM','06:30 PM'),(91,19,1,'11:00 PM','07:00 AM'),(92,19,2,'11:00 PM','07:00 AM'),(93,19,3,'11:30 PM','07:30 AM'),(94,19,4,'11:30 PM','07:30 AM'),(95,19,5,'11:00 PM','07:00 AM'),(96,20,1,'07:00 AM','05:00 PM'),(97,20,2,'07:30 AM','06:30 PM'),(98,20,3,'07:00 AM','07:00 PM'),(99,20,4,'07:30 AM','08:30 PM'),(100,20,5,'07:30 AM','06:30 PM'),(101,21,1,'11:00 PM','04:00 AM'),(102,21,2,'11:00 PM','04:00 AM'),(103,21,3,'11:30 PM','04:30 AM'),(104,21,4,'11:30 PM','04:30 AM'),(105,21,5,'11:00 PM','04:00 AM'),(106,22,1,'07:00 AM','11:00 AM'),(107,22,2,'07:30 AM','11:30 AM'),(108,22,3,'07:00 AM','11:00 AM'),(109,22,4,'07:30 AM','11:30 AM'),(110,22,5,'07:30 AM','11:30 AM'),(111,23,1,'11:00 PM','04:00 AM'),(112,23,2,'11:00 PM','04:00 AM'),(113,23,3,'11:30 PM','04:30 AM'),(114,23,4,'11:30 PM','04:30 AM'),(115,23,5,'11:00 PM','04:00 AM'),(116,24,1,'07:00 AM','11:00 AM'),(117,24,2,'07:30 AM','11:30 AM'),(118,24,3,'07:00 AM','11:00 AM'),(119,24,4,'07:30 AM','11:30 AM'),(120,24,5,'07:30 AM','11:30 AM'),(121,25,1,'09:00 AM','07:00 PM'),(122,25,2,'10:00 AM','07:00 PM'),(123,25,3,'08:30 AM','07:30 PM'),(124,25,4,'09:30 AM','07:30 PM'),(125,25,5,'08:00 AM','07:00 PM');
/*!40000 ALTER TABLE `horarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-04 19:09:40
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: citas
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `horas`
--

DROP TABLE IF EXISTS `horas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horas` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `NombrePaciente` varchar(45) DEFAULT NULL,
  `Rut` varchar(11) DEFAULT NULL,
  `Dia` date DEFAULT NULL,
  `id_doctor` int DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `confirmado` tinyint DEFAULT '0',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horas`
--

LOCK TABLES `horas` WRITE;
/*!40000 ALTER TABLE `horas` DISABLE KEYS */;
INSERT INTO `horas` VALUES (1,'Juan Pérez','11111111-1','2023-11-15',3,'10:00:00',1),(2,'María Gómez','22222222-2','2023-11-16',7,'12:00:00',1),(3,'Carlos Rodríguez','33333333-3','2023-11-17',12,'10:00:00',0),(4,'Ana Sánchez','44444444-4','2023-11-18',18,'16:00:00',0),(5,'Luis Martínez','55555555-5','2023-11-19',2,'13:00:00',0),(6,'Laura Fernández','66666666-6','2023-11-20',15,'18:00:00',0),(7,'Pedro García','77777777-7','2023-11-21',10,'16:00:00',0),(8,'Elena López','88888888-8','2023-11-22',6,'14:00:00',0),(9,'Fernando Ruiz','99999999-9','2023-11-23',8,'18:00:00',1),(10,'Sofía Torres','00000000-0','2023-11-24',20,'17:00:00',1),(11,'Martín Castro','11111111-1','2023-11-25',1,'17:00:00',0),(12,'Lucía Díaz','22222222-2','2023-11-26',4,'10:00:00',0),(13,'Alejandro Moreno','33333333-3','2023-11-27',11,'13:00:00',0),(14,'Carmen Herrera','44444444-4','2023-11-28',13,'18:00:00',0),(15,'Andrés Soto','55555555-5','2023-11-29',9,'13:00:00',0),(16,'Valentina Navarro','66666666-6','2023-11-30',16,'14:00:00',0),(17,'Gabriel Vargas','77777777-7','2023-12-01',5,'15:00:00',0),(18,'Isabella Jiménez','88888888-8','2023-12-02',14,'12:00:00',0),(19,'Mateo Silva','99999999-9','2023-12-03',17,'17:00:00',1),(20,'Olivia Pérez','00000000-0','2023-12-04',19,'19:00:00',0),(21,'Juan Pérez','11111111-1','2023-11-15',7,'18:00:00',0),(22,'Juan Pérez','11111111-1','2023-11-20',7,'18:00:00',0),(23,'Gonzalo Gonzales','20111110','2023-11-17',1,'14:00:00',0),(24,'Pedro Palacios','20111110','2023-11-17',2,'09:00:00',0),(25,'Juan Romero','20111110','2023-11-18',3,'16:00:00',0),(26,'Juan Perez','1111111-1','2023-11-23',8,'18:00:00',0),(28,'JuanGarcíaLópez','12345678-5','2023-11-20',18,'12:00:00',0),(29,'Juan García López','12345678-5','2023-11-27',18,'12:00:00',0),(30,'Juan García López','12345678-5','2023-11-27',18,'14:00:00',0),(31,'Juan García López','12345678-5','2023-11-13',1,'14:00:00',0),(32,'Juan Perez','1111111-1','2023-11-24',8,'16:00:00',1),(33,'Juan Perez','1111111-1','2023-11-24',18,'16:00:00',0),(34,'Juan García López','12345678-5','2023-12-18',1,'14:00:00',0),(35,'Juan García López','12345678-5','2023-12-03',18,'14:00:00',0),(36,'Juan García López','12345678-5','2023-12-04',18,'12:00:00',0);
/*!40000 ALTER TABLE `horas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-04 19:09:40
