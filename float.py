import sys


decimal = str(
    input(
        """Enter the decimal point for the decimal number.
※ Be sure to include the positive and negative signs.
ex) -118.625 or +118.625
=> """
    )
)


def SignPart(sign: str) -> int:
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


def DecimalToBinary(decimal: float) -> list:
    binary = []

    while decimal != 1.0:
        decimal = decimal * 2
        if decimal > 1.0:
            binary.append(1)
            decimal -= 1.0
        elif decimal == 1.0:
            binary.append(1)
            break
        else:
            binary.append(0)

    return binary


def SinglePrecision():
    point_num = int(decimal.find("."))
    decimal_number = int(decimal[point_num + 1 :])
    div = int(decimal[1:point_num])
    dec = decimal_number / (10 ** len(str(decimal_number)))

    sign = [SignPart(decimal[0])]

    exponent = (len(IntegerToBinary(div)) - 1) + 127
    exponent_add_bias = IntegerToBinary(exponent)

    fraction = list(
        IntegerToBinary(div)[1:]
        + DecimalToBinary(dec)
        + [0] * (23 - int(len(IntegerToBinary(div)[1:] + DecimalToBinary(dec))))
    )

    if len(exponent_add_bias) > 8:
        print("Cannot be expressed in 32 bits.")
    elif len(fraction) > 23:
        print("Cannot be expressed in 32 bits.")
    else:
        print("IEEE754 floating point (single precision)")
        print("sign     : {}".format(sign))
        print("exponent : {}".format(exponent_add_bias))
        print("fraction : {}".format(fraction))


if __name__ == "__main__":
    SinglePrecision()
