# Theremin with DepthAI

Running Google Mediapipe Hand Tracking models on [DepthAI](https://docs.luxonis.com/en/gen2/) hardware (OAK-1, OAK-D, ...)


## Dependency

- pymycobot==2.3.3
- depthai==2.9.0.0
- python-sonic

## Setup

Linux PC or Mac

Install Python Library
```sh
$ pip3 install pyserial
$ pip3 install pymycobot==2.3.3
```

Download files:
```sh
$ cd && git clone git clone https://github.com/karaage0703/depthai_hand_tracker
```

## Usage
Execute following commands:
```sh
$ cd ~/depthai_hand_tracker/examples/robot_control
$ python3 robot_control.py -e
```

Press C key.

## License
This software is released under the MIT License, see LICENSE.txt.

## Credits
* [Google Mediapipe](https://github.com/google/mediapipe)
* Katsuya Hyodo a.k.a [Pinto](https://github.com/PINTO0309), the Wizard of Model Conversion !
