---
key: 视频生成/文生视频/RH-MINIMAX+H3+Motion+Context 长视频生成工作流V2_2103474631964446722.json
name: RH-MINIMAX+H3+Motion+Context 长视频生成工作流V2_2103474631964446722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/RH-MINIMAX+H3+Motion+Context 长视频生成工作流V2_2103474631964446722.json
hash: 809bdc6b2dee0abc
coverage: 0.65
learned_at: 2026-10-11 22:12:46
nodes: [ModelPreviewOverrideKJ, easy modelLoaderPack, Note, Note, ModelAttentionBackend, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, easy multitrackProject, ManualSigmas, KSamplerSelect, KSamplerSelect, BasicScheduler, easy multiTrackEditor, VAELoader, UNETLoader, CLIPLoader, easy multitrackProjectVideoCombine, SaveVideo, easy saveVideo]
patterns: []
missing: [easy modelLoaderPack, easy multiTrackEditor, easy multitrackProject, easy multitrackProjectVideoCombine, easy saveVideo]
discoveries: [次要节点 `easy modelLoaderPack` 知识库中没有该节点类型的任何知识, 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识, 次要节点 `easy multitrackProject` 知识库中没有该节点类型的任何知识, 次要节点 `easy multitrackProjectVideoCombine` 知识库中没有该节点类型的任何知识, 次要节点 `easy saveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/RH-MINIMAX+H3+Motion+Context 长视频生成工作流V2_2103474631964446722.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/RH-MINIMAX+H3+Motion+Context 长视频生成工作流V2_2103474631964446722.json`

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
- `easy multiTrackEditor`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy multitrackProjectVideoCombine`
- `SaveVideo`
- `easy saveVideo`

## 知识

覆盖率 **65%**（13/20）

**有卡**：`ModelPreviewOverrideKJ`、`ModelAttentionBackend`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ManualSigmas`、`KSamplerSelect`、`BasicScheduler`、`UNETLoader`、`CLIPLoader`、`SaveVideo`

**缺卡**（5）：`easy modelLoaderPack`、`easy multiTrackEditor`、`easy multitrackProject`、`easy multitrackProjectVideoCombine`、`easy saveVideo`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、ModelPreviewOverrideKJ、SaveVideo、BasicScheduler

## 学习发现

- 次要节点 `easy modelLoaderPack` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multiTrackEditor` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multitrackProject` 知识库中没有该节点类型的任何知识
- 次要节点 `easy multitrackProjectVideoCombine` 知识库中没有该节点类型的任何知识
- 次要节点 `easy saveVideo` 仅有 SaveImage 的通用知识，没有该节点自己的说明
