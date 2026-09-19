"""CSC110 Lab 1: Startup Check

Run this file to confirm that your Python and PyCharm setup is working.
You do NOT need to submit this file.

If this runs successfully, you should see a decoded welcome message,
followed by a line reporting the version of Python that ran it.
"""

import sys

_ENCODED_MESSAGE = [
    87, 101, 108, 99, 111, 109, 101, 32, 116, 111, 32, 67, 83, 67, 49, 49,
    48, 33, 32, 73, 102, 32, 121, 111, 117, 32, 99, 97, 110, 32, 114, 101,
    97, 100, 32, 116, 104, 105, 115, 32, 109, 101, 115, 115, 97, 103, 101,
    44, 32, 121, 111, 117, 114, 32, 115, 101, 116, 117, 112, 32, 105, 115,
    32, 119, 111, 114, 107, 105, 110, 103, 32, 58, 41,
]


def decode_message(codes: list[int]) -> str:
    """Return the message encoded as a list of character codes in codes.

    >>> decode_message([104, 105])
    'hi'
    """
    return ''.join(chr(code) for code in codes)


if __name__ == '__main__':
    print(decode_message(_ENCODED_MESSAGE))

    version = sys.version.split()[0]
    print(f'The Python version you are running is {version}.')
    if not version.startswith('3.11'):
        print('WARNING: this course expects Python 3.11. '
              'Please double check your interpreter setup with your TA.')
