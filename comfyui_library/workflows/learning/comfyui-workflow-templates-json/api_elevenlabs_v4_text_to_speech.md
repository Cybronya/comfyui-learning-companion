---
key: comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_speech.json
name: api_elevenlabs_v4_text_to_speech
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_speech.json
hash: b806c47b19ca3116
official: true
coverage: 0.75
learned_at: 2026-10-07 21:33:35
nodes: [ElevenLabsTextToSpeech, LoadAudio, ElevenLabsVoiceSelector, ElevenLabsInstantVoiceClone, RecordAudio, Note, SaveAudioAdvanced, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_speech.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_elevenlabs_v4_text_to_speech.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `ElevenLabsTextToSpeech`
- `LoadAudio`
- `ElevenLabsVoiceSelector`
- `ElevenLabsInstantVoiceClone`
- `RecordAudio`
- `Note`
- `SaveAudioAdvanced`
- `MarkdownNote`

## 知识

覆盖率 **75%**（6/8）

**有卡**：`ElevenLabsTextToSpeech`、`LoadAudio`、`ElevenLabsVoiceSelector`、`ElevenLabsInstantVoiceClone`、`RecordAudio`、`SaveAudioAdvanced`

**用到的条目**：SaveAudioAdvanced、LoadAudio、ElevenLabsInstantVoiceClone、ElevenLabsTextToSpeech、ElevenLabsVoiceSelector、RecordAudio、sd15-t2i-basic、sd15-t2i-lora
