import subprocess
import pyfiglet

text=pyfiglet.figlet_format("MR . PING")

print(text)

print("Enter the targate ip / url :")
ip=input()

print("Your targate is :",ip)

subprocess.call("ping "+ ip,shell=True)

