from passlib.hash import pbkdf2_sha512

class Utils(object):


    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2-sha512
        :param password: The sha512 password from the login/register from
        :return: A sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Check that the password sent matchees that of the database.
        The database password is encrypted more than the users's password at this stage
        :param password: sha512-hashed password
        :param hashed_password:
        :return:
        """
        return pbkdf2_sha512.verify(password, hashed_password)