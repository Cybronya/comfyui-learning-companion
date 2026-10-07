---
key: comfyui-workflow-templates-json/api_fishaudio_text_to_speech.json
name: api_fishaudio_text_to_speech
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_fishaudio_text_to_speech.json
hash: 6bbe2ec189e3b007
official: true
coverage: 0.833333
learned_at: 2026-10-07 21:33:36
nodes: [FishAudioTextToSpeech, SaveAudioAdvanced, FishAudioVoiceSelector, MarkdownNote, FishAudioInstantVoiceClone, LoadAudio]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_fishaudio_text_to_speech.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_fishaudio_text_to_speech.json`

## 结构

**生成流程**：Output → Other

**节点**（6 个）：
- `FishAudioTextToSpeech`
- `SaveAudioAdvanced`
- `FishAudioVoiceSelector`
- `MarkdownNote`
- `FishAudioInstantVoiceClone`
- `LoadAudio`

## 知识

覆盖率 **83%**（5/6）

**有卡**：`FishAudioTextToSpeech`、`SaveAudioAdvanced`、`FishAudioVoiceSelector`、`FishAudioInstantVoiceClone`、`LoadAudio`

**用到的条目**：SaveAudioAdvanced、LoadAudio、FishAudioInstantVoiceClone、FishAudioTextToSpeech、FishAudioVoiceSelector、sd15-t2i-basic、sd15-t2i-lora、SaveAudio
