---
name: unknown_workflow_upscale_sampler_clip_48
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9115
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/老孙AI 产品精修V3_2090318488920477697.json, 视频生成/图生视频/Flux2_klein_图生图+高清放大_2072586147523551233.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/老孙AI 产品精修V3_2090318488920477697.json、视频生成/图生视频/Flux2_klein_图生图+高清放大_2072586147523551233.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `DF_Integer` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
