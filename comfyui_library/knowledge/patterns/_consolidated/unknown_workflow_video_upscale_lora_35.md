---
name: unknown_workflow_video_upscale_lora_35
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.844
common_nodes: [BlockSparseAttention, CLIPLoader, GH_AudioVideoMerger, GH_ImageVideoComparer, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorFaceRefine, MiniMaxH3DirectorSelfLift, ModelAttentionBackend, UNETLoader, VAELoader, VHS_VideoCombine, VOSR2ModelLoader, VOSR2Upscale, 忽略多组孤海]
problems: []
missing: []
members: [视频生成/图生视频/导演台合集最终完成版_2106268078148505602.json, 视频生成/图生视频/视频换人复刻丨MiniMax H3 Hybrid丨多段续接·可选超分_2110593335210631169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/导演台合集最终完成版_2106268078148505602.json、视频生成/图生视频/视频换人复刻丨MiniMax H3 Hybrid丨多段续接·可选超分_2110593335210631169.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockSparseAttention`
- `CLIPLoader`
- `GH_AudioVideoMerger`
- `GH_ImageVideoComparer`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorFaceRefine`
- `MiniMaxH3DirectorSelfLift`
- `ModelAttentionBackend`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `LayerFilter: GaussianBlur` —— 1/2 个有
- `图像缩放V2_孤海` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
