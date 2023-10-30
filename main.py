from utils import detect_os, OperatingSystem


def main():
    os = detect_os()
    if os == OperatingSystem.Linux:
        from linux.linux import main as linux_main
        linux_main()


if __name__ == "__main__":
    main()
