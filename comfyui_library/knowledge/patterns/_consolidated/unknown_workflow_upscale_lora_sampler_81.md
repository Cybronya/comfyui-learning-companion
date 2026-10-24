---
name: unknown_workflow_upscale_lora_sampler_81
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.878
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageColorMatch]
problems: []
missing: []
members: [图片生成/图生图/Flux2+seedvr2高清放大_2043915810573389825.json, 图片生成/图生图/flux2klein 4K高清放大_2041033443819130881.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux2+seedvr2高清放大_2043915810573389825.json、图片生成/图生图/flux2klein 4K高清放大_2041033443819130881.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
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
- `easy cleanGpuUsed`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `CR Set Value On Boolean` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Float` —— 1/2 个有
- `ImageBlur` —— 1/2 个有
- `ImageSmartSharpen+` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy int` —— 1/2 个有
- `easy mathInt` —— 1/2 个有
- `easy setNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
