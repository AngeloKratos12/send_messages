-- MySQL dump 10.19  Distrib 10.3.34-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: sms
-- ------------------------------------------------------
-- Server version	10.3.34-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('37d0d4dae0f6');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `file_sended`
--

DROP TABLE IF EXISTS `file_sended`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `file_sended` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_expediteur` int(11) DEFAULT NULL,
  `id_destinateur` int(11) DEFAULT NULL,
  `filetype` varchar(15) DEFAULT NULL,
  `filename` varchar(50) DEFAULT NULL,
  `reference` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_file_sended_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `file_sended`
--

LOCK TABLES `file_sended` WRITE;
/*!40000 ALTER TABLE `file_sended` DISABLE KEYS */;
/*!40000 ALTER TABLE `file_sended` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reception`
--

DROP TABLE IF EXISTS `reception`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reception` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `expediteur` varchar(50) DEFAULT NULL,
  `id_expediteur` int(11) DEFAULT NULL,
  `destinateur` varchar(50) DEFAULT NULL,
  `id_destinateur` int(11) DEFAULT NULL,
  `message_` text DEFAULT NULL,
  `date` date DEFAULT NULL,
  `heure` time DEFAULT NULL,
  `file` int(11) DEFAULT NULL,
  `reference` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_reception_date` (`date`),
  KEY `ix_reception_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reception`
--

LOCK TABLES `reception` WRITE;
/*!40000 ALTER TABLE `reception` DISABLE KEYS */;
INSERT INTO `reception` VALUES (13,'angelo',1,'kratos',2,'salut!!','2022-08-05','01:54:50',NULL,NULL),(15,'angelo',1,'kratos',2,'je suis là!!','2022-08-05','10:52:30',NULL,NULL),(20,'kratos',2,'angelo',1,'Ouai cv!!','2022-08-05','12:20:06',NULL,NULL),(21,'angelo',1,'angelo',1,'Qu\'est ce que tu veux!!','2022-08-05','12:21:13',NULL,NULL),(23,'angelo',1,'kratos',2,'Non!! C\'est comme ça!!','2022-08-05','12:21:49',NULL,NULL),(26,'angelo',1,'kratos',2,'cc','2022-08-05','12:22:58',NULL,NULL),(28,'kratos',2,'angelo',1,'Pourqoui tu ne marce pas!!','2022-08-05','12:29:51',NULL,NULL),(30,'kratos',2,'kratos',2,'salut mec','2022-08-05','13:49:45',NULL,NULL),(32,'kratos',2,'angelo',1,'salut','2022-08-05','13:50:08',NULL,NULL),(35,'angelo',1,'kratos',2,'cc','2022-08-05','20:10:10',NULL,NULL),(43,'angelo',1,'kratos',2,'n','2022-08-07','01:15:20',NULL,NULL),(57,'angelo',1,'kratos',2,'mande amizay','2022-08-07','15:59:43',NULL,NULL),(58,'kratos',2,'angelo',1,'ya, mande','2022-08-07','16:00:04',NULL,NULL),(59,'kratos',2,'angelo',1,'ya, mande','2022-08-07','16:00:19',NULL,NULL),(60,'kratos',2,'angelo',1,'ya, mande','2022-08-07','16:00:20',NULL,NULL),(61,'angelo',1,'kratos',2,'EO!! atero eo fa hitako!!','2022-08-07','17:17:14',NULL,NULL),(62,'kratos',2,'angelo',1,'merci!!','2022-08-07','17:18:01',NULL,NULL),(63,'kratos',2,'angelo',1,'de aôn ny fandean:!!','2022-08-07','17:18:42',NULL,NULL),(64,'kratos',2,'angelo',1,'merci!!','2022-08-07','18:33:55',NULL,NULL),(65,'kratos',2,'kratos',2,'ffffffffffffffffffffffff','2022-08-08','23:19:48',NULL,NULL),(66,'kratos',2,'kratos',2,'ffffffffffffffffffffffff','2022-08-08','23:19:52',NULL,NULL),(67,'kratos',2,'kratos',2,'de aôneee','2022-08-08','23:20:38',NULL,NULL),(68,'kratos',2,'kratos',2,'de aôneee','2022-08-08','23:28:55',NULL,NULL),(86,'angelo',1,'kratos',2,'Salut!!!','2022-08-09','10:23:58',NULL,NULL),(87,'angelo',1,'kratos',2,'voila!!','2022-08-09','10:43:20',NULL,NULL),(88,'angelo',NULL,'kratos',NULL,'ccccccccc','2022-08-09','10:45:35',NULL,NULL),(89,'angelo',NULL,'kratos',NULL,'ccccccccc','2022-08-09','10:45:45',NULL,NULL),(90,'angelo',NULL,'kratos',2,'ccccccccc','2022-08-09','10:45:53',NULL,NULL),(91,'kratos',2,'angelo',1,'fa ôna eee','2022-08-09','10:45:53',NULL,NULL),(92,'angelo',1,'kratos',NULL,'best','2022-08-09','10:46:33',NULL,NULL),(93,'angelo',1,'kratos',2,'bonjour mec!!!','2022-09-23','16:08:32',NULL,NULL),(94,'kratos',2,'angelo',1,'best boite!!','2022-09-23','16:12:57',NULL,NULL),(95,'angelo',1,'krat',NULL,'','2022-09-27','19:29:06',NULL,NULL),(96,'angelo',1,'kratos',2,'salut','2022-09-27','19:29:16',NULL,NULL),(97,'angelo',1,'krat',NULL,'','2022-09-27','20:51:00',NULL,NULL),(98,'kratos',2,'',NULL,'','2022-09-29','19:16:02',NULL,NULL),(99,'kratos',2,'',NULL,'','2022-09-29','21:25:47',NULL,NULL),(100,'kratos',2,'angelo',1,'blablablablablabalalababalanalabjanala','2022-09-30','00:03:45',NULL,NULL);
/*!40000 ALTER TABLE `reception` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `categorie` enum('male','femme','autres') DEFAULT NULL,
  `mail` varchar(50) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `password` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_user_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'MIHARIMANANA','angelo','male','angelo21.aps2b@gmail.com','0341447461','260702'),(2,'ANGELO','kratos','male','miharimananaangelo@yahoo.com','0341447461','270702'),(3,'randriamalala','precis','male','precis21.aps2a@gmail.com','0000','yes'),(4,'bandy','mamay','male','angelo21.aps2b@gmail.com','0000','non'),(5,'bandy','mamay','male','angelo21.aps2b@gmail.com','0000','non');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-04 15:50:51
