-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: PokeGuide
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `PokeGuide`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `PokeGuide` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `PokeGuide`;

--
-- Table structure for table `Ailment_Type`
--

DROP TABLE IF EXISTS `Ailment_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ailment_Type` (
  `Ail_Name` varchar(50) NOT NULL,
  `Duration` int DEFAULT NULL,
  `Security_Level` int DEFAULT NULL,
  PRIMARY KEY (`Ail_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ailment_Type`
--

LOCK TABLES `Ailment_Type` WRITE;
/*!40000 ALTER TABLE `Ailment_Type` DISABLE KEYS */;
INSERT INTO `Ailment_Type` VALUES ('Burn',5,2),('Confusion',3,3),('Fainted',0,0),('Flinching',1,1),('Freeze',3,5),('Paralysis',3,3),('Poison',5,2),('Sleep',3,4);
/*!40000 ALTER TABLE `Ailment_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ailment_and_Cure`
--

DROP TABLE IF EXISTS `Ailment_and_Cure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ailment_and_Cure` (
  `Berry_Name` varchar(50) DEFAULT NULL,
  `Item_Name` varchar(50) DEFAULT NULL,
  `Ail_Name` varchar(50) DEFAULT NULL,
  KEY `Ail_Name` (`Ail_Name`),
  KEY `Berry_Name` (`Berry_Name`),
  KEY `Item_Name` (`Item_Name`),
  CONSTRAINT `Ailment_and_Cure_ibfk_1` FOREIGN KEY (`Ail_Name`) REFERENCES `Ailment_Type` (`Ail_Name`),
  CONSTRAINT `Ailment_and_Cure_ibfk_2` FOREIGN KEY (`Berry_Name`) REFERENCES `Berries` (`Berry_Name`),
  CONSTRAINT `Ailment_and_Cure_ibfk_3` FOREIGN KEY (`Item_Name`) REFERENCES `Normal_Item` (`Item_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ailment_and_Cure`
--

LOCK TABLES `Ailment_and_Cure` WRITE;
/*!40000 ALTER TABLE `Ailment_and_Cure` DISABLE KEYS */;
INSERT INTO `Ailment_and_Cure` VALUES ('Cheri Berry',NULL,'Paralysis'),('Chesto Berry',NULL,'Burn'),('Pecha Berry',NULL,'Poison'),('Aspear Berry',NULL,'Sleep'),('Iapapa Berry',NULL,'Freeze'),('Tanga Berry',NULL,'Confusion'),(NULL,'Antidote','Poison'),(NULL,'Paralyze Heal','Paralysis'),(NULL,'Burn Heal','Burn'),(NULL,'Awakening','Sleep'),(NULL,'Ice Heal','Freeze'),(NULL,'Full Restore','Confusion'),(NULL,'Full Heal','Flinching'),(NULL,'Revive','Fainted');
/*!40000 ALTER TABLE `Ailment_and_Cure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bag_Items`
--

DROP TABLE IF EXISTS `Bag_Items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bag_Items` (
  `Item_Number` int NOT NULL,
  `Pokeball_Type` varchar(50) DEFAULT NULL,
  `Item_Name` varchar(50) DEFAULT NULL,
  `Berry_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Item_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bag_Items`
--

LOCK TABLES `Bag_Items` WRITE;
/*!40000 ALTER TABLE `Bag_Items` DISABLE KEYS */;
INSERT INTO `Bag_Items` VALUES (1,'Pokéball',NULL,NULL),(2,'Great Ball',NULL,NULL),(3,'Ultra Ball',NULL,NULL),(4,'Master Ball',NULL,NULL),(5,'Heal Ball',NULL,NULL),(6,'Premier Ball',NULL,NULL),(7,'Safari Ball',NULL,NULL),(8,NULL,NULL,'Oran Berry'),(9,NULL,NULL,'Leppa Berry'),(10,NULL,NULL,'Cheri Berry'),(11,NULL,NULL,'Chesto Berry'),(12,NULL,NULL,'Pecha Berry'),(13,NULL,NULL,'Aspear Berry'),(14,NULL,NULL,'Iapapa Berry'),(15,NULL,NULL,'Tanga Berry'),(16,NULL,'Potion',NULL),(17,NULL,'Super Potion',NULL),(18,NULL,'Hyper Potion',NULL),(19,NULL,'Max Potion',NULL),(20,NULL,'Revive',NULL),(21,NULL,'HP Up',NULL),(22,NULL,'Protein',NULL),(23,NULL,'Iron',NULL),(24,NULL,'Antidote',NULL),(25,NULL,'Paralyze Heal',NULL),(26,NULL,'Awakening',NULL),(27,NULL,'Burn Heal',NULL),(28,NULL,'Ice Heal',NULL),(29,NULL,'Full Restore',NULL),(30,NULL,'Full Heal',NULL);
/*!40000 ALTER TABLE `Bag_Items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Battle`
--

DROP TABLE IF EXISTS `Battle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Battle` (
  `Battle_Number` int NOT NULL,
  `Battle_Type` varchar(50) DEFAULT NULL,
  `Pokemon_Used` int DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Outcome` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Battle_Number`),
  KEY `Pokemon_Used` (`Pokemon_Used`),
  CONSTRAINT `Battle_ibfk_1` FOREIGN KEY (`Pokemon_Used`) REFERENCES `Owned_Pokemon` (`Poke_Number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Battle`
--

LOCK TABLES `Battle` WRITE;
/*!40000 ALTER TABLE `Battle` DISABLE KEYS */;
INSERT INTO `Battle` VALUES (1,'Gym Battle',63,'2024-11-01','Win'),(2,'Normal Battle',65,'2024-11-02','Win'),(3,'Gym Battle',15,'2024-11-05','Win'),(4,'Normal Battle',9,'2024-11-06','Loss'),(5,'Gym Battle',1,'2024-11-07','Win'),(6,'Normal Battle',12,'2024-11-08','Win'),(7,'Gym Battle',10,'2024-11-10','Win'),(8,'Gym Battle',6,'2024-11-12','Win'),(9,'Gym Battle',4,'2024-11-14','Loss'),(10,'Gym Battle',5,'2024-11-16','Win'),(11,'Normal Battle',148,'2024-11-18','Win'),(12,'Normal Battle',149,'2024-11-20','Win');
/*!40000 ALTER TABLE `Battle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Battling_Gym_Leader`
--

DROP TABLE IF EXISTS `Battling_Gym_Leader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Battling_Gym_Leader` (
  `Battle_Number` int DEFAULT NULL,
  `Pokemon_Number` int DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL,
  KEY `Battle_Number` (`Battle_Number`),
  KEY `Pokemon_Number` (`Pokemon_Number`),
  CONSTRAINT `Battling_Gym_Leader_ibfk_1` FOREIGN KEY (`Battle_Number`) REFERENCES `Gym_Battle` (`Battle_Number`) ON DELETE CASCADE,
  CONSTRAINT `Battling_Gym_Leader_ibfk_2` FOREIGN KEY (`Pokemon_Number`) REFERENCES `Owned_Pokemon` (`Poke_Number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Battling_Gym_Leader`
--

LOCK TABLES `Battling_Gym_Leader` WRITE;
/*!40000 ALTER TABLE `Battling_Gym_Leader` DISABLE KEYS */;
INSERT INTO `Battling_Gym_Leader` VALUES (1,63,'Pewter City'),(3,15,'Cerulean City'),(5,1,'Vermilion City'),(7,10,'Celadon City'),(8,6,'Fuchsia City'),(9,4,'Saffron City'),(10,5,'Cinnabar Island');
/*!40000 ALTER TABLE `Battling_Gym_Leader` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Battling_Rival_Trainer`
--

DROP TABLE IF EXISTS `Battling_Rival_Trainer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Battling_Rival_Trainer` (
  `Battle_Number` int NOT NULL,
  `Pokemon_Number` int NOT NULL,
  `Trainer_No` int DEFAULT NULL,
  PRIMARY KEY (`Battle_Number`,`Pokemon_Number`),
  KEY `Pokemon_Number` (`Pokemon_Number`),
  KEY `Trainer_No` (`Trainer_No`),
  CONSTRAINT `Battling_Rival_Trainer_ibfk_1` FOREIGN KEY (`Battle_Number`) REFERENCES `Normal_Battle` (`Battle_Number`) ON DELETE CASCADE,
  CONSTRAINT `Battling_Rival_Trainer_ibfk_2` FOREIGN KEY (`Pokemon_Number`) REFERENCES `Owned_Pokemon` (`Poke_Number`) ON DELETE CASCADE,
  CONSTRAINT `Battling_Rival_Trainer_ibfk_3` FOREIGN KEY (`Trainer_No`) REFERENCES `Rival_Trainer` (`Trainer_No`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Battling_Rival_Trainer`
--

LOCK TABLES `Battling_Rival_Trainer` WRITE;
/*!40000 ALTER TABLE `Battling_Rival_Trainer` DISABLE KEYS */;
INSERT INTO `Battling_Rival_Trainer` VALUES (2,65,201),(4,9,202),(6,12,203),(11,148,204),(12,149,205);
/*!40000 ALTER TABLE `Battling_Rival_Trainer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Berries`
--

DROP TABLE IF EXISTS `Berries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Berries` (
  `Item_Number` int NOT NULL,
  `Count` int DEFAULT NULL,
  `Effect` varchar(255) DEFAULT NULL,
  `Found_At` varchar(50) DEFAULT NULL,
  `Berry_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Item_Number`,`Berry_Name`),
  KEY `idx_berry_name` (`Berry_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Berries`
--

LOCK TABLES `Berries` WRITE;
/*!40000 ALTER TABLE `Berries` DISABLE KEYS */;
INSERT INTO `Berries` VALUES (1,10,'Heals 10 HP','Route 1','Oran Berry'),(2,10,'Restores PP for a move','Route 10','Leppa Berry'),(3,10,'Heals paralysis','Route 3','Cheri Berry'),(4,10,'Heals burn','Route 5','Chesto Berry'),(5,10,'Heals poison','Route 12','Pecha Berry'),(6,10,'Heals sleep','Route 8','Aspear Berry'),(7,10,'Heals freeze','Route 6','Iapapa Berry'),(8,10,'Cures confusion','Route 11','Tanga Berry');
/*!40000 ALTER TABLE `Berries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cure`
--

DROP TABLE IF EXISTS `Cure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cure` (
  `Cure` varchar(50) DEFAULT NULL,
  `Ail_Name` varchar(50) DEFAULT NULL,
  KEY `Ail_Name` (`Ail_Name`),
  CONSTRAINT `Cure_ibfk_1` FOREIGN KEY (`Ail_Name`) REFERENCES `Ailment_Type` (`Ail_Name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cure`
--

LOCK TABLES `Cure` WRITE;
/*!40000 ALTER TABLE `Cure` DISABLE KEYS */;
INSERT INTO `Cure` VALUES ('Antidote','Poison'),('Paralyze Heal','Paralysis'),('Burn Heal','Burn'),('Awakening','Sleep'),('Ice Heal','Freeze'),('Full Restore','Confusion'),('Full Heal','Flinching'),('Revive','Fainted');
/*!40000 ALTER TABLE `Cure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Gym_Battle`
--

DROP TABLE IF EXISTS `Gym_Battle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Gym_Battle` (
  `Battle_Number` int NOT NULL,
  `Gym` varchar(50) DEFAULT NULL,
  `Gym_Leader` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Battle_Number`),
  CONSTRAINT `Gym_Battle_ibfk_1` FOREIGN KEY (`Battle_Number`) REFERENCES `Battle` (`Battle_Number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Gym_Battle`
--

LOCK TABLES `Gym_Battle` WRITE;
/*!40000 ALTER TABLE `Gym_Battle` DISABLE KEYS */;
INSERT INTO `Gym_Battle` VALUES (1,'Pewter City','Brock'),(3,'Cerulean City','Misty'),(5,'Vermilion City','Lt. Surge'),(7,'Celadon City','Erika'),(8,'Fuchsia City','Koga'),(9,'Saffron City','Sabrina'),(10,'Cinnabar Island','Blaine');
/*!40000 ALTER TABLE `Gym_Battle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Move_Type`
--

DROP TABLE IF EXISTS `Move_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Move_Type` (
  `Move_Name` varchar(50) NOT NULL,
  `Poke_Name` varchar(50) NOT NULL,
  PRIMARY KEY (`Move_Name`,`Poke_Name`),
  KEY `Poke_Name` (`Poke_Name`),
  CONSTRAINT `Move_Type_ibfk_1` FOREIGN KEY (`Move_Name`) REFERENCES `Moves` (`Move_Name`) ON DELETE CASCADE,
  CONSTRAINT `Move_Type_ibfk_2` FOREIGN KEY (`Poke_Name`) REFERENCES `Owned_Pokemon` (`Poke_Name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Move_Type`
--

LOCK TABLES `Move_Type` WRITE;
/*!40000 ALTER TABLE `Move_Type` DISABLE KEYS */;
/*!40000 ALTER TABLE `Move_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Moves`
--

DROP TABLE IF EXISTS `Moves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Moves` (
  `Move_Name` varchar(50) NOT NULL,
  `Type` varchar(50) DEFAULT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `Power` int DEFAULT NULL,
  `Accuracy` float DEFAULT NULL,
  `Contact` tinyint(1) DEFAULT NULL,
  `PP` int DEFAULT NULL,
  `Pokemon_Number` int NOT NULL,
  PRIMARY KEY (`Move_Name`,`Pokemon_Number`),
  KEY `Pokemon_Number` (`Pokemon_Number`),
  CONSTRAINT `Moves_ibfk_1` FOREIGN KEY (`Pokemon_Number`) REFERENCES `Owned_Pokemon` (`Poke_Number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Moves`
--

LOCK TABLES `Moves` WRITE;
/*!40000 ALTER TABLE `Moves` DISABLE KEYS */;
INSERT INTO `Moves` VALUES ('Aerial Ace','Flying','Physical',60,NULL,1,20,18),('Agility','Psychic','Status',NULL,100,0,30,15),('Barrier','Psychic','Status',NULL,NULL,0,30,150),('Bite','Dark','Physical',60,100,1,25,8),('Bubble','Water','Special',40,100,0,30,8),('Confusion','Psychic','Special',50,100,0,25,12),('Confusion','Psychic','Special',50,100,0,25,63),('Cross Chop','Fighting','Physical',100,80,1,5,57),('Crunch','Dark','Physical',80,100,1,15,20),('Defense Curl','Normal','Status',NULL,NULL,0,40,74),('Dragon Rage','Dragon','Special',40,100,0,10,5),('Dragon Rage','Dragon','Special',40,100,0,10,147),('Dream Eater','Psychic','Special',100,100,0,15,94),('Earthquake','Ground','Physical',100,100,1,10,75),('Ember','Fire','Special',40,100,0,25,4),('Fire Spin','Fire','Special',35,85,0,15,6),('Flamethrower','Fire','Special',90,100,0,15,5),('Focus Energy','Normal','Status',NULL,100,0,30,56),('Gust','Flying','Special',40,100,0,35,12),('Hurricane','Flying','Special',110,70,0,10,18),('Hydro Pump','Water','Special',110,80,0,5,9),('Hyper Beam','Normal','Special',150,90,0,5,149),('Hyper Fang','Normal','Physical',80,90,1,15,19),('Hypnosis','Psychic','Status',NULL,60,0,20,92),('Iron Tail','Steel','Physical',100,75,1,15,26),('Karate Chop','Fighting','Physical',50,100,1,25,56),('Lick','Ghost','Physical',30,100,1,30,92),('Metronome','Normal','Status',NULL,NULL,0,10,151),('Outrage','Dragon','Physical',120,100,1,10,149),('Poison Sting','Poison','Physical',15,100,1,35,13),('Psybeam','Psychic','Special',65,100,0,20,65),('Psychic','Psychic','Special',90,100,0,10,150),('Quick Attack','Normal','Physical',40,100,1,30,16),('Quick Attack','Normal','Physical',40,100,1,30,25),('Rage','Normal','Physical',20,100,1,20,57),('Razor Leaf','Grass','Physical',55,95,1,25,2),('Recover','Psychic','Status',NULL,NULL,0,20,65),('Rock Slide','Rock','Physical',75,90,1,10,75),('Rock Throw','Rock','Physical',50,90,1,15,74),('Sand Attack','Ground','Status',NULL,100,0,15,16),('Scratch','Normal','Physical',40,100,1,35,4),('Shadow Ball','Ghost','Special',80,100,0,15,94),('Skull Bash','Normal','Physical',130,100,1,10,9),('Slam','Normal','Physical',80,75,1,20,148),('Sleep Powder','Grass','Status',NULL,75,0,15,2),('Sludge Bomb','Poison','Special',90,100,0,10,3),('Solar Beam','Grass','Special',120,100,0,10,3),('String Shot','Bug','Status',NULL,95,0,40,10),('String Shot','Bug','Status',NULL,95,0,40,13),('Super Fang','Normal','Physical',NULL,90,1,10,20),('Tackle','Normal','Physical',40,100,1,35,1),('Tackle','Normal','Physical',40,100,1,35,10),('Tail Whip','Normal','Status',NULL,100,0,30,19),('Teleport','Psychic','Status',NULL,NULL,0,20,63),('Thunder Shock','Electric','Special',40,100,0,30,25),('Thunder Wave','Electric','Status',NULL,90,0,20,148),('Thunderbolt','Electric','Special',90,100,0,15,26),('Transform','Normal','Status',NULL,NULL,0,10,151),('Twineedle','Bug','Physical',25,100,1,20,15),('Vine Whip','Grass','Physical',45,100,1,25,1),('Water Gun','Water','Special',40,100,0,25,7),('Wing Attack','Flying','Physical',60,100,1,35,6),('Withdraw','Water','Status',NULL,100,0,40,7),('Wrap','Normal','Physical',15,90,1,20,147);
/*!40000 ALTER TABLE `Moves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Normal_Battle`
--

DROP TABLE IF EXISTS `Normal_Battle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Normal_Battle` (
  `Battle_Number` int NOT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `Rival_ID` int DEFAULT NULL,
  PRIMARY KEY (`Battle_Number`),
  CONSTRAINT `Normal_Battle_ibfk_1` FOREIGN KEY (`Battle_Number`) REFERENCES `Battle` (`Battle_Number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Normal_Battle`
--

LOCK TABLES `Normal_Battle` WRITE;
/*!40000 ALTER TABLE `Normal_Battle` DISABLE KEYS */;
INSERT INTO `Normal_Battle` VALUES (2,'Route 1',201),(4,'Route 2',202),(6,'Route 3',203),(11,'Route 4',204),(12,'Route 5',205);
/*!40000 ALTER TABLE `Normal_Battle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Normal_Item`
--

DROP TABLE IF EXISTS `Normal_Item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Normal_Item` (
  `Item_Number` int NOT NULL,
  `Item_Name` varchar(50) NOT NULL,
  `Effect` varchar(255) DEFAULT NULL,
  `Cost` int DEFAULT NULL,
  `Count` int DEFAULT NULL,
  PRIMARY KEY (`Item_Number`,`Item_Name`),
  KEY `idx_item_name` (`Item_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Normal_Item`
--

LOCK TABLES `Normal_Item` WRITE;
/*!40000 ALTER TABLE `Normal_Item` DISABLE KEYS */;
INSERT INTO `Normal_Item` VALUES (1,'Potion','Heals 20 HP',200,50),(2,'Super Potion','Heals 50 HP',700,30),(3,'Hyper Potion','Heals 120 HP',1200,20),(4,'Max Potion','Fully heals HP',2500,10),(5,'Revive','Revives fainted Pokémon',1500,10),(6,'HP Up','Increases HP stat',2000,5),(7,'Protein','Increases Attack stat',2500,5),(8,'Iron','Increases Defense stat',2500,5),(9,'Antidote','Heals poison',100,20),(10,'Paralyze Heal','Heals paralysis',100,20),(11,'Awakening','Heals sleep',100,20),(12,'Burn Heal','Heals burn',100,20),(13,'Ice Heal','Heals freeze',100,20),(14,'Full Restore','Fully heals HP and cures status',3000,10),(15,'Full Heal','Cures flinching',200,20);
/*!40000 ALTER TABLE `Normal_Item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Owned_Pokemon`
--

DROP TABLE IF EXISTS `Owned_Pokemon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Owned_Pokemon` (
  `Poke_Number` int NOT NULL,
  `Poke_Name` varchar(50) DEFAULT NULL,
  `Height` float DEFAULT NULL,
  `Weight` float DEFAULT NULL,
  `Type` varchar(50) DEFAULT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `XP` int DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `HP` int DEFAULT NULL,
  `Level` int DEFAULT NULL,
  `Special_Attack` int DEFAULT NULL,
  `Attack` int DEFAULT NULL,
  `Defence` int DEFAULT NULL,
  `Special_Defence` int DEFAULT NULL,
  `Speed` int DEFAULT NULL,
  PRIMARY KEY (`Poke_Number`),
  KEY `idx_poke_name` (`Poke_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Owned_Pokemon`
--

LOCK TABLES `Owned_Pokemon` WRITE;
/*!40000 ALTER TABLE `Owned_Pokemon` DISABLE KEYS */;
INSERT INTO `Owned_Pokemon` VALUES (1,'Bulbasaur',0.7,6.9,'Grass/Poison','Seed',100,'Male',45,5,49,49,49,65,45),(2,'Ivysaur',1,13,'Grass/Poison','Seed',200,'Female',60,16,63,62,63,80,60),(3,'Venusaur',2,100,'Grass/Poison','Seed',300,'Male',80,32,122,82,83,100,80),(4,'Charmander',0.6,8.5,'Fire','Lizard',100,'Female',39,5,52,52,43,50,65),(5,'Charmeleon',1.1,19,'Fire','Flame',200,'Male',58,16,64,64,58,65,80),(6,'Charizard',1.7,90.5,'Fire/Flying','Flame',300,'Female',78,36,109,84,78,85,100),(7,'Squirtle',0.5,9,'Water','Tiny Turtle',100,'Male',44,5,50,48,65,64,43),(8,'Wartortle',1,22.5,'Water','Turtle',200,'Female',59,16,65,63,80,80,58),(9,'Blastoise',1.6,85.5,'Water','Shellfish',300,'Male',79,36,85,83,100,105,78),(10,'Caterpie',0.3,2.9,'Bug','Worm',39,'Female',45,3,20,30,35,20,45),(12,'Butterfree',1.1,32,'Bug/Flying','Butterfly',178,'Male',60,10,90,45,50,80,70),(13,'Weedle',0.3,3.2,'Bug/Poison','Hairy Bug',39,'Male',40,3,20,35,30,20,50),(15,'Beedrill',1,29.5,'Bug/Poison','Poison Bee',178,'Female',65,10,45,90,40,80,75),(16,'Pidgey',0.3,1.8,'Normal/Flying','Tiny Bird',50,'Male',40,5,35,45,40,35,56),(18,'Pidgeot',1.5,39.5,'Normal/Flying','Bird',216,'Female',83,36,70,80,75,70,101),(19,'Rattata',0.3,3.5,'Normal','Mouse',51,'Male',30,3,25,56,35,25,72),(20,'Raticate',0.7,18.5,'Normal','Mouse',145,'Female',55,20,50,81,60,50,97),(25,'Pikachu',0.4,6,'Electric','Mouse',112,'Male',35,10,50,55,40,50,90),(26,'Raichu',0.8,30,'Electric','Mouse',218,'Female',60,26,90,85,55,80,110),(56,'Mankey',0.5,28,'Fighting','Pig Monkey',61,'Male',40,5,35,80,35,45,70),(57,'Primeape',1,32,'Fighting','Pig Monkey',159,'Female',65,28,60,105,60,70,95),(63,'Abra',0.9,19.5,'Psychic','Psi',62,'Female',25,5,105,20,15,55,90),(65,'Alakazam',1.5,48,'Psychic','Psi',225,'Male',55,36,135,50,45,95,120),(74,'Geodude',0.4,20,'Rock/Ground','Rock',86,'Male',40,10,30,80,100,30,20),(75,'Graveler',1,105,'Rock/Ground','Rock',134,'Male',55,25,45,95,115,45,35),(92,'Gastly',1.3,0.1,'Ghost/Poison','Gas',62,'Male',30,5,100,35,30,35,80),(94,'Gengar',1.5,40.5,'Ghost/Poison','Shadow',225,'Female',60,36,130,65,60,75,110),(147,'Dratini',1.8,3.3,'Dragon','Dragon',60,'Male',41,5,50,64,45,50,50),(148,'Dragonair',4,16.5,'Dragon','Dragon',147,'Female',61,30,70,84,65,70,70),(149,'Dragonite',2.2,210,'Dragon/Flying','Dragon',270,'Male',91,55,100,134,95,100,80),(150,'Mewtwo',2,122,'Psychic','Genetic',306,'Genderless',106,70,154,110,90,154,130),(151,'Mew',0.4,4,'Psychic','New Species',270,'Genderless',100,70,100,100,100,100,100);
/*!40000 ALTER TABLE `Owned_Pokemon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Poke_Type`
--

DROP TABLE IF EXISTS `Poke_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Poke_Type` (
  `Pokemon_Number` int NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Weak_Against` varchar(50) DEFAULT NULL,
  `Immune_To` varchar(50) DEFAULT NULL,
  `Strong_Against` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Pokemon_Number`,`Type`),
  CONSTRAINT `Poke_Type_ibfk_1` FOREIGN KEY (`Pokemon_Number`) REFERENCES `Owned_Pokemon` (`Poke_Number`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Poke_Type`
--

LOCK TABLES `Poke_Type` WRITE;
/*!40000 ALTER TABLE `Poke_Type` DISABLE KEYS */;
INSERT INTO `Poke_Type` VALUES (1,'Grass','Fire',NULL,'Water'),(1,'Poison','Psychic',NULL,'Grass'),(2,'Grass','Fire',NULL,'Water'),(2,'Poison','Psychic',NULL,'Grass'),(3,'Grass','Fire',NULL,'Water'),(3,'Poison','Psychic',NULL,'Grass'),(4,'Fire','Water',NULL,'Grass'),(5,'Fire','Water',NULL,'Grass'),(6,'Fire','Water',NULL,'Grass'),(6,'Flying','Electric','Ground','Fighting'),(7,'Water','Electric',NULL,'Fire'),(8,'Water','Electric',NULL,'Fire'),(9,'Water','Electric',NULL,'Fire'),(10,'Bug','Fire',NULL,'Grass'),(12,'Bug','Fire',NULL,'Grass'),(12,'Flying','Electric','Ground','Fighting'),(13,'Bug','Fire',NULL,'Grass'),(15,'Bug','Fire',NULL,'Grass'),(15,'Poison','Psychic',NULL,'Grass'),(16,'Flying','Electric','Ground','Fighting'),(16,'Normal','Fighting',NULL,NULL),(18,'Flying','Electric','Ground','Fighting'),(18,'Normal','Fighting',NULL,NULL),(19,'Normal','Fighting',NULL,NULL),(20,'Normal','Fighting',NULL,NULL),(25,'Electric','Ground',NULL,'Flying'),(26,'Electric','Ground',NULL,'Flying'),(56,'Fighting','Psychic',NULL,'Normal'),(57,'Fighting','Psychic',NULL,'Normal'),(63,'Psychic','Bug',NULL,'Fighting'),(65,'Psychic','Bug',NULL,'Fighting'),(74,'Ground','Water','Electric','Fire'),(74,'Rock','Water',NULL,'Fire'),(75,'Ground','Water','Electric','Fire'),(75,'Rock','Water',NULL,'Fire'),(92,'Ghost','Dark','Normal','Psychic'),(92,'Poison','Psychic',NULL,'Grass'),(94,'Ghost','Dark','Normal','Psychic'),(94,'Poison','Psychic',NULL,'Grass'),(147,'Dragon','Ice',NULL,'Dragon'),(148,'Dragon','Ice',NULL,'Dragon'),(149,'Dragon','Ice',NULL,'Dragon'),(149,'Flying','Electric','Ground','Fighting'),(150,'Psychic','Bug',NULL,'Fighting'),(151,'Psychic','Bug',NULL,'Fighting');
/*!40000 ALTER TABLE `Poke_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pokeball`
--

DROP TABLE IF EXISTS `Pokeball`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pokeball` (
  `Item_Number` int NOT NULL,
  `Count` int DEFAULT NULL,
  `Catch_Rate` float DEFAULT NULL,
  `Cost` int DEFAULT NULL,
  `Type` varchar(50) NOT NULL,
  PRIMARY KEY (`Item_Number`,`Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pokeball`
--

LOCK TABLES `Pokeball` WRITE;
/*!40000 ALTER TABLE `Pokeball` DISABLE KEYS */;
INSERT INTO `Pokeball` VALUES (1,50,1,200,'Pokéball'),(2,30,1.5,600,'Great Ball'),(3,20,2,1200,'Ultra Ball'),(4,10,3,3000,'Master Ball'),(5,40,1.2,300,'Heal Ball'),(6,40,1,400,'Premier Ball'),(7,50,1,150,'Safari Ball');
/*!40000 ALTER TABLE `Pokeball` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pokemon_Gym`
--

DROP TABLE IF EXISTS `Pokemon_Gym`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pokemon_Gym` (
  `Location` varchar(50) NOT NULL,
  `Badge_Won` tinyint(1) DEFAULT NULL,
  `Gym_Badge` varchar(50) DEFAULT NULL,
  `Gym_Type` varchar(50) DEFAULT NULL,
  `Gym_Leader` varchar(50) DEFAULT NULL,
  `Previous_Gym` varchar(50) DEFAULT NULL,
  `Next_Gym` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Location`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pokemon_Gym`
--

LOCK TABLES `Pokemon_Gym` WRITE;
/*!40000 ALTER TABLE `Pokemon_Gym` DISABLE KEYS */;
INSERT INTO `Pokemon_Gym` VALUES ('Celadon City',1,'Rainbow Badge','Grass','Erika','Vermilion City','Fuchsia City'),('Cerulean City',1,'Cascade Badge','Water','Misty','Pewter City','Vermilion City'),('Cinnabar Island',0,'Volcano Badge','Fire','Blaine','Saffron City','Viridian City'),('Fuchsia City',1,'Soul Badge','Poison','Koga','Celadon City','Saffron City'),('Pewter City',1,'Boulder Badge','Rock','Brock',NULL,'Cerulean City'),('Saffron City',0,'Marsh Badge','Psychic','Sabrina','Fuchsia City','Cinnabar Island'),('Vermilion City',1,'Thunder Badge','Electric','Lt. Surge','Cerulean City','Celadon City'),('Viridian City',0,'Earth Badge','Ground','Giovanni','Cinnabar Island',NULL);
/*!40000 ALTER TABLE `Pokemon_Gym` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rival_Trainer`
--

DROP TABLE IF EXISTS `Rival_Trainer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rival_Trainer` (
  `Trainer_No` int NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Trainer_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rival_Trainer`
--

LOCK TABLES `Rival_Trainer` WRITE;
/*!40000 ALTER TABLE `Rival_Trainer` DISABLE KEYS */;
INSERT INTO `Rival_Trainer` VALUES (201,'Gary'),(202,'Blue'),(203,'Silver'),(204,'Brendan'),(205,'May'),(206,'Wally');
/*!40000 ALTER TABLE `Rival_Trainer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29  0:24:58
