from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        #Testi nimen pituudesta
        if len(username) < 3: 
            raise UserInputError("Username is too short")

        #Ei erikoismerkkejä 
        if not username.isalpha():
            raise UserInputError("Username contains special characters which are not allowed")
        
        #Onko käyttäjä jo olemassa
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already exists")
        
        #Salasanan pituus vähintään 8-merkkiä
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")
        
        #Salasana eivoi olla pelkästään kirjaimia
        if password.isalpha(): 
            raise UserInputError("Password must contain at least one number or special character")

