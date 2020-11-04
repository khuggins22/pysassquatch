import sys
import getopt
import re
import yaml
import logging
import logging.config

with open('logs/logging.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())

logging.config.dictConfig(log_cfg)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def print_help():
    print('Useage: test.py -i <input_file> -o <output_file>')


def get_variable_dict(text):
    d = {}
    for line in text.splitlines():
        # Remove tailing whitespace and any extra spaces
        line = line.rstrip().replace(" ", "")
        logging.debug(f"Line: {line}")
        # Get variable name and value
        variable, value = line.split(':')
        logging.debug(f"Variable: {variable}, Value: {value}")
        d[variable] = value
    return d


def replace_variables(text, var_dict):

    for key, item in var_dict.items():
        # Turn the key into a regex expression with the added \b (word boundary) for exact matches.
        pattern = r"{key}\b".format(key=key)
        logging.debug(f"Pattern: {pattern}")
        text = re.sub(pattern, item, text)
        logging.debug(f"Replaced text: {text}")
    # print(f"Replaced text: {repr(text)}")
    return text


def main():
    input_file = ''
    output_file = ''

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input-file=", "output-file="])
    except getopt.GetoptError:
        logging.error("Exception occured.", exc_info=True)
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ("-i", "--input-file"):
            input_file = arg
            logging.info(f"Input file provided: {input_file}")
        elif opt in ("-o", "--output-file"):
            output_file = arg
            logging.info(f"Output file provided: {output_file}")

    if not input_file:
        logging.error("Need an input file.", exc_info=True)
        raise ValueError("Need input file.")
    if not output_file:
        # If no output file has been given we will write to <input_file>.qss
        output_file = input_file[:-4] + 'qss'
        logging.info(f"No output file was provided. The output file will be: {output_file}")

    # print(f"Input file: {input_file}, Output file: {output_file}")
    try:
        with open(input_file, 'r') as f:
            logging.info("Reading input file.")
            text = f.read()
    except IOError:
        logging.error(f"Exception occured: file {input_file} does not exist.", exc_info=True)
        print(f"File {input_file} does not exist. Please check the path of the file.")
        sys.exit(2)

    # Separate variable text from qss text
    text = text.split('\n\n')
    variables_text = text[0]
    logging.debug(f"Variable text: {variables_text}")
    qss_text = '\n\n'.join(text[1:])  # Rebuild split into text
    logging.debug(f"Un-edited qss text: {qss_text}")
    variables = get_variable_dict(variables_text)
    logging.debug(f"Variables dict: {variables}")

    # Replace variables in qss
    qss_text = replace_variables(qss_text, variables)
    logging.debug(f"Updated qss_text")

    try:
        with open(output_file, 'w') as f:
            logging.info("Writing output file")
            f.write(qss_text)
    except IOError:
        logging.error(f"Exception occured.", exc_info=True)
        print(f"Could not open {output_file}")
        sys.exit(2)

    logging.info(f"{output_file} has been written.")


if __name__ == "__main__":
    main()
