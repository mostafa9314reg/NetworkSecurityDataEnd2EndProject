import socket

try:
    socket.getaddrinfo("ac-wegkch0-shard-00-00.ypqqlsp.mongodb.net", 27017)
    print("DNS resolution works ✅")
except Exception as e:
    print("DNS failed ❌", e)