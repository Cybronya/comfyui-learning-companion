---
name: unknown_workflow_lora_unet_vae_13
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.831667
common_nodes: [CLIPLoader, CreateVideo, GetImageSize, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorFaceRefine, MiniMaxH3DirectorSelfLift, ModelAttentionBackend, PlaySound|pysssss, PreviewAny, SaveImage, SaveVideo, UNETLoader, VAELoader, easy imageChooser, kkVideoFirstLastFrames]
problems: []
missing: []
members: [平台全量/MiniMax+H3+SelfLift导演台全能工作流直出1080P_2118334849953128450.json, 视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json, 视频生成/图生视频/MiniMax+H3+SelfLift导演台全能工作流直出1080P_2102745336082165762.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/MiniMax+H3+SelfLift导演台全能工作流直出1080P_2118334849953128450.json、视频生成/图生视频/MiniMax+H3+SelfLift导演台+RH Upscale_2104255482696388609.json、视频生成/图生视频/MiniMax+H3+SelfLift导演台全能工作流直出1080P_2102745336082165762.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
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
- `Astra` —— 1/3 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/3 个有
- `RH_Upscale` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
