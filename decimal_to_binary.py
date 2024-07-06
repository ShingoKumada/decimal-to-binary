decimal = str(
    input(
        """Enter the decimal point for the decimal number.
※Be sure to include the positive and negative signs.
ex) -118.625 or 118.625
=> """
    )
)


def DeterminingTheSign(sign: str) -> int:
    if sign == "-":
        return 1
    else:
        return 0


def IntegerToBinary(div: int) -> list:
    binary = []

    while div != 0:
        remainder = div % 2
        div = div // 2
        binary.append(remainder)

    binary = list(reversed(binary))
    return binary


def DecimalToBinary(dec: float) -> list:
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


def SinglePrecision():
    sign_part = [DeterminingTheSign(decimal[0])]

    point_num = int(decimal.find("."))
    decimal_number = int(decimal[point_num + 1 :])
    div = int(decimal[1:point_num])
    dec = decimal_number / (10 ** len(str(decimal_number)))

    exponent_add_bias = (len(IntegerToBinary(div)) - 1) + 127
    exponent_part = IntegerToBinary(exponent_add_bias)

    fraction_part = list(
        IntegerToBinary(div)[1:]
        + DecimalToBinary(dec)
        + [0] * (23 - int(len(IntegerToBinary(div)[1:] + DecimalToBinary(dec))))
    )

    if len(exponent_part) > 8:
        print("Cannot be expressed in 32 bits.")
    elif len(fraction_part) > 23:
        print("Cannot be expressed in 32 bits.")
    else:
        print("IEEE754 floating point (single precision)")
        print("sign     : {}".format(sign_part))
        print("exponent : {}".format(exponent_part))
        print("fraction : {}".format(fraction_part))


if __name__ == "__main__":
    SinglePrecision()
