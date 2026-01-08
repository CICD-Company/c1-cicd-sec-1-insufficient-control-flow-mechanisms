from app.calculator import add
from utils import log


def main():
    print("CI/CD Flow Control Demo")
    print("2 + 3 =", add(2, 3))

    log("Calculator started")

    print("Small update")

    print("Auto merge has been abused")


if __name__ == "__main__":
    main()
