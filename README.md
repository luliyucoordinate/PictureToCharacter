# PictureToCharacter


[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/luliyucoordinate/PictureToCharacter)[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)](https://github.com/luliyucoordinate/PictureToCharacter)

Make picture  transformed into a character painting

<center class="half">
<img src="http://wx3.sinaimg.cn/mw690/af2d2659gy1foa4e4p1uuj20mp0pagm7.jpg"  width = "300" height = "200">
</center>

#### How to use

please put the picture which you want to transformed in the dir`PictureToCharacter\`

```shell
python PictureToCharacter.py picture.png
```

you can use `--width` and `--height` to adjust the picture size.Example

```shell
python PictureToCharacter.py picture.png --width 20 --height 20
```

 Also,you can get the `.txt` of the character painting use `-o`or`--output`

```shell
python PictureToCharacter.py picture.png --width 20 --height 20 --output picture.txt
```

