from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        car = {}
        car["first_name"] = result[0]
        car["last_name"] = result[1]
        car["hobbies"] = result[2]
        car["activate"] = result[3]
        car["license_plate"] = result[4]
        car["color"] = result[5]
        car["description"] = result[6]
        car["brand"] = result[7]
        car["model"] = result[8]
        out.append(car)
    return out


def scan():
    cursor = get_db().execute(
        ''' 
            SELECT  user.first_name,
                    user.last_name,
                    user.hobbies,
                    user.activate,
                    vehicle.license_plate,
                    vehicle.color,
                    vehicle_type.description,
                    vehicle.brand,
                    vehicle.model
            FROM user
            INNER JOIN vehicle ON user.id = vehicle.user_id
            INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id;
        '''
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)