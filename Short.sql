BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `Short` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`url`	TEXT,
	`short`	TEXT
);
COMMIT;
