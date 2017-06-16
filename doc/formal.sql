-- MySQL dump 10.13  Distrib 5.7.18, for Linux (x86_64)
--
-- Host: localhost    Database: ticket
-- ------------------------------------------------------
-- Server version	5.7.18-0ubuntu0.16.04.1

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
-- Table structure for table `cinema`
--

DROP TABLE IF EXISTS `cinema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cinema` (
  `cinema_id` int(11) NOT NULL AUTO_INCREMENT,
  `cinema_name` varchar(64) NOT NULL,
  `info` text,
  PRIMARY KEY (`cinema_id`),
  UNIQUE KEY `cinema_name` (`cinema_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cinema`
--

LOCK TABLES `cinema` WRITE;
/*!40000 ALTER TABLE `cinema` DISABLE KEYS */;
INSERT INTO `cinema` VALUES (1,'CINEMA_A','CINEMA_A_INFO'),(2,'CINEMA_B','CINEMA_B_INFO'),(3,'CINEMA_C','CINEMA_C_INFO'),(4,'CINEMA_D','CINEMA_D_INFO'),(5,'CINEMA_E','CINEMA_E_INFO'),(6,'CINEMA_F','CINEMA_F_INFO');
/*!40000 ALTER TABLE `cinema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie` (
  `movie_id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_name` varchar(64) NOT NULL,
  `length` int(11) NOT NULL,
  `img` varchar(256) DEFAULT NULL,
  `info` text,
  PRIMARY KEY (`movie_id`),
  UNIQUE KEY `ix_movie_movie_name` (`movie_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'WAR_AND_PIECE',100,'/static/pic/warandpiece.jpeg','A STORY ABOUT WAR AND PIECE!'),(2,'UNIX',90,'/static/pic/unix.jpg','UNIX LOGO'),(3,'LORD OF WAR',120,'/static/pic/lordofwar.jpeg','ni gu la si kai qi'),(4,'I AM LEGEND',120,'/static/pic/iamlegend.jpg','i am legend infomation'),(5,'THE SHAWSHANK REDEMPTION',140,'/static/pic/theshawshankredemption.jpeg','a story about two man'),(6,'IRON MAN',60,'/static/pic/ironman.jpg','super hero iron man');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `order_at` datetime DEFAULT NULL,
  `ticket_id` int(11) NOT NULL,
  `pay` int(4) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `ix_order_user_id` (`user_id`),
  KEY `ix_ticket_ticket_id` (`ticket_id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,2,'2017-06-17 03:08:19',23,0),(2,2,'2017-06-17 03:33:35',24,0),(3,2,'2017-06-17 04:37:19',25,0),(4,2,'2017-06-17 04:37:27',26,0);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `show_in`
--

DROP TABLE IF EXISTS `show_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `show_in` (
  `showin_id` int(11) NOT NULL AUTO_INCREMENT,
  `cinema_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `start_at` datetime DEFAULT NULL,
  `room` varchar(60) DEFAULT NULL,
  `seat` varchar(300) DEFAULT NULL,
  `price` double(16,2) DEFAULT NULL,
  PRIMARY KEY (`showin_id`),
  KEY `ix_show_in_movie_id` (`movie_id`),
  KEY `ix_show_in_cinema_id` (`cinema_id`),
  CONSTRAINT `show_in_ibfk_1` FOREIGN KEY (`cinema_id`) REFERENCES `cinema` (`cinema_id`),
  CONSTRAINT `show_in_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `show_in`
--

LOCK TABLES `show_in` WRITE;
/*!40000 ALTER TABLE `show_in` DISABLE KEYS */;
INSERT INTO `show_in` VALUES (1,1,1,'2001-12-12 06:00:00','A','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',100.00),(2,1,2,'2001-12-12 07:00:00','A','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',100.00),(3,2,2,'2001-12-12 07:00:00','A','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',100.00),(4,2,3,'2001-12-12 08:00:00','A','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',100.00),(5,1,1,'2001-12-12 06:06:06','B','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',100.00),(6,3,4,'2001-12-12 01:00:00','C','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',60.00),(7,3,5,'2001-12-12 01:00:00','C','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',60.00),(8,3,1,'2001-12-12 01:00:00','C','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',60.00),(9,4,2,'2001-12-12 01:00:00','C','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',60.00),(10,4,6,'2001-12-12 01:00:00','C','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',60.00),(11,5,1,'2001-12-12 01:00:00','C','0_0,0_1,0_2,0_3,0_4,1_0,1_1,1_2,1_3,1_4',60.00),(12,5,6,'2001-12-12 09:00:00','C','0_0,0_1,0_2,0_4,1_0,1_1,1_4,',60.00);
/*!40000 ALTER TABLE `show_in` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket` (
  `ticket_id` int(11) NOT NULL AUTO_INCREMENT,
  `cinema_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `showin_id` int(11) NOT NULL,
  `room` varchar(60) DEFAULT NULL,
  `seat` varchar(300) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `ix_ticket_movie_id` (`movie_id`),
  KEY `ix_ticket_cinema_id` (`cinema_id`),
  KEY `ix_ticket_user_id` (`user_id`),
  KEY `ix_ticket_showin_id` (`showin_id`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`cinema_id`) REFERENCES `cinema` (`cinema_id`),
  CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`movie_id`),
  CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `ticket_ibfk_4` FOREIGN KEY (`showin_id`) REFERENCES `show_in` (`showin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (22,1,1,1,'A','[\'0_1\', \'\']',2),(23,1,1,1,'A','[\'1_2\', \'\']',2),(24,1,1,5,'B','[\'0_1\', \'\']',2),(25,5,6,12,'C','[\'1_3\', \'1_2\', \'\']',2),(26,5,6,12,'C','[\'1_3\', \'0_3\', \'\']',2);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `email` varchar(64) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `password` char(65) NOT NULL,
  `img` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `ix_user_name` (`name`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'a123456','302926232@qq.com','15112416138','123456',NULL),(2,'a1234567','3029226232@qq.com','15112416137','123456',NULL);
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

-- Dump completed on 2017-06-17  4:40:03
