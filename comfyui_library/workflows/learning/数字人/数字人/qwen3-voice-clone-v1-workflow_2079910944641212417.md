---
key: 数字人/数字人/qwen3-voice-clone-v1-workflow_2079910944641212417.json
name: qwen3-voice-clone-v1-workflow_2079910944641212417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/qwen3-voice-clone-v1-workflow_2079910944641212417.json
hash: 72cdda7d7d9d4639
coverage: 0.857143
learned_at: 2026-10-18 19:07:48
nodes: [AudioCrop, ShowText|pysssss, Qwen3TTSModelLoader, LoadAudio, Apply Whisper, Qwen3TTSVoiceClone, SaveAudio]
patterns: []
missing: []
---

# 数字人/数字人/qwen3-voice-clone-v1-workflow_2079910944641212417.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/qwen3-voice-clone-v1-workflow_2079910944641212417.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（7 个）：
- `AudioCrop`
- `ShowText|pysssss`
- `Qwen3TTSModelLoader`
- `LoadAudio`
- `Apply Whisper`
- `Qwen3TTSVoiceClone`
- `SaveAudio`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`AudioCrop`、`Qwen3TTSModelLoader`、`LoadAudio`、`Apply Whisper`、`Qwen3TTSVoiceClone`、`SaveAudio`

**用到的条目**：SaveAudio、LoadAudio、AudioCrop、Qwen3TTSModelLoader、Qwen3TTSVoiceClone、Apply Whisper、sd15-t2i-basic、sd15-t2i-lora
