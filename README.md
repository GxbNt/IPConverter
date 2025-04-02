# IP Address Converter

This tool takes an IPv4 address and converts it into multiple alternative representations including:

- Decimal
- Packed integer (DWORD)
- Hexadecimal (various formats)
- Octal (standard and padded)
- Percent-encoded
- Mixed notation
- Unicode-styled fancy format

---

## Usage

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/ip-converter.git
   cd ip-converter
2. Run the script
   ```bash
   python3 ip_converter.py
3. Enter an IPv4 address when prompted
   ```bash
   Enter IPv4 address: 127.0.0.1

---

## Example Outputs
   ```bash
http://127.0.0.1
http://127.0.1
http://127.1
http://2130706433
http://0x7f.0x0.0x0.0x1
http://0x7f000001
http://127.0x000001
http://127.0.0.0x01
http://0177.00.00.01
http://00177.00.000000.00001
http://017700000001
http://%31%32%37%2e%30%2e%30%2e%31
http://127.0x0.0.1
http://①②⑦ï¼Ž⓪ï¼Ž⓪ï¼Ž①
