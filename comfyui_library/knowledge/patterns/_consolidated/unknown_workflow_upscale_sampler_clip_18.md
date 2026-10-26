---
name: unknown_workflow_upscale_sampler_clip_18
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.784714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-Klein--产品精修_2054918894313320450.json, 图片生成/图生图/Flux-Klein首饰产品精修 高清放大_2055474345887191041.json, 图片生成/图生图/Flux-Klein首饰产品精修加高清放大_2055843890846027778.json, 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json, 图片生成/图生图/Flux2+seedvr2高清放大_2043915810573389825.json, 图片生成/图生图/flux2-klein-产品精修-万物精修_2013791137181474818.json, 图片生成/图生图/最新Flux2 Klein 9B Klein万物产品精修_2043524112580087809.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux-Klein--产品精修_2054918894313320450.json、图片生成/图生图/Flux-Klein首饰产品精修 高清放大_2055474345887191041.json、图片生成/图生图/Flux-Klein首饰产品精修加高清放大_2055843890846027778.json、图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json、图片生成/图生图/Flux2+seedvr2高清放大_2043915810573389825.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
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

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `easy compare` —— 6/7 个有
- `easy int` —— 6/7 个有
- `AILab_QwenVL` —— 5/7 个有
- `BasicGuider` —— 5/7 个有
- `PreviewAny` —— 5/7 个有
- `easy ifElse` —— 5/7 个有
- `easy imageSizeBySide` —— 5/7 个有
- `AIO_Preprocessor` —— 2/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `CFGGuider` —— 2/7 个有
- `ColorMatch` —— 2/7 个有
- `ConditioningZeroOut` —— 2/7 个有
- `ImageScaleToTotalPixels` —— 2/7 个有
- `Text` —— 2/7 个有
- `CR Set Value On Boolean` —— 1/7 个有
- `Display Int (rgthree)` —— 1/7 个有
- `ImageSmartSharpen+` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `Switch any [Crystools]` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `easy imageColorMatch` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
