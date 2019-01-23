import os


environ = {
    "SECRET_KEY" : "",
    "UPLOAD_FOLDER" : None,
    "SQLALCHEMY_DATABASE_URI" : None,
    "SQLALCHEMY_TRACK_MODIFICATIONS" : None,
    "MAIL_SERVER" : None,
    "MAIL_PORT" : None,
    "MAIL_USE_TLS" : None,
    "MAIL_USERNAME" : None,
    "MAIL_PASSWORD" : None,
    "MAIL_SUBJECT_PREFIX" : None,
    "MAIL_SENDER" : None,
}


def environ_var(variable):
    try:
        variable = os.environ[variable]
    except KeyError:
        variable = input('Which Environment Variable are you changing? ')
        value = input('Assign the Environment Variable a value: ')
    
        try:
            os.environ[variable] = value
            print("Validation: {}".format(os.environ[variable]))
        except Exception as error:
            print(error)
    print("Validation: {}".format(os.environ[variable]))