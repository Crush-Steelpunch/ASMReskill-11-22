CREATE TABLE IF NOT EXISTS users
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          first_name VARCHAR(30) NOT NULL,
                          last_name  VARCHAR(30) NOT NULL,
                          email      VARCHAR(150) NOT NULL,
                          PRIMARY KEY (id),
                          UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ben','Hesketh','test@test7.com'),(2,'Luke','Benson','test@test.com'),(3,'Matt','Hunt','test4@test.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;