from functools import wraps
import datetime

def logged(log_dir):
    file_path =  log_dir
    
    def _logged(old_function):
    
        @wraps(old_function)
        def new_function(*args, **kwargs):
            dt = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            str_log = f'Дата и время вызова функции {dt}, \
            имя функции:{old_function.__name__}, c аргументами: {args} и {kwargs}, получен результат {result}'
            with open(file_path + 'logs.txt', 'a') as f:
                f.write(str_log + '\n')

            return result
        return new_function
    return _logged