# BLETerminal

BLETerminal is a project designed to facilitate communication with Bluetooth Low Energy (BLE) device UART port. It provides a user-friendly interface for sending and receiving data with UART over BLE Service UUID 0000ffe0-0000-1000-8000-00805f9b34fb and Characteristic UUID 0000ffe1-0000-1000-8000-00805f9b34fb.

## Features

- Scan for nearby BLE devices.
- Connect to BLE device.
- Send and receive data with BLE UART port.
- Cross-platform support.

## Requirements

To use BLETerminal, ensure you have the following:

- Python 3.7 or higher
- `pybluez` library for Bluetooth communication
- `bleak` library for BLE device interaction
- A compatible BLE adapter (tested with JDY-23)
- Optional: `virtualenv` for managing dependencies

## Installation

To install BLETerminal, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/pabloestrado/bleterminal.git
    ```
2. Navigate to the project directory:
    ```bash
    cd bleterminal
    ```
3. Install the package using `setup.py`:
    ```bash
    python setup.py install
    ```

## Usage

BLETerminal provides a command-line interface for interacting with BLE devices. Below are the available commands and examples:

### Scan for BLE Devices
To discover nearby BLE devices:
```bash
bleterminal/bleterminal --scan
```

### Connect to a BLE Device
To connect to a specific BLE device, use its MAC address:
```bash
bleterminal/bleterminal --connect 00:11:22:33:44:55
```

### Describe BLE Device Services and Characteristics
To discover nearby BLE devices:
```bash
bleterminal/bleterminal --describe 00:11:22:33:44:55
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

