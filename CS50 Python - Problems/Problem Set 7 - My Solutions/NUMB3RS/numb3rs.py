import re

def main() -> None:
    address = input("IPv4 Address: ")

    print(validate(address))


def validate(ip: str) -> bool:
    verifiedIP = re.fullmatch(r"^(25[0-5]|2[0-4][0-9]|[0-]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$", ip)

    return verifiedIP is not None

if __name__ == "__main__":
    main()