"""
Using this file you can generate the transcribed and translated videos as per choice.
"""

import os
import argparse
import logging
import datetime
from src.utils import execute_task

# Defining some global variables
TRANSCRIBE_AND_TRANSLATE = ['translate', 'transcribe']
LANGUAGE = ['Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Assamese', 'Azerbaijani', 'Bashkir',
            'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Breton', 'Bulgarian', 'Burmese', 'Castilian', 'Catalan',
            'Chinese', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Faroese', 'Finnish',
            'Flemish', 'French', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian', 'Haitian Creole',
            'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Italian', 'Japanese',
            'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Lao', 'Latin', 'Latvian', 'Letzeburgesch', 'Lingala',
            'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori',
            'Marathi', 'Moldavian', 'Moldovan', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian', 'Nynorsk', 'Occitan',
            'Panjabi', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Pushto', 'Romanian', 'Russian',
            'Sanskrit', 'Serbian', 'Shona', 'Sindhi', 'Sinhala', 'Sinhalese', 'Slovak', 'Slovenian', 'Somali',
            'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai',
            'Tibetan', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uzbek', 'Valencian', 'Vietnamese', 'Welsh',
            'Yiddish', 'Yoruba']


# Defining the main function which translates and/or transcribes videos as per the user's choice
def main(
    videos_path: str,
    updated_videos_path: str,
    task: str,
    language: str,
    video_extension: str
) -> None :
    """This function takes the choice of the user and translates and/or transcribes the videos.

    Args:
        videos_path (str): Path where all the videos to transcribe and/or translate are stored 
        updated_videos_path (str): Path where all the transcribed and/or translated videos are stored
        task (str): Translate and/or Transcribe
        language (str): Language for the task
        video_extension (str): Extension of video i.e. .mp4 or .mov or something else
    """
    
    logging.info('Started generating updated videos at - %s ##################', datetime.datetime.now())
    
    execute_task(
        videos_path=videos_path,
        updated_videos_path=updated_videos_path,
        language=language,
        task=task,
        video_extension=video_extension
    )

    logging.info('Completed generating updated videos at - %s ################', datetime.datetime.now())
        

if __name__ == '__main__':
    cmdline_parser = argparse.ArgumentParser('Transcribe and Translate')
    cmdline_parser.add_argument('-vp', '--videos_path',
                                default='./videos',
                                help='Path where all the videos to transcribe and/or translate are stored',
                                type=str)
    cmdline_parser.add_argument('-uvp', '--updated_videos_path',
                                default='./updated_videos',
                                help='Path where all the transcribed and/or translated videos are stored',
                                type=str)
    cmdline_parser.add_argument('-t', '--task',
                                default='none',
                                help='To\n1. Translate choose "translate"\n2. Transcribe choose "transcribe"',
                                choices=TRANSCRIBE_AND_TRANSLATE,
                                type=str)
    cmdline_parser.add_argument('-l', '--language',
                                default='English',
                                help='Language for the task',
                                choices=LANGUAGE,
                                type=str)
    cmdline_parser.add_argument('-ve', '--video_extension',
                                default='.mp4',
                                help='Pass the type of the video i.e. .mp4 or .mov or something else',
                                type=str)
    
    args, unknowns = cmdline_parser.parse_known_args()
    LOG_LVL = logging.INFO
    logging.basicConfig(level=LOG_LVL)

    if unknowns:
        logging.warning('Found unknown arguments!')
        logging.warning(str(unknowns))
        logging.warning('These will be ignored')
    
    # Calling the main method to translate and/or transcribe videos as per the user's choice
    main(
        videos_path=args.videos_path,
        updated_videos_path=args.updated_videos_path,
        task=args.task,
        language=args.language,
        video_extension=args.video_extension
    )