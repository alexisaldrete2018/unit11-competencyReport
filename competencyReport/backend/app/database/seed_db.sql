---------------------- USERS ----------------------
--- CREATE USER TABLE ---
CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    hobbies TEXT,
    activate BOOLEAN NOT NULL DEFAULT 1
);

--- INSERT DATA ---
INSERT INTO user(first_name, last_name, hobbies) VALUES ("Bob", "Roberts", "Soccer");
INSERT INTO user(first_name, last_name, hobbies) VALUES ("Alex", "Guerrero", "Play Basket");
INSERT INTO user(first_name, last_name, hobbies) VALUES ("Tom", "Brady", "Football");
INSERT INTO user(first_name, last_name, hobbies) VALUES ("Michael", "Phelps", "Swim");
INSERT INTO user(first_name, last_name, hobbies) VALUES ("Leo", "Messi", "Golf");

--- READ DATA ---
SELECT * from USER;

---------------------- VEHICLES ----------------------

CREATE TABLE vehicle_type(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description VARCHAR(64)
);

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    v_type INTEGER NOT NULL,
    license_plate VARCHAR(45) NOT NULL,
    color VARCHAR(45),
    brand VARCHAR(45) NOT NULL,
    model VARCHAR(45) NOT NULL,
    active BOOLEAN DEFAULT 1,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (v_type) REFERENCES vehicle_type(id)
);

INSERT INTO vehicle_type(description) VALUES("motorcycle");
INSERT INTO vehicle_type(description) VALUES("car");
INSERT INTO vehicle_type(description) VALUES("truck");
INSERT INTO vehicle_type(description) VALUES("SUV");

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "red",
    "HELLO",
    2,
    1,
    "honda",
    "city"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "blue",
    "HELL1",
    2,
    4,
    "toyota",
    "camry"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "silver",
    "HELLO3",
    3,
    5,
    "nissan",
    "Super Truck "
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "white",
    "HELLO4",
    2,
    6,
    "honda",
    "civic"
);

INSERT INTO vehicle (
    color,
    license_plate,
    v_type,
    user_id,
    brand,
    model
) VALUES (
    "black",
    "HELLO5",
    1,
    7,
    "Kawasaki",
    "XF-10"
);

SELECT user.last_name,
       user.first_name,
       user.hobbies,
       user.activate,
       vehicle.license_plate,
       vehicle.color,
       vehicle_type.description,
       vehicle.brand,
       vehicle.model
FROM user
INNER JOIN vehicle ON user.id = vehicle.user_id
INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id
WHERE user.id = 1;