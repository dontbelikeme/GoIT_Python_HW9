

result_dict = {}

def input_error(func):
    def inner(*args, **kwargs): 
        try: 
            result = func(*args, **kwargs)
        except IndexError as e:
            print('Give me name and phone number')
        return result 
    return inner       

def hello():
    print('How can I help you?')

@input_error    
def add(usr_name, usr_phone):
    result_dict[usr_name] = usr_phone
    #По этой команде бот сохраняет в памяти новый контакт.

@input_error    
def change(usr_name, usr_phone):
    result_dict.update({usr_name:usr_phone})    
    #По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.

@input_error    
def phone(usr_name):
    print(result_dict.get(usr_name))    
    #По этой команде бот выводит в консоль номер телефона для указанного контакта.
    
def show_all():
    print('\n'.join("{}: {}".format(k, v) for k, v in result_dict.items()))    
    #По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
    
def get_out():
    print('Good bye!')
    
#"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того, как выведет в консоль "Good bye!".

def main():
    while True:
        usr_input = input('Введите команду...').lower()
        input_args = usr_input.split(' ')
        #usr_index = input_args.pop()
        #usr_key = input_args.pop()
        #usr_value = input_args.pop()
        
        
        if input_args[0] == 'hello':
            hello()
        elif input_args[0] == 'add':
            try: 
                add(input_args[1], input_args[2])
            except IndexError as e:
                print('Give me a name and phone number')    
        elif input_args[0] == 'change':
            try:
                change(input_args[1],input_args[2])
            except IndexError as e:
                print('Give me a name and phone number')    
        elif input_args[0] == 'phone':
            try:
                phone(input_args[1])
            except IndexError as e:
                print('Give me a name')     
        elif input_args[0] == 'show':
            show_all()
        elif input_args[0] == 'good':
            get_out()
            break
        elif input_args[0] == 'close':
            get_out()
            break               
        elif input_args[0] == 'exit':
            get_out()      
            break
        else:
            print('Unknown command')       
            
            
    
main()    