---
name: unknown_workflow_lora_unet_vae_11
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.837
common_nodes: [CLIPLoader, CreateVideo, GetImageSize, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorFaceRefine, MiniMaxH3DirectorSelfLift, ModelAttentionBackend, PlaySound|pysssss, PreviewAny, SaveImage, SaveVideo, UNETLoader, VAELoader, easy imageChooser, kkVideoFirstLastFrames]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json, 视频生成/图生视频/MiniMax+H3+SelfLift导演台全能工作流直出1080P_2102745336082165762.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json、视频生成/图生视频/MiniMax+H3+SelfLift导演台全能工作流直出1080P_2102745336082165762.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `GetImageSize`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorFaceRefine`
- `MiniMaxH3DirectorSelfLift`
- `ModelAttentionBackend`
- `PlaySound|pysssss`
- `PreviewAny`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `easy imageChooser`
- `kkVideoFirstLastFrames`

**可变部分**（部分 workflow 才有）：
- `Astra` —— 1/2 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/2 个有
- `RH_Upscale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
