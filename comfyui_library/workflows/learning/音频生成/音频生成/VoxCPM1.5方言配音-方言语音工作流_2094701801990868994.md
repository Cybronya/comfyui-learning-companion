---
key: 音频生成/音频生成/VoxCPM1.5方言配音-方言语音工作流_2094701801990868994.json
name: VoxCPM1.5方言配音-方言语音工作流_2094701801990868994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/VoxCPM1.5方言配音-方言语音工作流_2094701801990868994.json
hash: 21e14a1894d2353e
coverage: 0.6
learned_at: 2026-10-18 17:45:45
nodes: [PrimitiveStringMultiline, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_Generate, PrimitiveStringMultiline, SaveAudioMP3]
patterns: []
missing: []
---

# 音频生成/音频生成/VoxCPM1.5方言配音-方言语音工作流_2094701801990868994.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/VoxCPM1.5方言配音-方言语音工作流_2094701801990868994.json`

## 结构

**生成流程**：Output → Other

**节点**（5 个）：
- `PrimitiveStringMultiline`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_Generate`
- `PrimitiveStringMultiline`
- `SaveAudioMP3`

## 知识

覆盖率 **60%**（3/5）

**有卡**：`RunningHub_VoxCPM_LoadModel`、`RunningHub_VoxCPM_Generate`、`SaveAudioMP3`

**用到的条目**：SaveAudioMP3、RunningHub_VoxCPM_LoadModel、RunningHub_VoxCPM_Generate、sd15-t2i-basic、sd15-t2i-lora、SaveAudio、String、VoxCPM_Generate
