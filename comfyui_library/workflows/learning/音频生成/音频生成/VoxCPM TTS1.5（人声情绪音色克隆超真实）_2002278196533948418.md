---
key: 音频生成/音频生成/VoxCPM TTS1.5（人声情绪音色克隆超真实）_2002278196533948418.json
name: VoxCPM TTS1.5（人声情绪音色克隆超真实）_2002278196533948418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/VoxCPM TTS1.5（人声情绪音色克隆超真实）_2002278196533948418.json
hash: b4300d029833d5eb
coverage: 0.857143
learned_at: 2026-10-18 01:46:54
nodes: [AudioSeparation, SoundFlow_TrimAudio, Apply Whisper, SaveAudio, VoxCPM_TTS, LoadAudio, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 音频生成/音频生成/VoxCPM TTS1.5（人声情绪音色克隆超真实）_2002278196533948418.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/VoxCPM TTS1.5（人声情绪音色克隆超真实）_2002278196533948418.json`

## 结构

**生成流程**：Output → Other

**节点**（7 个）：
- `AudioSeparation`
- `SoundFlow_TrimAudio`
- `Apply Whisper`
- `SaveAudio`
- `VoxCPM_TTS`
- `LoadAudio`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **86%**（6/7）

**有卡**：`AudioSeparation`、`SoundFlow_TrimAudio`、`Apply Whisper`、`SaveAudio`、`VoxCPM_TTS`、`LoadAudio`

**用到的条目**：SaveAudio、LoadAudio、AudioSeparation、SoundFlow_TrimAudio、VoxCPM_TTS、Apply Whisper、sd15-t2i-basic、sd15-t2i-lora
