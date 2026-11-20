---
name: unknown_workflow_video_lora_unet_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8285
common_nodes: [CLIPLoader, LoraLoaderBypassModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 AIMixer DSW导演台_2094439901352775681.json, 视频生成/图生视频/MiniMax-H3导演台文生图生首尾帧多参多合一视频制作_2091539822958702594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_unet_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 AIMixer DSW导演台_2094439901352775681.json、视频生成/图生视频/MiniMax-H3导演台文生图生首尾帧多参多合一视频制作_2091539822958702594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ManualSigmas` —— 1/2 个有
- `MiniMaxH3DirectorRefine` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
