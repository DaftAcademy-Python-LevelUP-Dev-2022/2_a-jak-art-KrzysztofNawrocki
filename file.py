from itertools import chain


def greeter(greet_person):
    def wrapper(*args):
        val = "Aloha "+greet_person(*args).lower().title()
        return val
    return wrapper


def sums_of_str_elements_are_equal(condition):
    def wrapper(*args):
        numbers_list = condition(*args).split(" ")
        sum_list = [0 for i in range(len(numbers_list))]
        for index, number in enumerate(numbers_list):
            for digit in number:
                if digit == "-":
                    continue
                sum_list[index] += int(digit)
        
        for index, num in enumerate(numbers_list):
            if num[0] == "-":
                sum_list[index] *= -1

        if sum_list[0] == sum_list[1]:
            return f"{sum_list[0]} == {sum_list[1]}"
        else:
            return f"{sum_list[0]} != {sum_list[1]}"
    return wrapper


def format_output(*required_args):
    def decorator(func):
        def wrapper(*args):
            args_list = [arg.split("__") for arg in required_args]
            input_dict = func(*args)

            if not all(key in input_dict.keys() for key in chain(*args_list)):
                raise ValueError

            output = {}
            for index, arg in enumerate(args_list):
                if len(arg)==1:
                    output[required_args[index]] = input_dict[arg[0]]

                if len(arg)==2:
                    value_combined = input_dict[arg[0]] + " " + input_dict[arg[1]]
                    output[required_args[index]] = value_combined

            return output
        return wrapper
    return decorator


def add_method_to_instance(klass):
    pass
