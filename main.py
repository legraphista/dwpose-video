from tqdm import tqdm
import numpy as np

from annotator.dwpose import DWposeDetector
from sys import argv
from torchvision.io import read_video, write_video

video_path = argv[1]
pose_path = argv[2]

frames, _a_frames, meta_dict = read_video(video_path, pts_unit='sec')
if len(frames) == 0:
    raise Exception(f'failed to open file {video_path}')
fps = meta_dict['video_fps']

dwpose = DWposeDetector()
output_frames = np.asarray([
    dwpose(np.asarray(frame))
    for frame in tqdm(frames)
])

write_video(pose_path, video_array=output_frames, fps=fps, video_codec='libx264rgb', options={'crf': '0'})
