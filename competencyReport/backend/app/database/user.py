from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        user = {}
        user["id"] = result[0]
        user["first_name"] = result[1]
        user["last_name"] = result[2]
        user["hobbies"] = result[3]
        user["active"] = result[4]
        out.append(user)
    return out

def scan():
    cursor = get_db().execute(
        "SELECT * FROM user WHERE activate=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)
    
def select_by_id(id):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=? AND activate=1", (id,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(data):
    query = """ INSERT INTO user (
        first_name, 
        last_name, 
        hobbies
    ) values (?,?,?) 
    """

    values = (
        data.get("first_name"),
        data.get("last_name"),
        data.get("hobbies")
    )

    cursor = get_db()
    cursor.execute(query, values)
    cursor.commit() #apply changes
    cursor.close()

def update(data, id):
    
    keys = data.keys()
    for key in keys:
        value = data.get(key) 
        query = "UPDATE user set "+key+"='"+value+"' WHERE id=?"
        cursor = get_db()
        cursor.execute(query, (id,))
        cursor.commit()
    cursor.close()

def delete(id):

    '''Delete User'''
    cursor = get_db()
    cursor.execute("DELETE FROM user WHERE id=?", (id,))
    cursor.commit()
    cursor.close()