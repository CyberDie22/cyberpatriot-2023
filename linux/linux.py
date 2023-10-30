from utils import detect_distro, LinuxDistro


def main():
    # TODO: detect running as root
    distro = detect_distro()
    if distro == LinuxDistro.Ubuntu22:
        from ubuntu22.ubuntu22 import main as ubuntu22_main
        ubuntu22_main()
    