from utils import run_shell, install_package
import pwd
import grp


def main():
    system_update()
    check_users()
    change_user_passwords()
    password_expiration()
    pamd()
    shadow()
    enable_ufw()
    set_ufw_rules()
    set_ssh_config()
    set_login_defs()
    print("check grub config")
    
def system_update():
    print("Updating System Packages")
    run_shell("apt-get update")
    run_shell("apt-get upgrade")


def check_users():
    auth_admins = input("Input the allowed administrators separated by commas: ").split(",")
    auth_users = input("Input the allowed users separated by commas: ").split(",")
    
    sudo = grp.getgrnam("sudo")
    
    # TODO: Grab MIN_UID and MAX_UID from /etc/login.defs
    users = [user.pw_name for user in pwd.getpwall() if 1000 <= user.pw_uid <= 60000]
    admins = [user for user in sudo.gr_mem]
    
    unauth_users = [user for user in users if user not in auth_users]
    unauth_admins = [admin for admin in admins if admin not in auth_admins]
    
    for admin in unauth_admins:
        run_shell(f"userdel {admin} sudo")
    
    for user in unauth_users:
        run_shell(f"userdel {user}")

def change_user_passwords():
    users = [user.pw_name for user in pwd.getpwall() if 1000 <= user.pw_uid <= 60000]

    print("Setting user passwords to `securepassword`")
    for user in users:
        run_shell(f"yes securepassword > passwd {user}")

def password_expiration():
    print("Setting Password Expiration")

    with open("/etc/login.defs", "w") as f:
        lines = f.readlines()

        idx = 0
        for line in lines:
            if line.startswith("PASS_MAX_DAYS"):
                lines[idx] = "PASS_MAX_DAYS\t30"
            if line.startswith("PASS_MIN_DAYS"):
                lines[idx] = "PASS_MIN_DAYS\t3"
            if line.startswith("PASS_WARN_DAYS"):
                lines[idx] = "PASS_WARN_DAYS\t7"
            idx += 1

        f.writelines(lines)

def pamd():
    # TODO: finish pam.d
    print("TODO: finish pam.d")

def shadow():
    print("Update shadow file")
    with open("/etc/shadow", "w") as f:
        lines = f.readlines()

        idx = 0
        for line in lines:
            lines[idx] = line.replace(":0:99999:7:::", ":3:30:7")

        f.writelines(lines)

def enable_ufw():
    print("Enable UFW")
    install_package("ufw")
    run_shell("ufw enable")

def set_ufw_rules():
    print("Set UFW Rules")
    run_shell("ufw allow in on lo")
    run_shell("ufw allow out on lo")
    run_shell("ufw deny in from 127.0.0.0/8")
    run_shell("ufw deny in from ::1")
    run_shell("ufw allow out on all")
    print("run ufw allow in/out port/(tcp/udp)")

def set_ssh_config():
    print("Set SSH Config")
    with open("/etc/ssh/sshd_config", "w") as f:
        lines = f.readlines()

        idx = 0
        for line in lines:
            if "PermitRootLogin" in line:
                lines[idx] = "PermitRootLogin no"
            if "X11Forwarding" in line:
                lines[idx] = "X11Forwarding no"
            idx += 1

        f.writelines(lines)
    print("Check sshd_config.d")

def set_login_defs():
    print("Set login.defs")
    with open("/etc/login.defs", "w") as f:
        lines = f.readlines()

        idx = 0
        for line in lines:
            if "FAILLOG_ENAB" in line:
                lines[idx] = "FAILLOG_ENAB yes"
            if "LOG_UNKFAIL_ENAB" in line:
                lines[idx] = "LOG_UNKFAIL_ENAB yes"
            if "LOG_OK_LOGINS" in line:
                lines[idx] = "LOG_OK_LOGINS yes"
            if "SYSLOG_SU_ENAB" in line:
                lines[idx] = "SYSLOG_SU_ENAB yes"
            if "SYSLOG_SG_ENAB" in line:
                lines[idx] = "SYSLOG_SG_ENAB yes"
            if "SULOG_FILE" in line:
                lines[idx] = "SULOG_FILE /var/log/sulog"
            if "FMTP_FILE" in line:
                lines[idx] = "FMTP_FILE /var/log/fmtp"
            if "SU_NAME" in line:
                lines[idx] = "SU_NAME su"
            if "LOGIN_RETRIES" in line:
                lines[idx] = "LOGIN_RETRIES 5"
            if "LOGIN_TIMEOUT" in line:
                lines[idx] = "LOGIN_TIMEOUT 60"
            if "ENCRYPT_METHOD" in line:
                lines[idx] = "ENCRYPT_METHOD SHA512"
