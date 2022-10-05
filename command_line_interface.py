def quit_f(_=None):
    print("Good bye!")
    quit()

END_DICT = {'good bye':quit_f,
            'close':quit_f,
            'exit':quit_f}
CONTACT_DICT = {}

def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            handler(*args, **kwargs)
                return handler(*args, **kwargs)
        except IndexError:
            print("Give me name and phone please")
        except ValueError:
            print("Give me name and phone please")
        except KeyError:
            print("No such name in contacts list")
    return wrapper

@input_error
def phone_func(var_inp):
        x = var_inp.split()
        print(CONTACT_DICT[x[1]])

@input_error
def change_func(var_inp):
    x = var_inp.split()
    if len(x) == 3:
        CONTACT_DICT[x[1]]=x[2]
    else:
        print("Give me name and phone please")


@input_error
def add_func(var_inp):
    x = var_inp.split()
    if len(x) == 3:
        CONTACT_DICT[x[1]]=x[2]
    else:
        print("Give me name and phone please")

def main_cli():
    while True:
        var_inp = input("Enter command: ")
        var = var_inp.lower()
        if var == "hello":
            print("How can I help you?")
        elif var.startswith('add'):
            add_func(var_inp)
        elif var.startswith('phone'):
            phone_func(var_inp)
        elif var.startswith('change'):
            change_func(var_inp)
        elif var == "show all":
            if len(CONTACT_DICT) > 0:
                print(CONTACT_DICT)
            else:
                print("No contacts in contact list.")
        elif var in END_DICT:
            END_DICT[var]()

if __name__ == "__main__":
    main_cli()
