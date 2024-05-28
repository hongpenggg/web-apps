-- CREATE DATABASE spectrum

CREATE TABLE IF NOT EXISTS `MonitorInfo` (
	`ModelNo`	TEXT NOT NULL,
	`Price`	INTEGER NOT NULL,
	`Promotion`	INTEGER NOT NULL CHECK(Promotion >= 0 AND Promotion <= 100),
	`ScreenSize`	INTEGER NOT NULL,
	`Resolution`	TEXT NOT NULL,
	PRIMARY KEY(`ModelNo`)
);

CREATE TABLE IF NOT EXISTS `ProductInfo` (
	`SerialNo`	TEXT NOT NULL,
	`ModelNo`	TEXT NOT NULL,
	`Status`	TEXT NOT NULL CHECK(Status IN ('Sold', 'In Stock')),
	PRIMARY KEY(`SerialNo`),
	FOREIGN KEY(`ModelNo`) REFERENCES `MonitorInfo`(`ModelNo`)
);

CREATE TABLE IF NOT EXISTS `CustomerInfo` (
	`Email`	TEXT NOT NULL,
	`Name`	TEXT NOT NULL,
	`Contact`	TEXT NOT NULL,
	`Address`	TEXT NOT NULL,
	PRIMARY KEY(`Email`)
);

CREATE TABLE IF NOT EXISTS `SalesRecord` (
	`RecordID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Email`	TEXT NOT NULL,
	`SerialNo`	TEXT NOT NULL,
	`OrderDate`	TEXT NOT NULL,
	`DeliveryDate`	TEXT NOT NULL,
	FOREIGN KEY(`Email`) REFERENCES `CustomerInfo`(`Email`),
	FOREIGN KEY(`SerialNo`) REFERENCES `ProductInfo`(`SerialNo`)
);