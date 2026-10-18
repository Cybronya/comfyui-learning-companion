---
key: 视频生成/图生视频/RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2105583664313749506.json
name: RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2105583664313749506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2105583664313749506.json
hash: 190c238aeec7edfb
coverage: 0.9
learned_at: 2026-10-17 22:18:57
nodes: [ModelPreviewOverrideKJ, easy modelLoaderPack, Note, Note, ModelAttentionBackend, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, easy multitrackProject, ManualSigmas, KSamplerSelect, KSamplerSelect, BasicScheduler, VAELoader, UNETLoader, CLIPLoader, easy multitrackProjectVideoCombine, SaveVideo, easy saveVideo, easy multiTrackEditor]
patterns: []
missing: []
---

# 视频生成/图生视频/RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2105583664313749506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/RH-MINIMAX+H3+Motion+Context_长视频生成工作流V2_2105583664313749506.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（20 个）：
- `ModelPreviewOverrideKJ`
- `easy modelLoaderPack`
- `Note`
- `Note`
- `ModelAttentionBackend`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `easy multitrackProject`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy multitrackProjectVideoCombine`
- `SaveVideo`
- `easy saveVideo`
- `easy multiTrackEditor`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`ModelPreviewOverrideKJ`、`easy modelLoaderPack`、`ModelAttentionBackend`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`easy multitrackProject`、`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`UNETLoader`、`CLIPLoader`、`easy multitrackProjectVideoCombine`、`SaveVideo`、`easy saveVideo`、`easy multiTrackEditor`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、ModelPreviewOverrideKJ、SaveVideo、easy saveVideo
