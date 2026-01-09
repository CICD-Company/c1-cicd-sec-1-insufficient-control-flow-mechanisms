from calculator import add
from utils import log


def main():
    print("2 + 3 =", add(2, 3))

    # Function of the shared library ([HACK])
    log("Calculator started after Utility-library hack")


if __name__ == "__main__":
    main()
