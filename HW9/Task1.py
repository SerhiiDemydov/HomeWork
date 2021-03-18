from math import sqrt
import logging

log_template = '%(asctime)s - %(name)s -%(levelname)s - %(message)s - %(pathname)s'
logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="a", format=log_template)

list_action = ('+', '-', '/', '^', '*', '/^', '%')


def values(name):
    while True:
        val = input(f"Enter {name} value: ")
        logging.info(f"Entered {name} value: {val}")
        try:
            x = float(val)
        except (ValueError,):
            logging.error(f'ValueError in {name} value', exc_info=True)
            print("First values is not decimal")
            continue
        return x


logging.info("Beginning of work")
try:
    while True:

        value_1 = values('first')

        while True:
            str_2 = input(f"Enter action on values {list_action}")
            logging.info(f"Entered action: {str_2}")
            if str_2 not in list_action:
                logging.warning('Incorrect action')
                print("This parameter dont include list actions")
                continue
            break

        logging.info("Check the action is /^ or not")
        if str_2 != "/^":
            logging.info("Check action is not /^")
            value_2 = values('second')

        if str_2 == "+":
            logging.info("The sum of two values")
            print(f'{value_1} + {value_2} = {value_1 + value_2}\n')
        elif str_2 == "-":
            logging.info("Difference of two values")
            print(f'{value_1} - {value_2} = {value_1 - value_2}\n')
        elif str_2 == "/":
            try:
                logging.info("Division of two values")
                print(f'{value_1} / {value_2} = {value_1 / value_2}\n')
            except(ZeroDivisionError,):
                logging.error('ZeroDivisionError', exc_info=True)
                print("Cannot be divide by 0\n")
                continue
        elif str_2 == "*":
            logging.info("Multiplying two values")
            print(f'{value_1} * {value_2} = {value_1 * value_2}\n')
        elif str_2 == "^":
            logging.info("Degree of value")
            print(f'{value_1} ^ {value_2} = {value_1 ** value_2}\n')
        elif str_2 == "/^":
            try:
                logging.info("Square root of value")
                print(f'/^{value_1} = {sqrt(value_1)}\n')
            except (ValueError,):
                print('Value in incorrect\n')
                logging.error(f'ValueError in {value_1}', exc_info=True)
                continue
        elif str_2 == "%":
            logging.info("Percentage of value")
            print(f'{value_1}% from {value_2} = {value_2 / 100 * value_1}\n')

except (KeyboardInterrupt, ):
    logging.info("End of work")
