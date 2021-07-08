/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.1.36-community-log : Database - kl
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`kl` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `kl`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `checkin` time NOT NULL,
  `checkout` time DEFAULT NULL,
  `adate` date DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`emp_id`,`checkin`,`checkout`,`adate`) values (1,5,'00:00:09','00:00:19','0000-00-00'),(2,6,'00:00:00','00:00:07','2000-03-03'),(3,5,'13:56:59','13:57:19','2020-01-30'),(4,5,'11:04:28','11:04:43','2020-02-13'),(5,5,'11:04:37','11:04:43','2020-02-13');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(20) NOT NULL,
  `complaint1` varchar(20) NOT NULL,
  `cdate` date NOT NULL,
  `reply` varchar(20) NOT NULL,
  `reply_date` date NOT NULL,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`comp_id`,`emp_id`,`complaint1`,`cdate`,`reply`,`reply_date`) values (1,5,'jdfkf','0000-00-00','ok','2020-02-23'),(2,2,'dk','0000-00-00','','0000-00-00'),(3,5,'jhugiugukgu','2020-01-23','','0000-00-00'),(4,5,'oihih','2020-01-23','','0000-00-00'),(5,5,'project','2020-01-23','','0000-00-00'),(6,5,'so poor','2020-01-30','ok','2020-02-13'),(7,5,'','2020-02-06','','0000-00-00'),(8,5,'pycharm','2020-02-12','','0000-00-00'),(9,5,'ds[paiodposi','2020-02-13','','0000-00-00'),(10,5,'nsdah','2020-02-13','','0000-00-00'),(11,5,'amal','2020-02-15','','0000-00-00'),(12,5,'ourewur','2020-02-21','','0000-00-00');

/*Table structure for table `dept` */

DROP TABLE IF EXISTS `dept`;

CREATE TABLE `dept` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `dept` */

insert  into `dept`(`dept_id`,`name`,`email`) values (2,'mba',NULL),(10,'bca','julia@gmail'),(12,'bba',NULL),(18,'dfddf','dfsdfdsf'),(20,'',''),(21,'','');

/*Table structure for table `emp` */

DROP TABLE IF EXISTS `emp`;

