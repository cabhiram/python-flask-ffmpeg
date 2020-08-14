import ffmpeg_streaming


from ffmpeg_streaming import Formats

video = ffmpeg_streaming.input('file_example_MP4_480_1_5MG.mp4')


hls = video.hls(Formats.h264())
hls.auto_generate_representations()
hls.output('../../static/videos/hls/hls.m3u8')
