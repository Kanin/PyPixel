<div align="center">

<h1>PyPixel</h1>

A Python Wrapper for The Hypixel API (https://api.hypixel.net). Originally by @TheDestruc7i0n and @WireSegal

Rewrite starting soon...

Installation
============

Download the zip here: https://github.com/destruc7i0n/PyPixel/archive/master.zip

If you're using Linux:

Download the source zip, and unpack it. From the folder created, run this command: 
```
sudo python3 setup.py install
```
Enter your password and you're good to go.

If you're using Mac:

Almost the same as Linux but the command is:
```
sudo python setup.py install
```


If you're using Windows:

Unpack the zip. Open Command Prompt, and go into the folder named PyPixel-1.0.
Run this in command prompt:
```
python setup.py install
```


Use
===

To use the pypixel library, just add this into the top of your code:

```
import pypixel
```

Single-Key Instance
-------------------

To initate an API instance, use this command (pass your API key to the class):

```
api = pypixel.HypixelAPI(key)
```

Remember that you can only make 120 API calls per minute per key.

Multi-Key Instance
------------------

If you want your api calls to be able to use more than one key (i.e. if you need more than 120 calls per minute), initialize your API with this instead, then use as normal.
```
api = pypixel.MultiKeyAPI([key1, key2, ... keyn])
```

</div>
