#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import asyncio
from bleak import BleakScanner, BleakClient
import time
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

def main():
    # Parse command line arguments
    def parse_arguments():
        parser = argparse.ArgumentParser(description="BLE Terminal Command Line Tool")
        parser.add_argument(
            "-c", "--connect",
            type=str,
            metavar="MAC_ADDRESS",
            help="Connect to a BLE device by specifying its MAC address"
        )
        parser.add_argument(
            "-l", "--list", "--scan", "-s",
            action="store_true",
            help="List (scan) all available BLE devices"
        )
        parser.add_argument(
            "-d", "--describe",
            type=str,
            metavar="MAC_ADDRESS",
            help="Describe the services and characteristics of a BLE device by specifying its address"
        )
        args = parser.parse_args()
        if not any(vars(args).values()):
            parser.print_help()
            exit(1)
        return args

    args = parse_arguments()

    if args.list:
        print("Scanning for BLE devices, please be patient, this may take a while.")

        async def scan_and_list_devices():
            devices = await BleakScanner.discover()
            for device in devices:
                asterisk = ""
                try:
                    async with BleakClient(device.address) as client:
                        services = client.services
                        for service in services:
                            if service.uuid == "0000ffe0-0000-1000-8000-00805f9b34fb":
                                for characteristic in service.characteristics:
                                    if characteristic.uuid == "0000ffe1-0000-1000-8000-00805f9b34fb":
                                        asterisk = "*"
                                        break
                except Exception:
                    pass  # Ignore devices that cannot be connected to
                print(f"{device.address} {device.name} {asterisk} (RSSI: {device.rssi} dBm)")

        asyncio.run(scan_and_list_devices())

    if args.connect:
        async def connect_and_interact(address):
            try:
                def disconnect_handler(_):
                    print("\nDevice disconnected. Exiting...")
                    exit(1)

                async with BleakClient(address, disconnected_callback=disconnect_handler) as client:
                    print(f"Connected to BLE device with address: {address}")

                    # Find the characteristic for communication
                    characteristic_uuid = "0000ffe1-0000-1000-8000-00805f9b34fb"

                    def notification_handler(_, data):
                        print(f"{data.decode('utf-8', errors='ignore')}", end="")

                    # Start notifications
                    await client.start_notify(characteristic_uuid, notification_handler)

                    # Read commands from stdin and write to the characteristic asynchronously
                    async def read_and_write_commands():
                        session = PromptSession(f"{address}> ")
                        with patch_stdout():
                            while True:
                                try:
                                    command = await session.prompt_async()
                                    await client.write_gatt_char(
                                        characteristic_uuid,
                                        f"{command}\r\n".encode('ascii', errors='ignore')
                                    )
                                except (EOFError, KeyboardInterrupt):
                                    print("Exiting...")
                                    break

                    # Run the read and write commands task concurrently with notifications
                    await asyncio.gather(read_and_write_commands())

                    # Stop notifications
                    await client.stop_notify(characteristic_uuid)
            except Exception as e:
                print(f"Failed to connect or interact with device {address}: {e}")

        asyncio.run(connect_and_interact(args.connect))

    if args.describe:
        async def describe_device(address):
            try:
                async with BleakClient(address) as client:
                    services = client.services
                    print(f"Services and characteristics for device {address}:")
                    for service in services:
                        print(f"Service: {service.uuid}")
                        for characteristic in service.characteristics:
                            print(f"  Characteristic: {characteristic.uuid}")
                            print(f"    Properties: {characteristic.properties}")
            except Exception as e:
                print(f"Failed to describe device {address}: {e}")

        asyncio.run(describe_device(args.describe))

if __name__ == "__main__":
    main()