CREATE TABLE `emp` (
  `emp_id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `post` varchar(20) NOT NULL,
  `house` varchar(20) NOT NULL,
  `street` varchar(20) NOT NULL,
  `Place` varchar(20) NOT NULL,
  `district` varchar(20) NOT NULL,
  `pin_code` int(11) NOT NULL,
  `mob_no` int(11) NOT NULL,
  `email` varchar(20) NOT NULL,
  `gender` char(1) NOT NULL,
  `DOB` varchar(11) NOT NULL,
  `dept_id` int(11) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `emp` */

insert  into `emp`(`emp_id`,`first_name`,`last_name`,`post`,`house`,`street`,`Place`,`district`,`pin_code`,`mob_no`,`email`,`gender`,`DOB`,`dept_id`,`photo`,`login_id`) values (5,'amal','joseph','kallu','malamel','kalluvayal','iritty','kannur',670703,789780000,'amalmakln@gamil.com','F','2020-09-09',10,'static/employee/191203-134158.jpg',5),(6,'julia','ryuyu','yjjjky','tyuty','fgfdg','juyhgtfd','oikjuhygtf',9876,2345678,'gf@gmail.com','F','2019',10,'static/employee/191211-123424.jpg',6),(16,'arun','lal','kdns','kap','ajs','kd','',0,1234,'arun@gmail.com','F','2020',32,'3',16),(19,'melbin','joz','hdui','dgsug','jdguis','jhgdsyu','kjdgs',670703,876,'ww','M','2020',0,'18',19);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `ftype` varchar(20) NOT NULL,
  `fdate` datetime NOT NULL,
  `userid` int(11) NOT NULL,
  `workid` int(11) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`ftype`,`fdate`,`userid`,`workid`) values (2,'bad','2019-09-09 00:00:00',5,NULL),(4,'good','2019-09-09 00:00:00',4,NULL),(5,'uygu','2020-01-23 00:00:00',5,5),(6,'ohj','2020-01-23 00:00:00',5,5),(7,'bad','2020-01-30 00:00:00',5,5),(8,'poor','2020-01-30 00:00:00',5,5),(9,'lkjfiojds','2020-02-13 00:00:00',5,5),(10,'jsj','2020-02-13 00:00:00',5,5),(11,'soiahd','2020-02-21 00:00:00',5,5);

/*Table structure for table `file` */

DROP TABLE IF EXISTS `file`;

CREATE TABLE `file` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `ffile` varchar(500) NOT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `fdate` int(11) NOT NULL,
  `workid` int(11) DEFAULT NULL,
  `emp_id` int(11) NOT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `file` */

insert  into `file`(`file_id`,`ffile`,`description`,`fdate`,`workid`,`emp_id`) values (1,'static/employee/200123-155320WIN_20191114_11_17_44_Pro.jpg','\"+dt+\"',0,9,0),(2,'static/employee/200123-155104WIN_20190701_18_11_29_Pro.jpg','dddd',20200123,8,0),(3,'static/employee/200123-155320WIN_20191114_11_17_44_Pro.jpg','xssdsdde',20200123,8,0),(4,'static/employee/200130-101528','iusahiuh',20200130,7,0),(5,'static/employee/200130-103324WIN_20191114_11_17_41_Pro.jpg','oiduyoi',20200130,6,0),(6,'static/employee/200130-111445WIN_20191114_11_17_41_Pro.jpg','hdkuwhd',20200130,5,0),(7,'static/employee/200130-111807WIN_20191114_11_17_41_Pro.jpg','fghf',20200130,4,0),(8,'static/employee/200213-115712WIN_20191114_11_17_41_Pro.jpg','hshs',20200213,3,0),(9,'static/employee/200213-141637p1.pdf','khsajh',20200213,1,0),(10,'static/employee/200213-145415p1.pdf','jkh',20200213,2,5),(11,'static/employee/200215-152837p1.pdf','good',20200215,5,5);

/*Table structure for table `fileshare` */

DROP TABLE IF EXISTS `fileshare`;

CREATE TABLE `fileshare` (
  `file_id` int(12) NOT NULL AUTO_INCREMENT,
  `fname` varchar(200) DEFAULT NULL,
  `ffile` varchar(200) DEFAULT NULL,
  `send_id` int(12) NOT NULL,
  `rec_id` int(12) NOT NULL,
  `fdate` date DEFAULT NULL,
  `hashvalue` varchar(200) DEFAULT NULL,
  `filesize` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fileshare` */

insert  into `fileshare`(`file_id`,`fname`,`ffile`,`send_id`,`rec_id`,`fdate`,`hashvalue`,`filesize`) values (1,'qq.txt','1.txt',5,6,'2020-02-23','63a540b5f8df63f2b176a3019827d7a5','82');

/*Table structure for table `imei` */

DROP TABLE IF EXISTS `imei`;

CREATE TABLE `imei` (
  `imeiid` int(11) NOT NULL AUTO_INCREMENT,
  `imei1` varchar(20) DEFAULT NULL,
  `emp_id` int(11) NOT NULL,
  PRIMARY KEY (`imeiid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `imei` */

insert  into `imei`(`imeiid`,`imei1`,`emp_id`) values (1,'hjsgjk',2),(2,'6737823',0),(3,'62781',0),(4,'567156',0),(5,'4536',0),(6,'562537',0),(7,'562537',0),(8,'562537',0),(9,'465243542163',0);

/*Table structure for table `leave1` */

DROP TABLE IF EXISTS `leave1`;

CREATE TABLE `leave1` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `ldate` date NOT NULL,
  `lreason` varchar(100) NOT NULL,
  `status` varchar(30) DEFAULT 'pending',
  PRIMARY KEY (`l_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `leave1` */

insert  into `leave1`(`l_id`,`emp_id`,`ldate`,`lreason`,`status`) values (1,0,'0000-00-00','amkn','pending'),(2,0,'2020-01-15','lkcjdflksjidohl','pending'),(3,0,'2020-01-15','lkcjdflksjidohl','pending'),(4,5,'2020-01-14','lsdjposajjulia','pending'),(5,5,'0000-00-00','gkjkijhl','pending'),(6,5,'0000-00-00','fdfhbfdh','pending'),(7,5,'0000-00-00','oriueiosu','pending'),(8,5,'0000-00-00','amal','pending');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `passwd` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`name`,`passwd`,`type`) values (1,'w','emp','employee'),(2,'anmal@gmail.com','emp','employee'),(3,'k','emp','employee'),(4,'j','emp','employee'),(5,'amalmakln@gamil.com','emp','employee'),(6,'gf@gmail.com','emp','employee'),(7,'huhw','emp','employee'),(8,'k@ll','emp','employee'),(9,'k@ll','emp','employee'),(10,'dep','dep','department'),(11,'admin','admin','admin'),(12,'jdsdhksdn','19572','department'),(13,'julia@gmail.com','17662','department'),(14,'julia@gmail.com','82147','department'),(15,'bba@gmail.com','77123','department'),(16,'arun@gmail.com','emp','employee'),(17,'julia@gmail.com','59963','department'),(18,'dfsdfdsf','53829','department'),(19,'ww','emp','employee'),(20,'','6675','department'),(21,'','2343','department');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `workid` int(11) NOT NULL AUTO_INCREMENT,
  `dep_id` int(20) NOT NULL,
  `w_work` varchar(20) NOT NULL,
  PRIMARY KEY (`workid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

insert  into `work`(`workid`,`dep_id`,`w_work`) values (5,0,'hjgg'),(11,0,'djj'),(12,0,'djj'),(13,10,'kjdbj'),(14,17,'amal'),(15,17,'amal'),(16,3,'amal'),(17,3,'amjhvf'),(18,3,'amjjhcvh'),(19,10,'djj'),(20,12,'djj');

/*Table structure for table `work_status` */

DROP TABLE IF EXISTS `work_status`;

CREATE TABLE `work_status` (
  `status_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `work_id` int(11) NOT NULL,
  `status` varchar(500) NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `work_status` */

insert  into `work_status`(`status_id`,`emp_id`,`work_id`,`status`,`date`) values (1,5,5,'5','2020-02-13'),(2,5,5,'5','2020-02-13'),(3,5,5,'5','2020-02-13'),(4,5,5,'jkh','2020-02-13'),(5,5,5,'better','2020-02-15');

/*Table structure for table `workassign` */

DROP TABLE IF EXISTS `workassign`;

CREATE TABLE `workassign` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `workid` int(11) NOT NULL,
  `work_status` varchar(20) NOT NULL,
  `emp_id` int(11) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `workassign` */

insert  into `workassign`(`assign_id`,`workid`,`work_status`,`emp_id`,`date`) values (1,5,'PENDING',5,'0000-00-00'),(2,6,'ihds',8,'0000-00-00'),(3,6,'jqoj',3,'0000-00-00'),(4,13,'',5,'2020-02-15'),(5,13,'',7,'2020-02-23'),(6,13,'',6,'2020-03-23');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
