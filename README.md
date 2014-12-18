PyPixel
=======

A Python Wrapper for The Hypixel API (https://api.hypixel.net). By @TheDestruc7i0n and @WireSegal



Installation
------------

Download the tarball here: https://github.com/destruc7i0n/PyPixel/archive/1.1.tar.gz

If you're using Mac or Linux:

Using your terminal, go to the folder that contains the tarball. Then run these:
```
tar PyPixel-1.0.tar.gz
cd PyPixel-1.0
sudo python setup.py install
```
Enter your password and you're good to go.



If you're using Windows:

Unpack the tarball. Open Command Prompt, and go into the folder named PyPixel-1.0.
Run this in command prompt:
```
python setup.py install
```


Use
---

To use the pypixel library, just add this into the top of your code:

```
import pypixel
```

To initate an API instance, use this command (pass your API key to the class):

```
api = pypixel.HypixelAPI(key)
```

Remember that you can only make 60 API calls per minute per key.
