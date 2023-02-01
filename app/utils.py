from passlib.context import CryptContext


# variable that converts the entered password field and changes it to be hashed, 
# this is for security reasons so no hackers can get the raw password data in the database
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = 'auto')

def hash(password: str):
    return pwd_context.hash(password)

# a way to verify the hashed password and the password being entered by the user
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)