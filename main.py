from utils import detect_os, OperatingSystem


def main():
    input("Press enter to confirm that you have completed the forensics questions...")

    os = detect_os()
    if os == OperatingSystem.Linux:
        from linux.linux import main as linux_main
        linux_main()


if __name__ == "__main__":
    main()
