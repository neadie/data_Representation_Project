-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 05, 2020 at 01:18 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `data_representation_project2`
--

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `dept_no` char(4) NOT NULL,
  `dept_name` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`dept_no`, `dept_name`) VALUES
('0010', 'FreeStyle'),
('5678', 'Geography'),
('8777', 'PHYSICS'),
('0001', 'Sports And Leasure');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_no` int(11) NOT NULL,
  `birth_date` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01',
  `first_name` varchar(14) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `hire_date` timestamp NOT NULL DEFAULT '1970-01-01 00:00:01',
  `dept_no` char(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`emp_no`, `birth_date`, `first_name`, `last_name`, `hire_date`, `dept_no`) VALUES
(11, '1970-01-01 00:00:01', 'Tommy', 'M', '1970-01-01 00:00:01', '0010'),
(12, '1970-01-01 00:00:01', 'Tommy', 'Mo', '1970-01-01 00:00:01', '0010'),
(20, '2020-11-11 00:00:00', 'John', 'Rowing', '2020-11-25 00:00:00', '0010'),
(25, '2020-10-28 00:00:00', 'Finbar', 'Frawley', '2020-11-03 00:00:00', '0010'),
(26, '2020-10-28 00:00:00', 'Finbar', 'Frawley', '2020-11-03 00:00:00', '0010'),
(27, '2020-11-04 00:00:00', 'Finbar', 'Frawley', '2020-11-24 00:00:00', '5678');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`dept_no`),
  ADD UNIQUE KEY `dept_name` (`dept_name`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`emp_no`),
  ADD KEY `dept_fk` (`dept_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `emp_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `employees`
--
ALTER TABLE `employees`
  ADD CONSTRAINT `dept_fk` FOREIGN KEY (`dept_no`) REFERENCES `departments` (`dept_no`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
