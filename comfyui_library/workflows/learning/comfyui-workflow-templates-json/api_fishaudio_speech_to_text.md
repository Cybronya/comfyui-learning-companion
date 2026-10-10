---
key: comfyui-workflow-templates-json/api_fishaudio_speech_to_text.json
name: api_fishaudio_speech_to_text
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_fishaudio_speech_to_text.json
hash: be9822d2bec1da91
official: true
coverage: 0.8
learned_at: 2026-10-10 22:43:48
nodes: [LoadAudio, FishAudioSpeechToText, SaveText, SaveText, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_fishaudio_speech_to_text.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_fishaudio_speech_to_text.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `LoadAudio`
- `FishAudioSpeechToText`
- `SaveText`
- `SaveText`
- `MarkdownNote`

## 知识

覆盖率 **80%**（4/5）

**有卡**：`LoadAudio`、`FishAudioSpeechToText`、`SaveText`

**用到的条目**：SaveText、LoadAudio、FishAudioSpeechToText、sd15-t2i-basic、sd15-t2i-lora、Text、SaveImage、CS_Preview_Any
