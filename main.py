import subprocess
print("below are the ssid of different network of which the password dumped in the device")
subprocess.run("netsh wlan show profiles",shell = True)
ssid = input("enter the ssid of which you want to get the password : ")
srccde = "netsh wlan show profile \"{}\" key = clear".format(ssid)
with open ("ps.txt", mode = "w") as f:
    subprocess.run(srccde, shell = True, stdout = f)
with open("ps.txt", mode="r") as f:
    print(f.readlines()[32])

