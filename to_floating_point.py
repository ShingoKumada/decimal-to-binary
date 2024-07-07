decimal = str(
    input(
        """Enter the decimal point for the decimal number.
※ Be sure to include the positive and negative signs.
ex) -118.625 or +118.625
=> """
    )
)

if decimal[0] != '-' and decimal[0] != '+':
    decimal = str(
    input(
        """No sign.
※ Be sure to include the positive and negative signs.
ex) -118.625 or +118.625
=> """
    )
)


def determining_the_sign(sign: str) -> int:
    if sign == "-":
        return 1
    else:
        return 0


def integer_to_binary(div: int) -> list:
    binary = []

    while div != 0:
        remainder = div % 2
        div = div // 2
        binary.append(remainder)

    binary = list(reversed(binary))
    return binary


def decimal_to_binary(dec: float) -> list:
    binary = []

    if dec == 0:
        binary.append(0)
        return binary

    while dec != 1.0:
        dec = dec * 2
        if dec > 1.0:
            binary.append(1)
            dec -= 1.0
        elif dec == 1.0:
            binary.append(1)
            break
        else:
            binary.append(0)

    return binary


def single_precision():
    sign_part = [determining_the_sign(decimal[0])]

    point_num = int(decimal.find("."))
    decimal_number = int(decimal[point_num + 1 :])
    div = int(decimal[1:point_num])
    dec = decimal_number / (10 ** len(str(decimal_number)))

    exponent_add_bias = (len(integer_to_binary(div)) - 1) + 127
    exponent_part = integer_to_binary(exponent_add_bias)

    fraction_part = list(
        integer_to_binary(div)[1:]
        + decimal_to_binary(dec)
        + [0] * (23 - int(len(integer_to_binary(div)[1:] + decimal_to_binary(dec))))
    )

    if len(exponent_part) > 8:
        print("Cannot be expressed in 32 bits.")
    elif len(fraction_part) > 23:
        print("Cannot be expressed in 32 bits.")
    else:
        print(
            """ IEEE754 floating point (single precision)
sign     : {}
exponent : {}
fraction : {}""".format(
                sign_part, exponent_part, fraction_part
            )
        )


if __name__ == "__main__":
    single_precision()
