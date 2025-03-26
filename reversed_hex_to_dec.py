import sys

def reversed_hex_to_decimal(hex_str):
    # Entferne Leerzeichen und teile die Hex-Zeichen in Bytes (2 Zeichen pro Byte)
    hex_bytes = hex_str.replace(" ", "")
    
    # Stelle sicher, dass die Länge gerade ist (jedes Byte hat 2 Zeichen)
    if len(hex_bytes) % 2 != 0:
        print("Ungültige Hexadezimalzahl! Sie muss eine gerade Anzahl von Zeichen haben.")
        sys.exit(1)
    
    # Teile den String in 2-stellige Bytes und kehre die Reihenfolge um
    reversed_bytes = [hex_bytes[i:i+2] for i in range(0, len(hex_bytes), 2)][::-1]
    
    # Setze die umgekehrten Bytes wieder zu einer neuen Hex-Zahl zusammen
    corrected_hex = "".join(reversed_bytes)
    
    # Wandle die korrigierte Hex-Zahl in Dezimal um
    decimal_value = int(corrected_hex, 16)
    
    return decimal_value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python reversed_hex_to_dec.py <reversed hexadezimale Zahl>")
        sys.exit(1)

    hex_input = sys.argv[1]  # Reversed Hexadezimal-Eingabe
    decimal_output = reversed_hex_to_decimal(hex_input)

    print(decimal_output)
