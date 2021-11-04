from crypto_hash import crypto_hash

HEX_2_BINARY_CONVERSION_TABLE = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def main():
    number = 1
    hex_number = hex(number)[2:]
    print(f'hex_number: {hex_number}')

    binary_number = "{0:08b}".format(int(hex_number, 16))
    print(f'binary_number: {binary_number}')

    original_number = int(binary_number, 2)
    print(f'original_number: {original_number}')

    hex_2_binary_crypto_hash = "{0:08b}".format(int(crypto_hash('test'), 16))
    print(f'hex_2_binary_crypto_hash: {hex_2_binary_crypto_hash}')


if __name__ == '__main__':
    main()
