import subprocess, platform, os
from typing import Optional
from enum import Enum


class OperatingSystem(Enum):
    Linux = 'Linux'
    
    
class LinuxDistro(Enum):
    Ubuntu22 = 'Ubuntu 22'
    Ubuntu20 = 'Ubuntu 20'
    Debian11 = 'Debian 11'


def unknown_os(name: Optional[str] = None):
    if not name:
        print("Unknown operating system")
    else:
        print(f"Unknown operating system {name}")
    exit(-1)
    
    
def unknown_distro(name: Optional[str] = None):
    if not name:
        print("Unknown linux distro")
    else:
        print(f"Unknown linux distro {name}")
    exit(-1)


memo_os: Optional[OperatingSystem] = None
def detect_os() -> OperatingSystem:
    global memo_os
    if memo_os:
        return memo_os
    
    system = platform.system()
    match system:
        case OperatingSystem.Linux:
            memo_os = OperatingSystem.Linux
            return memo_os
        case _:
            unknown_os(system)

memo_distro: Optional[LinuxDistro] = None
def detect_distro() -> LinuxDistro:
    global memo_distro
    if memo_distro:
        return memo_distro
    
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release", "r") as f:
            lines = f.readlines()
            
        name = None
        ver = None
        for line in lines:
            if line.startswith("ID="):
                split = line.split("=")
                name = split[1]
            if line.startswith("VERSION_ID="):
                split = line.split("=")
                ver = split[1]
                
        if not name:
            unknown_distro()
            
        if not ver:
            unknown_distro()
        
        match name:
            case "ubuntu":
                if ver.startswith('"22'):  # TODO: check if this is correct
                    memo_distro = LinuxDistro.Ubuntu22
                    return memo_distro
                elif ver.startswith('"20'):  # TODO: check if this is correct
                    memo_distro = LinuxDistro.Ubuntu20
                    return memo_distro
                else:
                    unknown_distro(f"{name} {ver}")
            case "debian":
                if "11" in ver:  # TODO: check if this is correct
                    memo_distro = LinuxDistro.Debian11
                else:
                    unknown_distro(f"{name} {ver}")
            case _:
                unknown_distro(f"{name} {ver}")
            

def run_shell(command: str) -> tuple[int, str, str]:
    operating_system = detect_os()
    if operating_system == OperatingSystem.Linux:
        shell = "/bin/bash"
    else:
        unknown_os()
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True, executable=shell)
        stdout = result.stdout
        stderr = result.stderr
        exit_code = result.returncode
    except subprocess.CalledProcessError as e:
        stdout = e.stdout
        stderr = e.stderr
        exit_code = e.returncode
        
    return exit_code, stdout, stderr
