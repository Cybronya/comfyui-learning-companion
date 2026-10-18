---
key: 音频生成/音频生成/VoxCPM2语音极限克隆V1  企财盈6.17_2067072588702113793.json
name: VoxCPM2语音极限克隆V1  企财盈6.17_2067072588702113793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/VoxCPM2语音极限克隆V1  企财盈6.17_2067072588702113793.json
hash: 49d2c85e51329f36
coverage: 1
learned_at: 2026-10-18 03:04:57
nodes: [Qwen3ASRLoader, Qwen3ASRTranscribe, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_Generate, LoadAudio, SaveAudio, CR Prompt Text]
patterns: []
missing: []
---

# 音频生成/音频生成/VoxCPM2语音极限克隆V1  企财盈6.17_2067072588702113793.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/VoxCPM2语音极限克隆V1  企财盈6.17_2067072588702113793.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（7 个）：
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_Generate`
- `LoadAudio`
- `SaveAudio`
- `CR Prompt Text`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`RunningHub_VoxCPM_LoadModel`、`RunningHub_VoxCPM_Generate`、`LoadAudio`、`SaveAudio`、`CR Prompt Text`

**用到的条目**：CR Prompt Text、SaveAudio、LoadAudio、Qwen3ASRLoader、Qwen3ASRTranscribe、RunningHub_VoxCPM_LoadModel、RunningHub_VoxCPM_Generate、sd15-t2i-basic
