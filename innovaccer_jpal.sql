-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 20, 2014 at 07:24 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `innovaccer_jpal`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_log`
--

CREATE TABLE IF NOT EXISTS `activity_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(20) NOT NULL,
  `action` varchar(50) NOT NULL,
  `entity` varchar(20) NOT NULL,
  `entity_id` varchar(20) NOT NULL,
  `last_updated` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `de_surveyor`
--

CREATE TABLE IF NOT EXISTS `de_surveyor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_id` varchar(20) NOT NULL,
  `de_id` varchar(20) NOT NULL,
  `survey_id` varchar(20) NOT NULL,
  `last_updated` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  KEY `p_id` (`p_id`),
  KEY `de_id` (`de_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `flag_check`
--

CREATE TABLE IF NOT EXISTS `flag_check` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `s_id` varchar(20) NOT NULL,
  `p_id` varchar(20) NOT NULL,
  `flagged_quest` longtext NOT NULL,
  `last_updated` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `project_table`
--

CREATE TABLE IF NOT EXISTS `project_table` (
  `id` varchar(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `time_stamp` timestamp NOT NULL,
  `pm_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pm_id` (`pm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE IF NOT EXISTS `role` (
  `role_id` varchar(10) NOT NULL,
  `role_desc` varchar(20) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `user_id` varchar(100) NOT NULL,
  `f_name` varchar(150) NOT NULL,
  `l_name` varchar(150) NOT NULL,
  `company` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `login_id` varchar(150) NOT NULL,
  `login_password` varchar(100) NOT NULL,
  `photo_path` varchar(200) NOT NULL,
  `primary_phone` varchar(50) NOT NULL,
  `secondary_phone` varchar(50) NOT NULL,
  `address` varchar(300) NOT NULL,
  `line_1` varchar(300) NOT NULL,
  `line_2` varchar(300) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `role` varchar(10) NOT NULL,
  `last_updated` timestamp NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `role` (`role`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `activity_log`
--
ALTER TABLE `activity_log`
  ADD CONSTRAINT `activity_log_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `de_surveyor`
--
ALTER TABLE `de_surveyor`
  ADD CONSTRAINT `de_surveyor_ibfk_2` FOREIGN KEY (`de_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `de_surveyor_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `flag_check`
--
ALTER TABLE `flag_check`
  ADD CONSTRAINT `flag_check_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `project_table`
--
ALTER TABLE `project_table`
  ADD CONSTRAINT `project_table_ibfk_1` FOREIGN KEY (`pm_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_2` FOREIGN KEY (`role`) REFERENCES `role` (`role_id`),
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role`) REFERENCES `role` (`role_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
