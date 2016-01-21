import socket
import struct


class IpGen(object):
    def __init__(self, ip_range):
        ip1, ip2 = ip_range.split('-')
        self.start = self._atoi(ip1)
        self.end = self._atoi(ip2)
        self.current = self.start

    def available(self):
        return self.end - self.current >= 0

    def alloc(self):
        if self.available():
            ip = self.current
            self.current += 1
            return self._itoa(ip)
        else:
            raise Exception("sorry, all ips have been allocated.")

    def _atoi(self, ip):
        d = struct.unpack('i', socket.inet_aton(ip))[0]
        return socket.ntohl(d)

    def _itoa(self, ip):
        d = struct.pack('i', socket.htonl(ip))
        return socket.inet_ntoa(d)


if __name__ == "__main__":
    pool = IpGen("192.168.188.1-192.168.188.10")
    while pool.available():
        print pool.alloc()