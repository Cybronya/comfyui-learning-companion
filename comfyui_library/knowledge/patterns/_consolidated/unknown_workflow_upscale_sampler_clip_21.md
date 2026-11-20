---
name: unknown_workflow_upscale_sampler_clip_21
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.780375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-Klein--产品精修_2054918894313320450.json, 图片生成/图生图/Flux-Klein首饰产品精修 高清放大_2055474345887191041.json, 图片生成/图生图/Flux-Klein首饰产品精修加高清放大_2055843890846027778.json, 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json, 图片生成/图生图/Flux2+seedvr2高清放大_2043915810573389825.json, 图片生成/图生图/flux2-klein-产品精修-万物精修_2013791137181474818.json, 图片生成/图生图/最新Flux2 Klein 9B Klein万物产品精修_2043524112580087809.json, 平台全量/产品精修Flux2 Klein 9B Klein 万物修图 电商产品修复放大_2017839478374666241.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux-Klein--产品精修_2054918894313320450.json、图片生成/图生图/Flux-Klein首饰产品精修 高清放大_2055474345887191041.json、图片生成/图生图/Flux-Klein首饰产品精修加高清放大_2055843890846027778.json、图片生成/图生图/Flux2 Klein9B 图像编辑工作流 浮云2.2_2016809192056688641.json、图片生成/图生图/Flux2+seedvr2高清放大_2043915810573389825.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 7/8 个有
- `ImageScaleBy` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `easy compare` —— 7/8 个有
- `easy int` —— 7/8 个有
- `AILab_QwenVL` —— 6/8 个有
- `BasicGuider` —— 6/8 个有
- `PreviewAny` —— 6/8 个有
- `easy ifElse` —— 6/8 个有
- `easy imageSizeBySide` —— 6/8 个有
- `AIO_Preprocessor` —— 3/8 个有
- `Any Switch (rgthree)` —— 3/8 个有
- `ColorMatch` —— 3/8 个有
- `Text` —— 3/8 个有
- `CFGGuider` —— 2/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `ImageScaleToTotalPixels` —— 2/8 个有
- `CR Set Value On Boolean` —— 1/8 个有
- `Display Int (rgthree)` —— 1/8 个有
- `ImageSmartSharpen+` —— 1/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `Switch any [Crystools]` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy imageColorMatch` —— 1/8 个有
- `easy mathInt` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
