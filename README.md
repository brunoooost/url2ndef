# url2ndef

This Python script processes a URL, identifies its protocol, and generates an NFC Data Exchange Format (NDEF) structure. The script supports the following protocols:

## Supported Protocols

- **HTTPS with `www.`**: Identifier `02`  
  Example: `https://www.example.com`

- **HTTP with `www.`**: Identifier `01`  
  Example: `http://www.example.com`

- **HTTPS**: Identifier `04`  
  Example: `https://example.com`

- **HTTP**: Identifier `03`  
  Example: `http://example.com`

- **TEL**: Identifier `05`  
  Example: `tel:+1234567890`

- **MAILTO**: Identifier `06`  
  Example: `mailto:example@example.com`

The script recognizes these protocols and returns a unique identifier for each when processing the URL.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
