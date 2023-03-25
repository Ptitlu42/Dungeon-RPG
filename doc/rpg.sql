-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : sam. 25 mars 2023 à 23:11
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `rpg`
--

-- --------------------------------------------------------

--
-- Structure de la table `caracter`
--

DROP TABLE IF EXISTS `caracter`;
CREATE TABLE IF NOT EXISTS `caracter` (
  `strenght` int NOT NULL,
  `life` int NOT NULL,
  `speed` int NOT NULL,
  `constitution` int NOT NULL,
  `action_point` int NOT NULL,
  `inventory` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `equiped_stuff` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `carac_sprite` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `caracter`
--

INSERT INTO `caracter` (`strenght`, `life`, `speed`, `constitution`, `action_point`, `inventory`, `equiped_stuff`, `carac_sprite`) VALUES
(20, 100, 10, 10, 8, 'empty', 'empty', 1);

-- --------------------------------------------------------

--
-- Structure de la table `item`
--

DROP TABLE IF EXISTS `item`;
CREATE TABLE IF NOT EXISTS `item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `equipable` tinyint(1) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `emplacement` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `strenght_mod` int NOT NULL,
  `life_mod` int NOT NULL,
  `speed_mod` int NOT NULL,
  `const_mod` int NOT NULL,
  `ap_mod` int NOT NULL,
  `heal` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `item`
--

INSERT INTO `item` (`id`, `equipable`, `name`, `emplacement`, `strenght_mod`, `life_mod`, `speed_mod`, `const_mod`, `ap_mod`, `heal`) VALUES
(1, 1, 'Casque nul', 'helmet', 5, 10, 2, 2, 0, 0),
(2, 1, 'Casque cool', 'helmet', 10, 20, 4, 4, 0, 0),
(3, 1, 'Armure ravivante', 'chesplate', 0, 20, 0, 5, 1, 0),
(4, 1, 'Potion de soin', 'potion', 0, 0, 0, 0, 0, 20);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
