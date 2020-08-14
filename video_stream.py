import sys, os, json
sys.path.append('../')

from webapp import flask_video_stream

if __name__ == '__main__':
   flask_video_stream.run(host='0.0.0.0', port=5002)
