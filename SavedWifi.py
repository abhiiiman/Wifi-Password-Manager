# importing the lib here to work with the cmd.
import subprocess

# getting the list of ssid here.
def get_ssid():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode("utf-8")
    data = data.split("\n")
    ssid_list = []
    for line in data:
        if "    All User Profile     : " in line:
            ssid = line.replace("    All User Profile     : ", "")
            ssid_list.append(ssid.replace("\r", ""))
    return ssid_list

# getting their respective passwords here.
def get_password():
    for ssid in get_ssid():
        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, "key=clear"])
        data = meta_data.decode("utf-8", errors= "backslashreplace")
        data = data.split("\n")
        for line in data:
            if "Key Content" in line:
                password = line.split(":")[1]
        print(ssid, ":", password)

# calling the func here for ssid profiles.
get_ssid()
# calling the func here for fetching their respective passwords.
get_password()
