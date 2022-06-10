from functools import wraps
import time

def logged(log_file_path):
    file_path =  log_file_path
    
    def _logged(old_function):
    
        @wraps(old_function)
        def new_function(*args, **kwargs):
            start_date = time.date()
            start_time = time.time()
            result = old_function(*args, **kwargs)
            str_log = f'Дата и время вызова функции {start_date} {start_time}, \
            имя функции:{old_function.__name__}, c аргументами: {args} и {kwargs}, получен результат {result}'
            with open(file_path + 'logs.txt', 'a') as f:
                f.write(str_log + '\n')

            return result
        return new_function
    return _logged