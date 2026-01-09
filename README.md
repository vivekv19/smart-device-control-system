# smart-device-control-system
OOP-based smart device control system (Motor and Light)

## Overview
This project implements a simple and scalable smart device control system using Object-Oriented Programming principles in Python. The system supports multiple devices and a generic controller that can operate any device.

## Technologies Used
- Python 3.x

## Project Structure
smart_device_system/
│
├── device.py
├── motor.py
├── light.py
├── controller.py
└── main.py

## How to Run
1. Ensure Python 3.x is installed.
2. Navigate to the project directory.
3. Run the following command:

   python main.py

## Expected Output
Motor has started  
Motor has stopped  
Light switched on  
Light switched off  

## Design Highlights
- Encapsulation to protect device state
- Inheritance for device types
- Polymorphism for controller operation
- Easily extendable for future devices

## Assumptions
- Device state is managed internally.
- External code can only read device status, not modify it.
