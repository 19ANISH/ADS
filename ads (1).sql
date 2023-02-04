-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2023 at 04:15 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ads`
--

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE `branch` (
  `branch_id` int(11) NOT NULL,
  `branch_name` varchar(40) DEFAULT NULL,
  `mgr_id` int(11) DEFAULT NULL,
  `mgr_start_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`branch_id`, `branch_name`, `mgr_id`, `mgr_start_date`) VALUES
(1, 'corporate', 100, '1990-05-01'),
(2, 'scranton', 102, '1992-04-06'),
(3, 'stamford', 103, '1998-02-13'),
(4, 'india', 104, '1992-12-01');

-- --------------------------------------------------------

--
-- Table structure for table `branch supplier`
--

CREATE TABLE `branch supplier` (
  `branch_id` int(11) NOT NULL,
  `supplier_name` varchar(25) NOT NULL,
  `supply_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branch supplier`
--

INSERT INTO `branch supplier` (`branch_id`, `supplier_name`, `supply_type`) VALUES
(2, 'Hammer Mill', 'Paper'),
(2, 'Uni-Ball', 'Writing Utensils'),
(3, 'Patriot Paper', 'Paper'),
(2, 'JT Forms and Labels', 'Custom Form'),
(3, 'Stamford Labels', 'Custom Forms');

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `client_id` int(11) NOT NULL,
  `client_name` varchar(40) NOT NULL,
  `branch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`client_id`, `client_name`, `branch_id`) VALUES
(400, 'Dunmore Highschool', 2),
(401, 'Lackawana Country', 2),
(402, 'FedEx', 3),
(403, 'John Daly Law,LLC', 3),
(404, 'Scranton Whitepages', 2),
(405, 'Times Newspaper', 3),
(406, 'FedEx', 2);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `emp_id` int(11) NOT NULL,
  `first_name` varchar(10) NOT NULL,
  `last_name` varchar(12) NOT NULL,
  `birth_date` date NOT NULL,
  `sex` varchar(1) NOT NULL,
  `salary` int(11) NOT NULL,
  `super_id` int(11) NOT NULL,
  `branch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id`) VALUES
(100, 'jan', 'levison', '1961-05-11', 'F', 110000, 100, 1),
(101, 'michael', 'scott', '1964-03-15', 'M', 75000, 102, 1),
(102, 'josh', 'potter', '1964-09-05', 'M', 78000, 103, 2),
(103, 'dan', 'daniles', '1990-02-28', 'F', 90000, 101, 3),
(104, 'Kelly', 'Kapoor', '1900-02-05', 'F', 55000, 102, 2),
(105, 'Stanley', 'Hudson', '2014-06-11', 'M', 69000, 102, 2),
(106, 'Josh', 'Porter', '1969-09-05', 'M', 98000, 100, 3),
(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3),
(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);

-- --------------------------------------------------------

--
-- Table structure for table `horizontal`
--

CREATE TABLE `horizontal` (
  `emp_id` int(11) NOT NULL,
  `first_name` varchar(10) NOT NULL,
  `last_name` varchar(12) NOT NULL,
  `birth_date` date NOT NULL,
  `sex` varchar(1) NOT NULL,
  `salary` int(11) NOT NULL,
  `super_id` int(11) NOT NULL,
  `branch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `horizontal`
--

INSERT INTO `horizontal` (`emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id`) VALUES
(100, 'jan', 'levison', '1961-05-11', 'F', 110000, 100, 1),
(103, 'dan', 'daniles', '1990-02-28', 'F', 90000, 101, 3),
(106, 'Josh', 'Porter', '1969-09-05', 'M', 98000, 100, 3);

-- --------------------------------------------------------

--
-- Table structure for table `horizontalother`
--

CREATE TABLE `horizontalother` (
  `emp_id` int(11) NOT NULL,
  `first_name` varchar(10) NOT NULL,
  `last_name` varchar(12) NOT NULL,
  `birth_date` date NOT NULL,
  `sex` varchar(1) NOT NULL,
  `salary` int(11) NOT NULL,
  `super_id` int(11) NOT NULL,
  `branch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `horizontalother`
--

INSERT INTO `horizontalother` (`emp_id`, `first_name`, `last_name`, `birth_date`, `sex`, `salary`, `super_id`, `branch_id`) VALUES
(101, 'michael', 'scott', '1964-03-15', 'M', 75000, 102, 1),
(102, 'josh', 'potter', '1964-09-05', 'M', 78000, 103, 2),
(104, 'Kelly', 'Kapoor', '1900-02-05', 'F', 55000, 102, 2),
(105, 'Stanley', 'Hudson', '2014-06-11', 'M', 69000, 102, 2),
(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3),
(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `branch`
--
ALTER TABLE `branch`
  ADD PRIMARY KEY (`branch_id`),
  ADD KEY `mgr_id` (`mgr_id`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`client_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`emp_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `branch`
--
ALTER TABLE `branch`
  ADD CONSTRAINT `branch_ibfk_1` FOREIGN KEY (`mgr_id`) REFERENCES `employee` (`emp_id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
