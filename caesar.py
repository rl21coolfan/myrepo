from __future__ import print_function
import os
import string
import argparse

try:
    maketrans = string.maketrans  # python2
except AttributeError:
    maketrans = str.maketrans  # python3


def caesar_cipher(string_: str, offset: int, decode: bool, file_: string) -> None:
    """ caesar Cipher implementation, reads file or string.  Also decodes.

    Default implementation is ROT13 encoding.

    To decode, specify the same offset you used to encode and your ciphertext / file.

    :param string_: string to encode / decode
    :param offset:  # of chars to rotate by
    :param decode:  decode instead of encode
    :param file_:   file to read in then encode/decode
    """
    if file_ and os.path.exists(file_):
        with open(file_, 'r') as f:
            string_ = f.read()

    if decode:
        offset *= -1

    lower_offset_alphabet = string.ascii_lowercase[offset:] + string.ascii_lowercase[:offset]
    lower_translation_table = maketrans(string.ascii_lowercase, lower_offset_alphabet)

    upper_offset_alphabet = string.ascii_uppercase[offset:] + string.ascii_uppercase[:offset]
    upper_translation_table = maketrans(string.ascii_uppercase, upper_offset_alphabet)

    lower_converted = string_.translate(lower_translation_table)
    final_converted = lower_converted.translate(upper_translation_table)

    if file_:
        extension = 'dec' if decode else 'enc'
        with open("{}.{}".format(file_, extension), 'w') as f:
            print(final_converted, file=f)
    else:
        print(final_converted)


def check_offset_range(value: int) -> int:
    """ Validates that value is in the allowable range.

    :param value:  integer to validate
    :return:  valid integer
    :raises: argparse.ArgumentTypeError
    """
    value = int(value)
    if value < -25 or value > 25:
        raise argparse.ArgumentTypeError("{} is an invalid offset".format(value))
    return value
