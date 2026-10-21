---
name: unknown_workflow_video_unet_vae_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.947
common_nodes: [CLIPLoader, LoadImage, MiniMaxH3Director, MiniMaxH3DirectorGroupsCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/Minimax-H3 导演台 多帧素材组图生视频（加速版）_2087218383308812289.json, 视频生成/文生视频/Minimax-H3 导演台 多模态素材组生视频（加速版）_2087413389864820738.json]
source: knowledge_consolidation
---

# unknown_workflow_video_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3 导演台 多帧素材组图生视频（加速版）_2087218383308812289.json、视频生成/文生视频/Minimax-H3 导演台 多模态素材组生视频（加速版）_2087413389864820738.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `LoadImage`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorGroupsCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DirectorGroupImageToVideo` —— 1/2 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
