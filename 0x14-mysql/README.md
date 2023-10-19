## 0. Install MySQL
Since we have two servers, web-01 and web-02, we need to install mysql 5.7.x on both servers. Here is the process.
#### STEP 1 : MySQL installation.
Create the file signature.key where ever you will be executing the rest of the commands in this section.
Copy the following into the file.
```
-----BEGIN PGP PUBLIC KEY BLOCK----- Version: SKS 1.1.6 Comment: Hostname: pgp.mit.edu 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 sTSKHe+QnnnoFmu4gnmDU31i =Xqbo -----END PGP PUBLIC KEY BLOCK-----
```
Next, follow up with these commands.
```bash
sudo apt-key add signature.key
```

```bash
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
```

```bash
sudo apt-get update
```
Check the available versions.
```bash
sudo apt-get update
```
```
mysql-server:
  Installed: (none)
  Candidate: 8.0.27-0ubuntu0.20.04.1
  Version table:
     8.0.27-0ubuntu0.20.04.1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
        500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages
     8.0.19-0ubuntu5 500
        500 http://archive.ubuntu.com/ubuntu focal/main amd64 Packages
     5.7.37-1ubuntu18.04 500
        500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages
```
Install the recommended version for the tasks.
```bash
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```
Make sure that you installed the right version.
```bash
mysql --version
```
You must get the following.
```
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
```
#### STEP 2 : SSH VERIFICATION
Check if the key given by ALX is within the authorized keys in the path `~/.ssh/authorized_keys` for both servers. If the following key does not exist, you must add it using
`sudo vi ~/.ssh/authorized_keys`.
They key provided by ALX.
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```
## 1. Let us in!
In this task we need to create a user and grant privileges, here are the commands.
#### SERVER web-01
```bash
ssh ubuntu@ip
sudo mysql
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY projectcorrection280hbtn;
# Make sure that holberton_user has permission to check the primary/replica status of your databases.
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
# Apply the changes
FLUSH PRIVILEGES;
# Make sure the grants are as mentioned in the task.
SHOW GRANTS FOR 'holberton_user'@'localhost';
```
#### SERVER web-02
```bash
ssh ubuntu@ip
sudo mysql
```
```sql
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY projectcorrection280hbtn;
"""Make sure that holberton_user has permission to check the primary/replica status of your databases."""
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
"""Apply the changes"""
FLUSH PRIVILEGES;
"""Make sure the grants are as mentioned in the task."""
SHOW GRANTS FOR 'holberton_user'@'localhost';
```
## 2. If only you could see what I've seen with your eyes
Database and table creation and population. We will be creating a database in web-01 in order to replicate it later in web-02.
#### SERVER web-01
```bash
ssh ubuntu@ip
sudo mysql
```
```sql
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
"""Creation of the table nexus6."""
CREATE TABLE nexus6(
	id INT(11) AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20)
);
"""Granting select permissions to holberton_user on the table nexus6."""
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
"""Make sure the table has been populated"""
select * from nexus6;
```
## 3. Quite an experience to live in fear, isn't it?
Continuing our work in web-01, we will create a new user.
```bash
ssh ubuntu@ip
sudo mysql
```
```sql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'projectcorrection281hbtn';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
"""holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions."""
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
"""Make sure that all is good"""
SELECT user, Repl_slave_priv FROM mysql.user;
```
## 4. Setup a Primary-Replica infrastructure using MySQL
Finally we will set up our primary-replica synchronization.
#### STEP 1 : web-01
First thing first, we need to unable port 3306, using the following command.
```bash
sudo ufw allow 3306/tcp
```
Access the file `my.cnf` or `mysqld.cnf`. This file is located in `/etc/mysql/mysql.conf.d`.
```bash
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
```
Comment the line `bind-address   = 127.0.0.1`. And add these two lines after `[mysqld]`.
```
server_id       = 1
log_bin         = /var/log/mysql/mysql-bin.log
```
Before you exit the server do the following.
```bash
sudo mysql
```
```sql
SHOW MASTER STATUS;
```
Keep the file name that may look something like `mysql-bin.000001` and the Position `711`. We will need those info when connecting our slave server.
#### STEP 2 : web-02
Unable port 3306, using the following command.
```bash
sudo ufw allow 3306/tcp
```
Create the database as it is in the primary, and populate it with the same info.
```sql
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
"""Creation of the table nexus6."""
CREATE TABLE nexus6(
	id INT(11) AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20)
);
```
Access the file `my.cnf` or `mysqld.cnf`. This file is located in `/etc/mysql/mysql.conf.d` again. This time we will add one line under, `[mysql]`.
```
server-id       = 2
```
We must run the following script.
```sql
CHANGE MASTER TO
	MASTER_HOST = 'web-01',
	MASTER_USER = 'replica_user',
	MASTER_PASSWORD = 'projectcorrection281hbtn',
	MASTER_LOG_FILE = 'mysql-bin.000001',
	MASTER_LOG_POS = '711';
START SLAVE;
```
Then we need to show slave status in order to check if the replication was successful.
```sql
SHOW SLAVE STATUS\G
```
The command will show the following information.
```
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: web-01
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000001
          Read_Master_Log_Pos: 711
               Relay_Log_File: 376576-web-02-relay-bin.000003
                Relay_Log_Pos: 320
        Relay_Master_Log_File: mysql-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 711
              Relay_Log_Space: 1258
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error:
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 1
                  Master_UUID: e4d7568b-6d1e-12ee-a6d8-066a60abga09
             Master_Info_File: /var/lib/mysql/master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind:
      Last_IO_Error_Timestamp:
     Last_SQL_Error_Timestamp:
               Master_SSL_Crl:
           Master_SSL_Crlpath:
           Retrieved_Gtid_Set:
            Executed_Gtid_Set:
                Auto_Position: 0
         Replicate_Rewrite_DB:
                 Channel_Name:
           Master_TLS_Version:
```
You should have `Slave_IO_State: Waiting for master to send event`.  And no errors in these fields.
```
Last_IO_Errno: 0
Last_IO_Error:
Last_SQL_Errno: 0
Last_SQL_Error:
```
In order to test your primary-replica synchronization, try adding a new record to the database from the primary server and check if it has been added in the secondary server. If everything worked out well, the database would be duplicated in the second server as it is in the first server.
## 5. MySQL backup
In this task we will learn how to dump a database and archive it.
```bash
sudo mysqldump -u root -p"$1" --all-databases | sudo tee backup.sql
```
The first command is to dump the database in an sql file called backup.sql.
The name of the user is root and the password will be passed as an argument. The second part is where we used tee to store in the file.
Next we will archive the file backup.sql.
```bash
tar -czf "$(date +'%d-%m-%Y').tar.gz" backup.sql
```
This is a command that will help us archive the file. The tar is used to archive, and the options c z f are for create, gzip, file consecutively.
The file will be saved under a string of the current date.tar.gz .
