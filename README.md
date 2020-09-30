# picam_getting_started

Just trying to take images and record videos with the PI camera, this is part of development of [this api](https://github.com/Lindelanimcebo/picam_iot)

## Using the terminal

To take an image and video using the terminal tthe follwing commands were used respectively.
```Bash
raspistill -o ./images/first.jpg
```
```Bash
raspivid -o ./videos/first.h264
```
Note that the video plays better with vlc

## Using Python
The python script under the [src](https://github.com/Lindelanimcebo/picam_getting_started/tree/master/src) directory uses the python PiCamera library to take still pictures and record videos
