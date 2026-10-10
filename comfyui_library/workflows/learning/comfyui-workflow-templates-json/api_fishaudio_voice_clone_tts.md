---
key: comfyui-workflow-templates-json/api_fishaudio_voice_clone_tts.json
name: api_fishaudio_voice_clone_tts
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_fishaudio_voice_clone_tts.json
hash: 17a43918a67cd701
official: true
coverage: 0.857143
learned_at: 2026-10-10 22:43:50
nodes: [FishAudioTextToSpeech, SaveAudioAdvanced, FishAudioVoiceSelector, MarkdownNote, FishAudioInstantVoiceClone, LoadAudio, RecordAudio]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_fishaudio_voice_clone_tts.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_fishaudio_voice_clone_tts.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `FishAudioTextToSpeech`
- `SaveAudioAdvanced`
- `FishAudioVoiceSelector`
- `MarkdownNote`
- `FishAudioInstantVoiceClone`
- `LoadAudio`
- `RecordAudio`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`FishAudioTextToSpeech`、`SaveAudioAdvanced`、`FishAudioVoiceSelector`、`FishAudioInstantVoiceClone`、`LoadAudio`、`RecordAudio`

**用到的条目**：SaveAudioAdvanced、LoadAudio、FishAudioInstantVoiceClone、FishAudioTextToSpeech、FishAudioVoiceSelector、RecordAudio、sd15-t2i-basic、sd15-t2i-lora
