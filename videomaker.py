import pyttsx3
import os


def driver(body):
    with open(f"scraped blogs/{body}", 'r', encoding='utf-8') as fp:
        body = fp.readlines()
    body = ' '.join([str(char) for char in body])
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 300)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.save_to_file(body, "template/Voiceover.mp3")
    engine.runAndWait()
    cwd = os.getcwd()
    cmd = f"ffmpeg -stream_loop -1 -i {cwd}\Template\preview.mp4 -i {cwd}\Template\Voiceover.mp3 -shortest -map 0:v:0 -map 1:a:0 -y {cwd}\Template\output.mp4"
    print(cmd)


if __name__ == "__main__":
    dir_path = f'{os.getcwd()}\scraped blogs'
    res = []
    for i, path in enumerate(os.listdir(dir_path)):
        if os.path.isfile(os.path.join(dir_path, path)):
            print(f"{i+1}. {path}")
            res.append(path)
    choice = int(input("Select The blog : "))
    driver(res[choice-1])
