---
name: unknown_workflow_lora_sampler_clip_100
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8562
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text Concatenate, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageResizeKJv2, ImageScaleToTotalPixels, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/KINGHERE-klein摄影溶图+KLEIN高清放大V4_2040852851857035265.json, 图片生成/图生图/Klein高清重绘放大_2032838566539169794.json, 图片生成/图生图/▶F2K-高清重绘_2046072734924414977.json, 图片生成/图生图/▶Flux2_Klein-换脸高一致性编辑流+KV加速流_2060565541210910722.json, 图片生成/图生图/▶Flux2_Klein-高清重绘+高一致性编辑流+KV加速流_2041692902253924353.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_100

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/KINGHERE-klein摄影溶图+KLEIN高清放大V4_2040852851857035265.json、图片生成/图生图/Klein高清重绘放大_2032838566539169794.json、图片生成/图生图/▶F2K-高清重绘_2046072734924414977.json、图片生成/图生图/▶Flux2_Klein-换脸高一致性编辑流+KV加速流_2060565541210910722.json、图片生成/图生图/▶Flux2_Klein-高清重绘+高一致性编辑流+KV加速流_2041692902253924353.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text Concatenate`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 2/5 个有
- `Florence2Run` —— 2/5 个有
- `FluxKVCache` —— 2/5 个有
- `WD14Tagger|pysssss` —— 2/5 个有
- `BiRefNetRMBG` —— 1/5 个有
- `ConstrainImage|pysssss` —— 1/5 个有
- `Crop (mtb)` —— 1/5 个有
- `DetailTransfer` —— 1/5 个有
- `GetImageSize+` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerMask: MaskGrow` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
