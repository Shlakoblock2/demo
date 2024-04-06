from src.database.db_manager import db


def getAll(table: str) -> list:
    res_list = db.execute(query=f"select * from {table}", many=True)
    return res_list

def create(table: str, model: dict):
    if model.__contains__("id"):
        model.pop("id")
    db.execute(
        query=f"insert into {table}({array_to_str(model.keys())}) values({get_values_str(len(model))})",
        args=(tuple(model.values()))
    )

def update(table: str, model: dict, index: int):
    if model.__contains__("id"):
        model.pop("id")

    args = list(model.values())
    args.append(index)
    return db.execute(
        query=f'update {table} set ({array_to_str(model.keys())}) = ({get_values_str(len(model))}) where id=(?)',
        args=(tuple(args)))

def delete(table: str, index: int):
    db.execute(f'delete from {table} where id=(?)', args=(index,))

def login(name: str, password: str):
    res = db.execute(
        query=f'select * from Users where login=(?) and password =(?)',
        args=(name, password)
    )
    return res

def get_values_str(amount: int) -> str:
    values: str = "?"
    for i in range(1, amount):
        values += ", ?"
    return values

def array_to_str(array) -> str:
    return ','.join(map(str, array))