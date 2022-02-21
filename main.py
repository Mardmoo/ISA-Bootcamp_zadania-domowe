import json

user_db = {}


def keep_personal_data():
    first_name = input('Podaj imię: ')
    last_name = input('Podaj nazwisko: ')
    while True:
        try:
            phone_number = input('Podaj numer telefonu: ')
            user_db['Imie'] = first_name
            user_db['Nazwisko'] = last_name
            user_db['nr_telefonu'] = phone_number

            phone_number = phone_number.replace(" ", "").replace("-", "")
            if len(str(phone_number)) == 9:
                print('Zweryfikowano numer telefonu, zapisano dane użytkownika.')
                break

            else:
                raise ValueError

        except ValueError:
            print('Nieprawidłowy numer telefonu, spróbuj ponownie.')

        finally:
            with open('user_db.json', 'w') as database:
                json.dump(user_db, database)


keep_personal_data()
