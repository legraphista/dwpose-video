# DWPose video
_simple implementation for video to animated DWPose_

## Install

```bash
pip -r requirements.txt
```

## Models
You should be able to find the models [here](https://github.com/IDEA-Research/DWPose/tree/onnx#-dwpose-for-controlnet) in the controlnet section

## Usage

```bash
python main.py INPUT.mp4 POSE.mp4
```
Output is h264 RGB variant (is not be playable by all video players, preview with VLC or ffplay)

## License
Apache License 2.0 

## Disclaimer
This is a simple script to convert videos. It's not optimized and does not stream frames, so make sure you have enough RAM to keep all your video frames in memory (twice)
