---
key: 视频生成/文生视频/MiniMax-H3图生视频工作流.json
name: MiniMax-H3图生视频工作流
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3图生视频工作流.json
hash: 66048a8cddae14b0
coverage: 1
learned_at: 2026-10-10 23:03:49
nodes: [MiniMaxH3IntegrationAdapterGH, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3DualClockT8GH, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8GH, SaveAudioAdvanced, VHS_VideoCombine, MiniMaxH3IntegrationGH]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax-H3图生视频工作流.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3图生视频工作流.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（11 个）：
- `MiniMaxH3IntegrationAdapterGH`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3DualClockT8GH`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8GH`
- `SaveAudioAdvanced`
- `VHS_VideoCombine`
- `MiniMaxH3IntegrationGH`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`MiniMaxH3IntegrationAdapterGH`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3DualClockT8GH`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8GH`、`SaveAudioAdvanced`、`VHS_VideoCombine`、`MiniMaxH3IntegrationGH`

**用到的条目**：UNETLoader、SamplerCustomAdvanced、MiniMaxH3AVDecodeT8GH、SaveAudioAdvanced、BasicGuider、MiniMaxH3MemoryEfficientSageAttentionPatch、RandomNoise、VHS_VideoCombine
