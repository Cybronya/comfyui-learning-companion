---
key: comfyui-workflow-templates-json/api_elevenlabs_speech_to_speech.json
name: api_elevenlabs_speech_to_speech
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_elevenlabs_speech_to_speech.json
hash: ab7a20faa80d61b7
official: true
coverage: 0.875
learned_at: 2026-10-07 21:33:32
nodes: [LoadAudio, ElevenLabsInstantVoiceClone, Note, RecordAudio, ElevenLabsVoiceSelector, ElevenLabsSpeechToSpeech, LoadAudio, SaveAudioAdvanced]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_elevenlabs_speech_to_speech.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_elevenlabs_speech_to_speech.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `LoadAudio`
- `ElevenLabsInstantVoiceClone`
- `Note`
- `RecordAudio`
- `ElevenLabsVoiceSelector`
- `ElevenLabsSpeechToSpeech`
- `LoadAudio`
- `SaveAudioAdvanced`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LoadAudio`、`ElevenLabsInstantVoiceClone`、`RecordAudio`、`ElevenLabsVoiceSelector`、`ElevenLabsSpeechToSpeech`、`SaveAudioAdvanced`

**用到的条目**：SaveAudioAdvanced、LoadAudio、ElevenLabsInstantVoiceClone、ElevenLabsSpeechToSpeech、ElevenLabsVoiceSelector、RecordAudio、sd15-t2i-basic、sd15-t2i-lora
