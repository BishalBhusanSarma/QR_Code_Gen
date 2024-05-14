# QR_Code_Gen

This Python project generates QR codes from user-provided data or URLs. The generated QR codes are saved as PNG images.

## Features

- Accepts user input for the data to encode into a QR code.
- Configurable QR code version, box size, and border size.
- Saves the QR code as a PNG image file.


## Prerequisites

- Python 3.x
- `qrcode` library

## Installation
**Install the required library:**
    ```
    pip install qrcode
    ```

## Usage

1. Run the script:
    ```
    python qr_code_generator.py
    ```

2. Enter the link or data when prompted:
    ```
    Enter Your Link or Data Here:
    ```

3. The generated QR code will be saved as `testQR.png` in the current directory.

## Example

```python
import qrcode

def generate_qr_code(data, file_path, version=7, box_size=10, border=5):
    try:
        qr = qrcode.QRCode(
            version=version,
            box_size=box_size,
            border=border
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(file_path)
        print(f"QR code saved as {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    data = input("Enter Your Link or Data Here:\n")
    file_path = "test.png"
    generate_qr_code(data, file_path)
```

## Contact


For any questions or suggestions, please contact me (Bishal Bhusan Sarma) at bishalbhusansarma87787@gmail.com.
Thank You.



