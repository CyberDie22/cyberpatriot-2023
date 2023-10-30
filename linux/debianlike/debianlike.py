from utils import run_shell
import pwd
import grp


def main():
    system_update()
    check_users()
    
    
def system_update():
    run_shell("apt-get update")
    run_shell("apt-get upgrade")


def check_users():
    auth_admins = input("Input the allowed administrators separated by commas: ").split(",")
    auth_users = input("Input the allowed users separated by commas: ").split(",")
    
    sudo = grp.getgrnam("sudo")
    
    users = [user.pw_name for user in pwd.getpwall() if 1000 <= user.pw_uid <= 60000]
    admins = [user for user in sudo.gr_mem]
    
    unauth_users = [user for user in users if user not in auth_users]
    unauth_admins = [admin for admin in admins if admin not in auth_admins]
    
    for admin in unauth_admins:
        sudo.gr_mem.remove(admin)
    
    for user in unauth_users:
        run_shell(f"userdel {user}")
