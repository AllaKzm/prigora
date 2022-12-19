CREATE TABLE History
(
  EnterDate DATE NOT NULL,
  Entery_id INT NOT NULL,
  ExitDate DATE NOT NULL,
  PRIMARY KEY (Entery_id)
);

CREATE TABLE Services
(
  Serv_ID INT NOT NULL,
  Serv_Title NVARCHAR(MAX) NOT NULL,
  servise_code NUMERIC NOT NULL,
  prise__for_hour FLOAT NOT NULL,
  PRIMARY KEY (Serv_ID)
);

CREATE TABLE Client
(
  Client_ID INT NOT NULL,
  Name NVARCHAR(MAX) NOT NULL,
  passport NUMERIC NOT NULL,
  Birth_date DATE NOT NULL,
  address NVARCHAR(MAX) NOT NULL,
  email NVARCHAR(MAX) NOT NULL,
  password NVARCHAR(MAX) NOT NULL,
  PRIMARY KEY (Client_ID)
);

CREATE TABLE Status
(
  StatusID INT NOT NULL,
  StatusName NVARCHAR(MAX) NOT NULL,
  PRIMARY KEY (StatusID)
);

CREATE TABLE Position
(
  PosID INT NOT NULL,
  PosTitle NVARCHAR(MAX) NOT NULL,
  PRIMARY KEY (PosID)
);

CREATE TABLE LogStatus
(
  StatusID INT NOT NULL,
  StatusTitle NVARCHAR(MAX) NOT NULL,
  PRIMARY KEY (StatusID)
);

CREATE TABLE Employee
(
  emp_id INT NOT NULL,
  name NVARCHAR(MAX) NOT NULL,
  login NVARCHAR(MAX) NOT NULL,
  password NVARCHAR(MAX) NOT NULL,
  LastLogIn DATE NOT NULL,
  PosID INT NOT NULL,
  StatusID INT NOT NULL,
  PRIMARY KEY (emp_id),
  FOREIGN KEY (PosID) REFERENCES Position(PosID),
  FOREIGN KEY (StatusID) REFERENCES LogStatus(StatusID)
);

CREATE TABLE orders
(
  Order_ID INT NOT NULL,
  barcode NVARCHAR(MAX) NOT NULL,
  Date_create DATE NOT NULL,
  Time_ordered DATE NOT NULL,
  close_date DATE NOT NULL,
  rental_time NVARCHAR(MAX) NOT NULL,
  emp_id INT NOT NULL,
  Client_ID INT NOT NULL,
  StatusID INT NOT NULL,
  PRIMARY KEY (Order_ID),
  FOREIGN KEY (emp_id) REFERENCES Employee(emp_id),
  FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID),
  FOREIGN KEY (StatusID) REFERENCES Status(StatusID)
);

CREATE TABLE Emp_enter
(
  emp_id INT NOT NULL,
  Entery_id INT NOT NULL,
  PRIMARY KEY (emp_id, Entery_id),
  FOREIGN KEY (emp_id) REFERENCES Employee(emp_id),
  FOREIGN KEY (Entery_id) REFERENCES History(Entery_id)
);

CREATE TABLE Ordered
(
  Order_ID INT NOT NULL,
  Serv_ID INT NOT NULL,
  PRIMARY KEY (Order_ID, Serv_ID),
  FOREIGN KEY (Order_ID) REFERENCES orders(Order_ID),
  FOREIGN KEY (Serv_ID) REFERENCES Services(Serv_ID)
);