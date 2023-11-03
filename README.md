# transcribe_and_translate

OpenAI's Automatic Speech Recognition model Whisper was launched on September 21, 2022 and since then it has become 
very easy to transcribe and translate audio/video files. To know more you can refer to the webpage 
[here](url:https://openai.com/research/whisper). Also, the amazing part is that it can not only handle English but also 
do the above-mentioned tasks in multiple other languages.

This repository provides you with a structured script that makes it even more easier to execute these tasks. Now, 
instead of writing all the code by yourself, you can just clone this repository and run the designated Python scripts 
to achieve your goal. Below, you can find detailed instructions to work with this repository.

## Installation

Follow the provided instructions to successfully install the dependencies for this repository to function.

1. You can work with any IDE like PyCharm or VSCode. My personal preference would be VSCode.
2. Create a virtual environment and set that as the interpreter for this project in your local machine. Also, make 
sure that it is active in your IDE's terminal.
3. Run ```pip install -r requirements.txt``` in your terminal. This installs all the required python libraries 
to run this repository.
4. Install FFMPEG as follows,
    - Windows - Follow this [link](https://www.wikihow.com/Install-FFmpeg-on-Windows)
    - macOS - ```brew install ffmpeg```
    - Linux - ```sudo apt-get install ffmpeg```

## Using this repository

You can simply follow the commands provided below to translate/transcribe a video. All these commands are to be run from
 the root folder of this repository. 

1. To Transcribe a video - 
    - Run ```python -m src.generate_updated_videos -vp "./videos" -uvp "./updated_videos" -t "transcribe" -l "German" -ve "mp4"``` 
    - You can provide the path where the videos are located in ```-vp```
    - You can provide the path where you want to store the close-captioned videos under ```-uvp```
    - Choose the task as ```"transcribe"``` in ```-t```
    - Choose the language that exist's in the video under ```-l```
    - Choose the video extension of the video you want to update under ```-ve``` 

2. To Translate a video - 
    - Run ```python -m src.generate_updated_videos -vp "./videos" -uvp "./updated_videos" -t "trasnlate" -l "English" -ve ".mp4"``` 
    - You can provide the path where the videos are located in ```-vp```
    - You can provide the path where you want to store the close-captioned videos under ```-uvp```
    - Choose the task as ```"translate"``` in ```-t```
    - Choose the language to translate to under ```-l```
    - Choose the video extension of the video you want to update under ```-ve```

3. Finally, the provided scripts also merge the closed-captions with the input video such that you can now have them 
embedded in the video. So feel free and generate your own close-captioned videos.