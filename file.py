def greeter(greet_person):
    def wrapper(*args):
        val = "Aloha "+greet_person(*args).lower().title()
        return val
    return wrapper


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
