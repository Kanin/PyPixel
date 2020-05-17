PyPixel
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
=======

A Python Wrapper for The Hypixel API (https://api.hypixel.net). By @TheDestruc7i0n and @WireSegal



Installation
============

Download the zip here: https://github.com/destruc7i0n/PyPixel/archive/master.zip

If you're using Mac or Linux:

Download the source zip, and unpack it. From the folder created, run this command: 
```
sudo python setup.py install
```
Enter your password and you're good to go.



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






[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/destruc7i0n/pypixel/trend.png)](https://bitdeli.com/free "Bitdeli Badge")


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://thedestruc7i0n.ca"><img src="https://avatars2.githubusercontent.com/u/6181960?v=4" width="100px;" alt=""/><br /><sub><b>destruc7i0n</b></sub></a><br /><a href="https://github.com/CodingKanin/PyPixel/commits?author=destruc7i0n" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!