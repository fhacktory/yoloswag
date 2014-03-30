DROP TABLE IF EXISTS roads;
CREATE TABLE roads(`id`  INTEGER PRIMARY KEY AUTOINCREMENT,
       	           `name` VARCHAR(512),
		   `points` BLOB);

DROP TABLE IF EXISTS pois;
CREATE TABLE pois(`id`  INTEGER PRIMARY KEY AUTOINCREMENT,
       	           `road_id` INTEGER,
		   `position` BLOB,
		   `name` VARCHAR(512),
		   `picture` VARCHAR(512),
		   `type` INTEGER);

DROP TABLE IF EXISTS users;
CREATE TABLE users(`id`  INTEGER PRIMARY KEY AUTOINCREMENT,
       	           `name` VARCHAR(512),
		   `email` VARCHAR(512) UNIQUE,
		   `gender` VARCHAR(512),
		   `level` VARCHAR(512),
		   `age` INTEGER);
