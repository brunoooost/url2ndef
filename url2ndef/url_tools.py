# Function to identify protocol
def identificar_protocolo(url):
    protocols = {
        "https://www.": "02",
        "http://www.": "01",
        "https://": "04",
        "http://": "03",
        "tel:": "05",
        "mailto:": "06"
    }

    for protocol, identifier in protocols.items():
        if url.startswith(protocol):
            return identifier

    return "No se detectó un protocolo"

# Function to get the length of the rest and convert to hex
def obtener_longitud_resto(url):
    protocols = ["https://www.", "http://www.", "https://", "http://", "ftp://"]
    resto = next((url[len(protocol):] for protocol in protocols if url.startswith(protocol)), url)

    # Convert the rest of the URL to hex (UTF-8 encoding)
    resto_hex = [format(byte, '02X') for byte in bytearray(resto, 'utf-8')]
    return len(resto) + 1, [resto_hex[i:i+2] for i in range(0, len(resto_hex), 2)]

# Function to generate the NDEF structure
def generar_ndef(url):
    longitud_resto, resto_hex = obtener_longitud_resto(url)

    # NFC parameters
    NFC_TYPE = "D1"                                 # NFC type
    LENGTH_RECORD = "01"                            # Length record of URL
    LENGTH_PAYLOAD = str(longitud_resto)            # Length of the payload
    URI_TYPE = "55"                                 # URI type
    URI_IDENTIFIER = identificar_protocolo(url)     # URI identifier
    STRING = ' '.join(resto_hex)                    # Content of the URL (string)

    # NDEF structure
    STRUCTURE_NDEF = [NFC_TYPE, LENGTH_RECORD, LENGTH_PAYLOAD, URI_TYPE, URI_IDENTIFIER, STRING]

    # Final result
    resultado = ' '.join([num.zfill(2) for num in ' '.join(STRUCTURE_NDEF).split()])

    return resultado
