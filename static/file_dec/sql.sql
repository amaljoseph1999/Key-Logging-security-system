/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.1.36-community-log : Database - cseft
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`cseft` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cseft`;

/*Table structure for table `candidate` */

DROP TABLE IF EXISTS `candidate`;

CREATE TABLE `candidate` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `log_id` int(11) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `district` varchar(25) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `candidate` */

insert  into `candidate`(`sid`,`name`,`log_id`,`dob`,`email`,`phone`,`place`,`post`,`pin`,`district`,`image`) values (1,'cfgghjk',6,'2019-12-03','rttyuu',98765443,'dfghj','rtyuu',8796,'vbgret','20191203_144931.jpg'),(2,'sandra',7,'2019-12-04','sandra@gmail.com',2147483647,'pala','md',7864,'palakad','20191204_113245.jpg'),(3,'nfhgf',8,'hgfhfhj','gnfcfcbdh',888888,'ttre','fdghfr',87687,'frsdghfd','20191205_111727.jpg'),(4,'gfgsgf',9,'kklhyly','kghk,hlh',9999999,'hgfhjgt','gfjg',876868,'gfhjg','20191205_112146.jpg'),(5,'',13,'','',8888888,'','',6656,'','20191205_140639.jpg'),(6,'hfhfjf',19,'','',888888,'','',5645,'','20191205_201850.jpg'),(7,'hfhjr',20,'hgmjhk','hgfmhg',88888,'hfj','jhfjhf',4564,'hgfjg','20191205_201923.jpg'),(8,'fdshtAW',22,'JGKJGKJGH','GFYJRUYJZ',7777777,'','',5349,'','20191206_111300.jpg'),(9,'T6RET5RED`',24,'UGHUGU','HUHBG',899989,'UGHUH','BUBUHG',89898,'UGUHBG','20191206_111541.jpg'),(10,'\"+name+\"',0,'\"+DOB+\"','\"+E_Mail+\"',0,'\"+place+\"','\"+Post+\"',0,'\"+District+\"','\"+fname+\"'),(11,'\"+name+\"',0,'\"+DOB+\"','\"+E_Mail+\"',0,'\"+place+\"','\"+Post+\"',0,'\"+District+\"','\"+fname+\"'),(12,'joel',26,'2019-12-24','nnnn',67890123,'kannur','kannur',12345,'kannur','20191210_103759.jpg');

/*Table structure for table `company` */

DROP TABLE IF EXISTS `company`;

CREATE TABLE `company` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `log_id` int(11) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `contact` varchar(25) DEFAULT NULL,
  `email` varchar(26) DEFAULT NULL,
  `licence_no` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `company` */

insert  into `company`(`staff_id`,`name`,`log_id`,`place`,`pin`,`post`,`contact`,`email`,`licence_no`) values (1,'SANDRA',2,'PLACEE',78998,'POST','6789','HFYRUR','JHB,H'),(3,'GVJF',11,'khkhg',9087,'khkh','hkjh','khkh','khkjh'),(4,'hhhhd',3,'hhhh',0,'jlkj','jbkjh','khkjh','khkhj'),(7,'saaa',4,'fsddd',0,'','gfdghdf','ggfnf','gdjf'),(10,'xxxxxxx',27,'kannur',678905,'kannur','9678909','hhhh@gmail.com','123456');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `vid` int(11) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

/*Table structure for table `instruction` */

DROP TABLE IF EXISTS `instruction`;

CREATE TABLE `instruction` (
  `inst_id` int(11) NOT NULL AUTO_INCREMENT,
  `instructions` varchar(70) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `qualification` varchar(70) DEFAULT NULL,
  `age_limit` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`inst_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `instruction` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values (1,'admin','admin','admin'),(4,'san','123','company'),(6,'haris','haris','candidate'),(7,'sandra','sandra','candidate'),(26,'candidate','8888','pending'),(27,'yyyyyy','123','pending');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(40) DEFAULT NULL,
  `date` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`nid`,`notification`,`date`) values (2,'sample noti','2019-12-02'),(3,'sandra','2019-12-05'),(4,'hfnhr','2019-12-07'),(6,'hhhhhhh','2019-12-10');

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `qid` int(11) NOT NULL AUTO_INCREMENT,
  `vid` int(11) DEFAULT NULL,
  `question` varchar(999) DEFAULT NULL,
  `option1` varchar(25) DEFAULT NULL,
  `option2` varchar(25) DEFAULT NULL,
  `option3` varchar(25) DEFAULT NULL,
  `option4` varchar(34) DEFAULT NULL,
  `answer` varchar(999) DEFAULT NULL,
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `questions` */

insert  into `questions`(`qid`,`vid`,`question`,`option1`,`option2`,`option3`,`option4`,`answer`) values (1,1,'\"+Questions+\"','\"+Option1+\"','\"+Option2+\"','\"+Option3+\"','\"+Option4+\"','\"+Answers+\"'),(4,1,'ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt','yyyyyy','xxxxxxxxxxx','yyyyyyyyyyy','xxxxxxxxxxxxxx','yyyyyyyyyyy');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) DEFAULT NULL,
  `qid` int(11) DEFAULT NULL,
  `option` varchar(50) DEFAULT NULL,
  `mark` int(11) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`rid`,`cid`,`qid`,`option`,`mark`) values (1,26,NULL,NULL,NULL);

/*Table structure for table `vacancyy` */

DROP TABLE IF EXISTS `vacancyy`;

CREATE TABLE `vacancyy` (
  `vac_id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `no_of_post` int(11) DEFAULT NULL,
  `examdate` date DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`vac_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `vacancyy` */

insert  into `vacancyy`(`vac_id`,`cid`,`post`,`description`,`no_of_post`,`examdate`,`date`) values (1,11,'xxxx',NULL,NULL,NULL,NULL),(2,3,'xxxxxx',NULL,NULL,NULL,NULL),(3,27,'xxxxxxxx',NULL,NULL,NULL,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
