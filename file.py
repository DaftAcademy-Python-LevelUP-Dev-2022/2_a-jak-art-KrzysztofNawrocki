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


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
