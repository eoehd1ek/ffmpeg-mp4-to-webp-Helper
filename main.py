import os
from multiprocessing import *


process_size = 4
video_extension = "mp4"
output_extension = "webp"


def execute_command(queue):
    while (not queue.empty()):
        command = queue.get()
        os.system(command)


def is_video_file(path: str) -> bool:
    return path[-len(video_extension):] == video_extension


def get_video_file_list() -> list[str]:
    file_list = os.listdir(os.getcwd())
    video_file_list = list(filter(is_video_file, file_list))
    return video_file_list


def get_result_file_path(path: str) -> str:
    return path[:(len(path) - len(video_extension))] + output_extension


def get_ffmpeg_command(path: str) -> str:
    return f"ffmpeg -i \"{path}\" -vcodec libwebp -lossless 1 -loop 0 -an -vsync 0 \"{get_result_file_path(path)}\""


def main():
    freeze_support()
    command_queue = Queue()
    commands = list(map(get_ffmpeg_command, get_video_file_list()))
    for command in commands:
        command_queue.put(command)

    if (not command_queue.empty()):
        procs = []
        for _ in range(process_size):
            p = Process(target=execute_command, args=(command_queue,))
            procs.append(p)
            p.start()
        for proc in procs:
            proc.join()
        print("모든 프로세스가 join 되었습니다.(작업이 완료되었습니다.)")
    else:
        print("변경할 mp4 확장자 파일을 찾지 못했습니다.")
    os.system("pause")


if __name__ == "__main__":
    main()
