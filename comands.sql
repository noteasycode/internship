CREATE SCHEMA `db_books` ;

use db_books;

CREATE TABLE `db_books`.`tbl_topics` (
  `topic_id` INT(127) NOT NULL AUTO_INCREMENT,
  `topic_name` VARCHAR(100) NULL,
  PRIMARY KEY (`topic_id`),
  UNIQUE INDEX `topic_name_UNIQUE` (`topic_name` ASC) VISIBLE);

CREATE TABLE `db_books`.`tbl_books` (
  `b_id` CHAR(17) NOT NULL COMMENT 'ISBN код книги',
  `b_name` CHAR(255) NOT NULL COMMENT 'Название книги',
  `b_author` CHAR(255) NULL COMMENT 'Автор',
  `b_topic` INT NULL COMMENT 'Код категории, к которой относится книга',
  `b_price` DECIMAL(10,2) NULL COMMENT 'Стоимость ',
  PRIMARY KEY (`b_id`),
  INDEX `tbl_topics_idx` (`b_topic` ASC) VISIBLE,
  CONSTRAINT `tbl_topics`
    FOREIGN KEY (`b_topic`)
    REFERENCES `db_books`.`tbl_topics` (`topic_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('Классика');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('Лирика');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('Мемуары');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('Психология');
INSERT INTO `db_books`.`tbl_topics` (`topic_name`) VALUES ('Философия');

INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('978-5-17-086923-7', 'Сто лет одиночества', 'Габриэль Гарсиа Маркес', '1', '445.50');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('978-5-699-78967-2', 'Мастер и Маргарита', 'Михаил Булгаков', '1', '342');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`) VALUES ('978-617-12-3352-2', 'Психология влияния', 'Роберт Чалдини', '4');
INSERT INTO `db_books`.`tbl_books` (`b_id`, `b_name`, `b_author`, `b_topic`, `b_price`) VALUES ('978-5-906897-39-8', 'Мужчины с Марса, Женщины с Венеры', 'Джон Грэй', '4', '119');

UPDATE tbl_books SET b_price = b_price * 0.10 + b_price WHERE b_price > 0;
DELETE FROM tbl_books WHERE b_price is NULL;