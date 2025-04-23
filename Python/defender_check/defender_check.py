# Imports and libraries
from pyamsi import Amsi
import argparse
import sys
from colorama import init, Fore


# initialize colorama for Windows
init()


# Function declarations

#
# amsi_check takes 3 arguments and returns the results
# of a scan to the calling function (main in this case)
#
def amsi_check(object_var, scan_type, debug_var=False):
    if scan_type.lower() == 'string':
        string_name = 'User-supplied string.'
        return Amsi.scan_string(object_var, string_name, debug=debug_var)
    elif scan_type.lower() == 'file':
        try:
            results = Amsi.scan_file(object_var, debug=debug_var)
            return results
        except:
            print('\n{}[!] Error! The file or file path is incorrect or does not exist. Exiting...{}\n'.format(
                Fore.YELLOW, Fore.RESET))
            sys.exit(1)
    else:
        print('\n{}[!] Error! User must provide a string or a file path to check. Exiting...{}\n'.format(
            Fore.YELLOW, Fore.RESET))
        sys.exit(1)


#
# and options and then passes the correct objects
# to the amsi_check function for testing
#
def main():
    parser = argparse.ArgumentParser(
        prog='defender_check.py',
        description='A simple script to compare a file or string against the AMSI engine.',
        usage='%(prog)s [options]',
        epilog='by Blu3gl0w13 - April 23, 2025'
    )
    group_args = parser.add_mutually_exclusive_group(required=True)
    group_args.add_argument('-f', '--file', dest='file_name', help='File or file path to test.')
    group_args.add_argument('-s', '--string', dest='string_value', help='String to test.')
    arguments = parser.parse_args()
    test_object = arguments.file_name if arguments.file_name is not None else arguments.string_value
    type_object = 'file' if arguments.file_name else 'string'
    results = amsi_check(test_object, type_object, False)
    if 2 > results['Risk Level'] >= 0 or results['Message'].lower() == 'n/a':
        print("\n{}[+] Results: {}{}\n".format(Fore.BLUE, results, Fore.RESET))
    elif results['Risk Level'] >= 2 and results['Message'].lower() != 'n/a':
        print("\n{}[-] Results: {}{}\n".format(Fore.RED, results, Fore.RESET))
    else:
        print("\n{}[!] Error: Unexpected results. Possible error with AMSI.{}\n".format(Fore.YELLOW, Fore.RESET))
    sys.exit(0)


# Call main if this is a standalone script
if __name__ == "__main__":
    main()
