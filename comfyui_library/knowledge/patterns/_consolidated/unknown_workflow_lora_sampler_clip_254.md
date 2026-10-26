---
name: unknown_workflow_lora_sampler_clip_254
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8275
common_nodes: [BlockifyMask, CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, ConditioningZeroOut, DrawMaskOnImage, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GetNode, ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewImage, RandomNoise, ReferenceLatent, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SaveImage, SetNode, ToBinaryMask, UNETLoader, VAEDecode, VAEEncode, VAELoader, YOLOModelLoader]
problems: []
missing: []
members: [图片生成/图生图/Klein-9B-最强二创_多人角色替换-新版_2027838925250764801.json, 图片生成/图生图/Klein-9B-最强二创_多角色替换-（一次替换2个，支持动漫&真人）_2040771742951542785.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_254

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Klein-9B-最强二创_多人角色替换-新版_2027838925250764801.json、图片生成/图生图/Klein-9B-最强二创_多角色替换-（一次替换2个，支持动漫&真人）_2040771742951542785.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ToBinaryMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `ClothesSegment` —— 1/2 个有
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `easy ifElse` —— 1/2 个有
- `easy isMaskEmpty` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
