import platform
import socket

print("Halo dari container!")
print("Sistem operasi:", platform.system())
print("Hostname:", socket.gethostname())