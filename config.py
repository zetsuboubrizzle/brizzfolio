import os


def set_env_var():
    variable = input('Which Environment Variable are you changing? ')
    value = input('Assign the Environment Variable a value: ')
    
    try:
        os.environ[variable] = value
        print("Validation: {}".format(os.environ[variable]))
    except Exception as error:
        print(error)