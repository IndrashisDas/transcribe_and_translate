"""_summary_
"""

import os
import logging
import warnings
import cv2
from typing import List
from mlxtend.file_io import find_files
warnings.filterwarnings('ignore')


def seek_files(
    videos_path: str,
    video_extension: str
) -> List:
    """This function looks for all the files with a specific video extension in a folder where these videos are stored.

    Args:
        videos_path (str): Path where all the videos to transcribe and/or translate are stored
        video_extension (str): Extension of video i.e. .mp4 or .mov or something else

    Returns:
        List: Of all such files with a specific video extension in a folder
    """
    return find_files(substring=video_extension, path=videos_path, recursive=True)


def execute_task(
    videos_path: str,
    updated_videos_path: str,
    language: str,
    task: str,
    video_extension: str
) -> None:
    
    # Find all the files with a specific extension
    all_files = seek_files(videos_path=videos_path, video_extension=video_extension)
    logging.info('Found %d video file(s) in the folder %s', len(all_files), videos_path)
    
    # Create the following directories if they don't exist
    audio_outdir = updated_videos_path + f'\\audio_files\\{task}\\{language}'
    subtitle_outdir = updated_videos_path + f'\\subtitle_files\\{task}\\{language}'
    updated_videos_path = updated_videos_path +f'\\{task}\\{language}'
    for dir in [audio_outdir, subtitle_outdir, updated_videos_path]:
        if not os.path.exists(dir):
            os.makedirs(dir)
    
    for file in all_files:
        file = file.replace('/', '\\')
        logging.info('Executing Task for video %s', file)
        file_name = (file.split('\\')[-1]).split('.')[0]
        audio_file_path = os.path.join(audio_outdir, file_name + '.mp3')
        subtitle_file_path = os.path.join(subtitle_outdir, file_name)
        video_file_path = os.path.join(updated_videos_path, file_name + video_extension)
        
        # Extract the audio from the video
        if not os.path.isfile(audio_file_path):
            audio_query = f"ffmpeg -i {file} -vn -acodec mp3 {audio_file_path} -hide_banner -loglevel error"
            os.system(audio_query)
            logging.info('Audio generated for %s', file)
        
        # Generate the subtitles from the audio
        if not os.path.isfile(subtitle_file_path):
            subtitle_query = f"whisper {audio_file_path} --model medium --language {language} --output_dir \
                {subtitle_file_path} --verbose False --task {task}"
            os.system(subtitle_query)
            logging.info('Subtitles generated for %s', file)
        
        # Generate the close-captioned video
        cap = cv2.VideoCapture(file)
        if not cap.isOpened():
            print("Error: Could not open video.")
            exit()
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        bar_height = int(170 * width / 1920)
        subtitle_file_path = os.path.join(subtitle_file_path, file_name + '.mp3.srt')
        subtitle_file_path = subtitle_file_path.replace('\\', '/')
        video_file_path = video_file_path.replace('\\', '/')
        ccm_query = f'ffmpeg -i {file} -c:v libx264 -preset fast -crf 23 -c:a mp3 -b:a 128k -vf \
                "pad=iw:ih+{bar_height}:0:0:black,subtitles={subtitle_file_path}:force_style=' + "'" + 'Fontsize=12' + \
                "'" + f'" -scodec srt {video_file_path}'
        os.system(ccm_query)
        
        
        
        
        
        
        
        

