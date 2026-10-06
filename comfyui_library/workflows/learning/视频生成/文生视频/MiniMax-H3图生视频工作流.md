---
key: 视频生成/文生视频/MiniMax-H3图生视频工作流.json
name: MiniMax-H3图生视频工作流
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax-H3图生视频工作流.json
hash: 66048a8cddae14b0
coverage: 0.545455
learned_at: 2026-10-07 00:35:48
nodes: [MiniMaxH3IntegrationAdapterGH, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3DualClockT8GH, BasicGuider, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8GH, SaveAudioAdvanced, VHS_VideoCombine, MiniMaxH3IntegrationGH]
patterns: []
missing: [MiniMaxH3DualClockT8GH, MiniMaxH3IntegrationAdapterGH, MiniMaxH3IntegrationGH, MiniMaxH3AVDecodeT8GH, SaveAudioAdvanced]
discoveries: [次要节点 `MiniMaxH3DualClockT8GH` 知识库中没有该节点类型的任何知识, 次要节点 `MiniMaxH3IntegrationAdapterGH` 知识库中没有该节点类型的任何知识, 次要节点 `MiniMaxH3IntegrationGH` 知识库中没有该节点类型的任何知识, 次要节点 `MiniMaxH3AVDecodeT8GH` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `SaveAudioAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/MiniMax-H3图生视频工作流.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax-H3图生视频工作流.json`

## 结构

**生成流程**：Model → Sampling → Other

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

覆盖率 **55%**（6/11）

**有卡**：`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`VHS_VideoCombine`

**缺卡**（5）：`MiniMaxH3DualClockT8GH`、`MiniMaxH3IntegrationAdapterGH`、`MiniMaxH3IntegrationGH`、`MiniMaxH3AVDecodeT8GH`、`SaveAudioAdvanced`

**用到的条目**：UNETLoader、SamplerCustomAdvanced、BasicGuider、MiniMaxH3MemoryEfficientSageAttentionPatch、RandomNoise、VHS_VideoCombine、sd15-t2i-basic、sd15-t2i-lora

## 学习发现

- 次要节点 `MiniMaxH3DualClockT8GH` 知识库中没有该节点类型的任何知识
- 次要节点 `MiniMaxH3IntegrationAdapterGH` 知识库中没有该节点类型的任何知识
- 次要节点 `MiniMaxH3IntegrationGH` 知识库中没有该节点类型的任何知识
- 次要节点 `MiniMaxH3AVDecodeT8GH` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SaveAudioAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
