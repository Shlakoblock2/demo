create table Patient(
	id integer PRIMARY KEY autoincrement,
    name varchar(50),
    surname varchar(50),
    birthdate date,
    passport_number integer,
    passport_series integer,
    gender varchar(50),
    address varchar(50),
    mail varchar(50)
);
create table MedCard(
	id integer PRIMARY KEY autoincrement,
    patient_id integer,
    insurance integer,
    insurance_expiration date,
    issue_date date,
    last_visit_date date,
    next_visit_date date,
    foreign key (patient_id) references Patient(id)
);
create table Users(
	id integer PRIMARY KEY autoincrement,
    login varchar(16) not null unique,
    password varchar(16) not null,
    power_level integer
);
create table Visit_Type(
	id integer PRIMARY KEY autoincrement,
    name varchar(50)
);
create table Visit(
	id integer PRIMARY KEY autoincrement,
    visit_date date,
    patient_id integer,
    user_id integer,
    visit_type_id integer,
    visit_name varchar(50),
    result varchar(50),
     foreign key (user_id) references Users(id),
     foreign key (visit_type_id) references Visit_Type(id),
     foreign key (patient_id) references Patient(id)
);
