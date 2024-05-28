-- CREATE DATABASE `sanitisers`

CREATE TABLE IF NOT EXISTS `Sanitisers` (
	`product_name`	TEXT NOT NULL,
	`active_ingredient`	TEXT NOT NULL,
	`alcohol_based`	TEXT NOT NULL,
	PRIMARY KEY(`product_name`)
);