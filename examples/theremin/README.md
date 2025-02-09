# Theremin with DepthAI

Running Google Mediapipe Hand Tracking models on [DepthAI](https://docs.luxonis.com/en/gen2/) hardware (OAK-1, OAK-D, ...)


## Dependency
- Sonic Pi
- depthai==2.9.0.0
- python-sonic

## Setup

Install Sonic Pi(Linux):
```sh
$ sudo apt update
$ sudo apt install sonic-pi
```

Install Sonic Pi(Mac):
```sh
$ brew install sonic-pi
```

Install Python Library
```sh
$ python3 -m pip install depthai==2.9.0.0
$ pip3 install python-sonic
```

Download files:
```sh
$ cd && git clone git clone https://github.com/karaage0703/depthai_hand_tracker
```

## Usage
Launch Sonic Pi and Execute following commands:

```sh
$ cd ~/depthai_hand_tracker/examples/theremin/
$ python3 theremin.py
```

If you want to edge mode for speed up, execute following commands:

```sh
$ cd ~/depthai_hand_tracker/examples/theremin/
$ python3 theremin.py -e
```


## License
This software is released under the MIT License, see LICENSE.txt.

## Credits
* [Google Mediapipe](https://github.com/google/mediapipe)
* Katsuya Hyodo a.k.a [Pinto](https://github.com/PINTO0309), the Wizard of Model Conversion !
