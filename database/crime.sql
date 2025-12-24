CREATE TABLE crime_cases (
    case_id INTEGER PRIMARY KEY,
    date DATE,
    area VARCHAR(100),
    crime_type VARCHAR(50),
    victim_age INTEGER,
    victim_gender VARCHAR(10),
    status VARCHAR(20)
);
