Spacemouse requires some installation as described here robosuite/robosuite/devices/spacemouse.py


### Step 1: Install the driver
Download and install driver from https://www.3dconnexion.com/service/drivers.html

### Step 2: Install hidapi library
```bash
pip install hidapi
```

### Step 3: Change the vendor id and product id
Change the vendor id and product id that correspond to the device. In the robosuite/robosuite/macros.py change the following (use actual id)
```
   SPACEMOUSE_VENDOR_ID = 9583
   SPACEMOUSE_PRODUCT_ID = 50734
```

Actual id can be found by running the following command.
```
lsusb
```
You should see a list of devices, including something similar as below: 
```
Bus 003 Device 006: ID 256f:c62e 3Dconnexion SpaceMouse Wireless (cabled)
``` 
Here, the vendor id is 256f and product id is c62e. Convert the hex to decimal to get the actual id.


### Step 4: Update permission

sudo nano /etc/udev/rules.d/99-spacemouse-permissions.rules
Then add the following lines to the file
```bash 
SUBSYSTEM=="usb", ATTR{idVendor}=="256f", ATTR{idProduct}=="c62e", MODE="0666"
KERNEL=="hidraw", ATTRS{idVendor}=="256f", ATTRS{idProduct}=="c62e", MODE="0666"
```

Then run the following commands
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```


