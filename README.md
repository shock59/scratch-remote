# Scratch Remote

Scratch Remote is a remote desktop client and server. The client is made in Scratch and the server is made in Python. You will also need to run a CloudLink server such as [this one](https://github.com/MikeDev101/cloudlink/blob/master/server_example.py).

**NOTE:** Scratch Remote is not meant for practical use and I have no reponsibility for whatever happens if you install it. I strongly discourage installing this on your main computer as it can give anyone complete control over it if they have your IP.

## Features

- View the server's screen
- Basic keyboard input

### Todo

- Mouse control
- Keyboard input not supported by Scratch

## Installation

### Client (Scratch)

The Scratch client can be used on [adacraft](https://beta.adacraft.org/studio/?project=fd3d362b), or you can download the sb3 and run it in a Scratch Editor of your choice after installing the CloudLink. It is strongly reccomended to use [TurboWarp](https://turbowarp.org/) or an editor that includes TurboWarp such as adacraft Beta and enable the TurboWarp compiler for the best performance. [Scratch Addons](https://scratchaddons.com/) (included with TurboWarp) is also required to see the log.

### Server (Python)

Install the dependencies:

```bash
pip install pyautogui cloudlink
```

Then download or clone the repository and open the `server` directory.

## Use

To begin, run a CloudLink server and copy the IP (including `ws://` or `wss://`) into the `config.ini` file for the Scratch Remote server.

Run the Scratch Remote server with

```bash
python3 server.py
```

Then open the Scratch client and paste in the IP of the CloudLink server. Scratch will render whatever is in the range defined in `config.ini`.
