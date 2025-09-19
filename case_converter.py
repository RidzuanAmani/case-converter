# I convert case with list comprehension, inspired by string handling in Cipher project
def convert_to_snake_case(pascal_or_camel_cased_string):
    # I build a list with conditions, like validation in Luhn
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    # I join and clean up, learned from Arithmetic Formatter
    return ''.join(snake_cased_char_list).strip('_')

# I test the function, similar to my main() in Time Calculator
def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()
