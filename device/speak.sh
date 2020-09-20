#!/bin/bash
tts(){
  python ~/python-docs-samples/texttospeech/cloud-client/synthesize_file.py --text $*
}
tts $*
