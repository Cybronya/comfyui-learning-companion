---
key: comfyui-workflow-templates-json/api_elevenlabs_text_to_dialogue.json
name: api_elevenlabs_text_to_dialogue
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/api_elevenlabs_text_to_dialogue.json
hash: 2dcd1575dc4ac442
official: true
coverage: 0.777778
learned_at: 2026-10-07 21:33:33
nodes: [LoadAudio, ElevenLabsInstantVoiceClone, Note, ElevenLabsVoiceSelector, ElevenLabsVoiceSelector, ElevenLabsTextToDialogue, RecordAudio, SaveAudioAdvanced, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/api_elevenlabs_text_to_dialogue.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/api_elevenlabs_text_to_dialogue.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `LoadAudio`
- `ElevenLabsInstantVoiceClone`
- `Note`
- `ElevenLabsVoiceSelector`
- `ElevenLabsVoiceSelector`
- `ElevenLabsTextToDialogue`
- `RecordAudio`
- `SaveAudioAdvanced`
- `MarkdownNote`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`LoadAudio`、`ElevenLabsInstantVoiceClone`、`ElevenLabsVoiceSelector`、`ElevenLabsTextToDialogue`、`RecordAudio`、`SaveAudioAdvanced`

**用到的条目**：SaveAudioAdvanced、LoadAudio、ElevenLabsInstantVoiceClone、ElevenLabsTextToDialogue、ElevenLabsVoiceSelector、RecordAudio、sd15-t2i-basic、sd15-t2i-lora
