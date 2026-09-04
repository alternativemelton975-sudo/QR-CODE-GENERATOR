# QR Code Generator

A simple Python utility to generate QR codes from text or URLs.

## Features

- **QR Code Generation** - Convert text or URLs to QR codes
- **Customizable** - Adjust version, error correction, box size, border
- **PNG Output** - Saves QR codes as high-quality PNG images
- **Simple API** - Easy-to-use functions

## Requirements

- Python 3.11+
- qrcode library
- Pillow (PIL)

## Installation

```bash
git clone https://github.com/yourusername/qrcode-generator.git
cd qrcode-generator
pip install -r requirements.txt
python QrCodeGenerator.py
```

## Usage

### Command Line

```bash
python QrCodeGenerator.py
```

This will generate a QR code for `https://b001.io` and save it as `qr_code.png`.

### As a Module

```python
from QrCodeGenerator import generate_qr_code

# Generate QR code
generate_qr_code("https://example.com", "my_qr_code.png")
```

## Configuration

Edit the `QrCodeGenerator.py` file to customize:

```python
text = "https://b001.io"  # Change this URL
file_name = "qr_code.png"  # Change output filename
```

### QR Code Parameters

- `version` - Controls the size of the QR code (1-40)
- `error_correction` - Error correction level (L, M, Q, H)
- `box_size` - Size of each box in pixels
- `border` - Border size in boxes

## Docker

Build and run with Docker:

```bash
docker build -t qrcode-generator .
docker run qrcode-generator:latest
```

The generated QR code will be in the container's `/app` directory.

## Output

The QR code is saved as a PNG image that can be:
- Scanned with any QR code reader
- Embedded in documents
- Used in web applications
- Printed

## License

MIT

## Author

Your Name
