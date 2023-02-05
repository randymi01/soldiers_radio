import os

def convert_to_mono(file_name: str) -> None:
    os.system("ffmpeg -i music/{} -ac 1 mono/{}".format(file_name,file_name))

music_files = [i for i in list(os.listdir("music")) if i.split('.')[-1] == 'ogg']

error_files = []

for file in music_files:
    try:
        convert_to_mono(file)
    except:
        error_files.append(file)
        pass

print(error_files)

# get number of audio channels
# ffprobe -show_entries stream=channels -of compact=p=0:nk=1 -v 0 <file>