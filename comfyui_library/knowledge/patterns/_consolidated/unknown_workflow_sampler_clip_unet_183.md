---
name: unknown_workflow_sampler_clip_unet_183
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.954333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/1_2023028109125099521.json, 图片生成/文生图/Klein 9B单、双、多图编辑_2018506313860386818.json, 视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1_2023028109125099521.json、图片生成/文生图/Klein 9B单、双、多图编辑_2018506313860386818.json、视频生成/图生视频/换脸Flux2Klein多图编辑9B加速版Flux2Klein多图编辑9B加速版+_2102351446854426626.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
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
- `ImageResize+` —— 2/3 个有
- `Int` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `RH_Nano_Banana2_Image2Image` —— 1/3 个有
- `StringFunction|pysssss` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
