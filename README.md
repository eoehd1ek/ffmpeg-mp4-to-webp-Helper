# ffmpeg-mp4-to-webp-helper
mp4파일을 webp파일로 변환하는 ffmpeg명령어를 실행하는 프로그램  
mp4파일을 webp 움짤로 만들 수 있습니다.

# 사용법
1. 프로그램과 같은 폴더에 'ffmpeg.exe' 파일을 둔다.
2. 프로그램과 같은 폴더에 변환할 mp4 파일들 둔다.
3. 이 프로그램을 실행시킨다.

# 실제 실행되는 명령어
```shell
ffmpeg -i "filename.mp4" -vcodec libwebp -lossless 1 -loop 0 -an -vsync 0 "file_name.webp"
```