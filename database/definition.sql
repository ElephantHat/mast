DROP TABLE IF EXISTS `advisor`;
CREATE TABLE advisor (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  --name VARCHAR(255) NOT NULL,--
  PRIMARY KEY  (id),
  UNIQUE KEY email (email)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `student`;
CREATE TABLE student (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY email (email)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE appointment (
  apt_date VARCHAR(255) NOT NULL,
  apt_time VARCHAR(255) NOT NULL,
  apt_uid VARCHAR(255) NOT NULL,
  aid INT UNSIGNED NOT NULL,
  sid INT UNSIGNED NOT NULL,
  PRIMARY KEY  (uid),
  FOREIGN KEY (aid) REFERENCES advisor (id) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (aid) REFERENCES student (id) ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO advisor(id, email, name)
VALUES (
    DEFAULT,
    "advisor1@oregonstate.edu",
);

INSERT INTO student(id, email, name)
VALUES (
    DEFAULT,
    "student1@oregonstate.edu",
    "Steve Steverson"
);

INSERT INTO appointment(apt_date, apt_time, apt_uid, aid, sid)
VALUES (
    "12-01-2014",
    "12:30am",
    "apt_uid-goes-here"
    (SELECT id FROM advisor WHERE name = "John Doe"),
    (SELECT id FROM student WHERE name = "Steve Steverson")
);
