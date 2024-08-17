from my_utils.services import dbAccess
import bcrypt


class User:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
        role: str,
        profilePic=None,
        last_edit: str = None,
        status: bool = None,
        id: int = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = (
            bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            if password
            else None
        )
        self.role = role
        self.profilePic = profilePic
        self.last_edit = last_edit
        self.status = status
        self.id = id

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name} {self.email}, {self.password}, {self.role}, {self.last_edit}, {self.status}"


@dbAccess
def Login(cursor, email: str, password: str):
    if cursor:
        sql_fetch_query = """SELECT `id`, `first_name`, `last_name`, `email`, `password`, `role`, `picture`, `last_edit`, `status` FROM `users` WHERE `email` = %s"""
        cursor.execute(sql_fetch_query, (email,))
        record = cursor.fetchone()
        if record:
            stored_password = record[4]
            if bcrypt.checkpw(password.encode(), stored_password.encode()):
                # Password matches, return User object
                return User(
                    first_name=record[1],
                    last_name=record[2],
                    email=record[3],
                    password=None,
                    role=record[5],
                    profilePic=record[6],
                    last_edit=record[7],
                    status=record[8],
                    id=record[0],
                )
    return None


@dbAccess
def CreateUser(cursor, user: User):
    if cursor:
        sql_fetch_query = """INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `role`, `picture`) VALUES (%s, %s, %s, %s, %s, %s)"""
        print(user.profilePic)
        cursor.execute(
            sql_fetch_query,
            (
                user.first_name,
                user.last_name,
                user.email,
                user.password,
                user.role,
                user.profilePic.read() if user.profilePic else None,
            ),
        )
        cursor.fetchone()
        record = cursor.lastrowid
        return record
    return None


@dbAccess
def ReadUser(cursor, user_id: int):
    if cursor:
        sql_fetch_query = """SELECT `id`, `first_name`, `last_name`, `email`, `role`, `picture`, `last_edit`, `status` FROM `users` WHERE `id` = %s"""
        cursor.execute(sql_fetch_query, (user_id,))
        record = cursor.fetchone()
        if record:
            return User(
                first_name=record[1],
                last_name=record[2],
                email=record[3],
                password=None,  # Password should not be fetched directly for security reasons
                role=record[4],
                profilePic=record[5],
                last_edit=record[6],
                status=record[7],
                id=record[0],
            )
    return None


@dbAccess
def UpdateUser(cursor, user: User):
    if cursor and user.id:
        sql_update_query = """UPDATE `users` SET `first_name` = %s, `last_name` = %s, `email` = %s, `role` = %s, `picture` = %s, `status` = %s WHERE `id` = %s"""
        cursor.execute(
            sql_update_query,
            (
                user.first_name,
                user.last_name,
                user.email,
                user.role,
                user.profilePic,
                user.status,
                user.id,
            ),
        )
        return cursor.rowcount > 0
    return False


@dbAccess
def DeleteUser(cursor, user_id: int):
    if cursor:
        sql_delete_query = """DELETE FROM `users` WHERE `id` = %s"""
        cursor.execute(sql_delete_query, (user_id,))
        return cursor.rowcount > 0
    return False


@dbAccess
def ReadAllUsers(cursor):
    if cursor:
        sql_fetch_all_query = """SELECT `id`, `first_name`, `last_name`, `email`, `role`, `picture`, `last_edit`, `status` FROM `users`"""
        cursor.execute(sql_fetch_all_query)
        records = cursor.fetchall()
        users = []
        for record in records:
            users.append(
                User(
                    first_name=record[1],
                    last_name=record[2],
                    email=record[3],
                    password=None,  # Password should not be fetched directly for security reasons
                    role=record[4],
                    profilePic=record[5],
                    last_edit=record[6],
                    status=record[7],
                    id=record[0],
                )
            )
        return users
    return None


@dbAccess
def ChangePassword(cursor, user_id: int, new_password: str):
    if cursor:
        hashed_password = bcrypt.hashpw(
            new_password.encode(), bcrypt.gensalt()
        ).decode()
        sql_update_query = """UPDATE `users` SET `password` = %s, `last_edit` = NOW() WHERE `id` = %s"""
        cursor.execute(sql_update_query, (hashed_password, user_id))
        return cursor.rowcount > 0
    return False
