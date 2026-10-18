---
key: 音频生成/音频生成/VoxCPM TTS1.5（荒哥内门弟子专用）_2000084223291686913.json
name: VoxCPM TTS1.5（荒哥内门弟子专用）_2000084223291686913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/VoxCPM TTS1.5（荒哥内门弟子专用）_2000084223291686913.json
hash: cb26ccab95e8f7f5
coverage: 0.75
learned_at: 2026-10-18 01:46:55
nodes: [ShowText|pysssss, Apply Whisper, SoundFlow_TrimAudio, AudioSeparation, SaveAudio, PrimitiveStringMultiline, LoadAudio, VoxCPM_TTS]
patterns: []
missing: []
---

# 音频生成/音频生成/VoxCPM TTS1.5（荒哥内门弟子专用）_2000084223291686913.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/VoxCPM TTS1.5（荒哥内门弟子专用）_2000084223291686913.json`

## 结构

**生成流程**：Output → Other

**节点**（8 个）：
- `ShowText|pysssss`
- `Apply Whisper`
- `SoundFlow_TrimAudio`
- `AudioSeparation`
- `SaveAudio`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `VoxCPM_TTS`

## 知识

覆盖率 **75%**（6/8）

**有卡**：`Apply Whisper`、`SoundFlow_TrimAudio`、`AudioSeparation`、`SaveAudio`、`LoadAudio`、`VoxCPM_TTS`

**用到的条目**：SaveAudio、LoadAudio、AudioSeparation、SoundFlow_TrimAudio、VoxCPM_TTS、Apply Whisper、sd15-t2i-basic、sd15-t2i-lora
