---
name: unknown_workflow_sampler_clip_unet_435
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.879
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageResize+, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1_2023028109125099521.json, 图片生成/文生图/klein多图编辑_2017934301005877250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_435

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1_2023028109125099521.json、图片生成/文生图/klein多图编辑_2017934301005877250.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageResize+`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `QwenMultiangleCameraNode` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RH_Nano_Banana2_Image2Image` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
