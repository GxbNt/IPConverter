import socket
import struct
import urllib.parse
import random

def ip_to_int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]

def convert_ip(ip):
    o1, o2, o3, o4 = map(int, ip.split('.'))
    ip_int = ip_to_int(ip)

    decimalv1 = f"http://{ip}"
    classb = f"http://{o1}.{o2}.{o3 * 256 + o4}"
    classa = f"http://{o1}.{o2 * 256**2 + o3 * 256 + o4}"
    dwordv1 = f"http://{ip_int}"

    hexv1 = f"http://{'.'.join(f'0x{x:x}' for x in [o1, o2, o3, o4])}"
    hexv2 = f"http://0x{''.join(f'{x:02x}' for x in [o1, o2, o3, o4])}"
    hexv3 = f"http://{o1}.0x{''.join(f'{x:02x}' for x in [o2, o3, o4])}"
    hexv4 = f"http://{o1}.{o2}.{o3}.0x{o4:02x}"

    octalv1 = f"http://{'.'.join(f'0{o:o}' for o in [o1, o2, o3, o4])}"
    random.seed(42)
    octalv2 = 'http://' + '.'.join('0' * random.randint(1, 8) + f"{x:o}" for x in [o1, o2, o3, o4])
    octalv3 = f"http://0{oct(ip_int)[2:]}"

    percentv1 = "http://" + ''.join(f"%{ord(c):x}" for c in ip)
    mixedv1 = f"http://{o1}.0x{o2:x}.{oct(o3)[2:]}.{o4}"

    unicode_digits = {
        '0': '⓪', '1': '①', '2': '②', '3': '③', '4': '④',
        '5': '⑤', '6': '⑥', '7': '⑦', '8': '⑧', '9': '⑨'
    }
    unicode = "http://" + 'ï¼Ž'.join(
        ''.join(unicode_digits.get(ch, ch) for ch in part) for part in ip.split('.')
    )

    return [
        decimalv1,
        classb,
        classa,
        dwordv1,
        hexv1,
        hexv2,
        hexv3,
        hexv4,
        octalv1,
        octalv2,
        octalv3,
        percentv1,
        mixedv1,
        unicode,
    ]

if __name__ == "__main__":
    ip = input("Enter IPv4 address: ").strip()
    try:
        socket.inet_aton(ip)  # validate IP
        results = convert_ip(ip)
        for url in results:
            print(url)
    except socket.error:
        print("Invalid IPv4 address.")
