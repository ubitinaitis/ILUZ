CREATE DATABASE budgetDB;
-- CREATE USER 'webapp'@'%' IDENTIFIED BY 'temporary_password';
GRANT ALL PRIVILEGES ON budgetDB.* TO 'webapp'@'%';
FLUSH PRIVILEGES;

USE budgetDB;

CREATE TABLE Balance
(
    balanceID    integer,
    currentFunds integer,
    PRIMARY KEY (balanceID)
);

CREATE TABLE Deposit (
    depositID integer,
    amount integer,
    balanceID integer,
    PRIMARY KEY (depositID),
    FOREIGN KEY (balanceID) REFERENCES Balance(balanceID)
);

CREATE TABLE BudgetCoach
(
    employeeID integer,
    firstName  varchar(20),
    lastName   varchar(20),
    birthDate  date,
    hireDate   date,
    email      varchar(255),
    salary     integer,
    ssn        varchar(20),
    managerID  integer,
    PRIMARY KEY (employeeID)
);

ALTER TABLE BudgetCoach
ADD FOREIGN KEY (managerID) REFERENCES BudgetCoach (employeeID);

CREATE TABLE Budget
(
    budgetID       integer,
    category       varchar(50),
    budgetCategory integer,
    balanceID      integer,
    PRIMARY KEY (budgetID),
    FOREIGN KEY (balanceID) REFERENCES Balance (balanceID)
);

CREATE TABLE Transaction
(
    transactionID integer,
    dateOf        date,
    total         integer,
    company       varchar(255),
    budgetID    integer,
    PRIMARY KEY (transactionID)
);

CREATE TABLE Individual
(
    userID        integer,
    email         varchar(255),
    firstName     varchar(20),
    lastName      varchar(20),
    hasBalance    integer,
    customerRepID integer,
    PRIMARY KEY (userID),
    FOREIGN KEY (hasBalance) REFERENCES Balance (balanceID),
    FOREIGN KEY (customerRepID) REFERENCES BudgetCoach (employeeID)
);

CREATE TABLE Dependent
(
    userID     integer,
    firstName  varchar(20),
    lastName   varchar(20),
    birthDate  date,
    hasBalance integer,
    parentID   integer,
    PRIMARY KEY (userID),
    FOREIGN KEY (hasBalance) REFERENCES Balance (balanceID),
    FOREIGN KEY (parentID) REFERENCES Individual (userID)
);


CREATE TABLE BudgetTowards
(
    budgetID      integer,
    transactionID integer,
    PRIMARY KEY (budgetID, transactionID),
    FOREIGN KEY (budgetID) REFERENCES Budget (budgetID),
    FOREIGN KEY (transactionID) REFERENCES Transaction (transactionID)
);


CREATE TABLE Item
(
    itemID        integer,
    price         integer,
    category      varchar(50),
    transactionID integer,
    PRIMARY KEY (itemID),
    FOREIGN KEY (transactionID) REFERENCES Transaction (transactionID)
);




