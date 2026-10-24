---
name: unknown_workflow_sampler_clip_unet_177
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.806571
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy compare, easy ifElse, easy imageSizeBySide, easy int]
problems: []
missing: []
members: [图片生成/图生图/Flux-Klein--产品精修_2054918894313320450.json, 图片生成/图生图/Flux-Klein首饰产品精修 高清放大_2055474345887191041.json, 图片生成/图生图/Flux-Klein首饰产品精修加高清放大_2055843890846027778.json, 图片生成/图生图/Flux2-klein-美甲迁移_2029843703233257474.json, 图片生成/图生图/Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2025741951122808834.json, 图片生成/图生图/flux2-klein-产品精修-万物精修_2013791137181474818.json, 图片生成/图生图/最新Flux2 Klein 9B Klein万物产品精修_2043524112580087809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_177

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux-Klein--产品精修_2054918894313320450.json、图片生成/图生图/Flux-Klein首饰产品精修 高清放大_2055474345887191041.json、图片生成/图生图/Flux-Klein首饰产品精修加高清放大_2055843890846027778.json、图片生成/图生图/Flux2-klein-美甲迁移_2029843703233257474.json、图片生成/图生图/Flux2-klein人物角色 任意变发型 发型迁移 假发模特_2025741951122808834.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy compare`
- `easy ifElse`
- `easy imageSizeBySide`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `PreviewAny` —— 6/7 个有
- `AILab_QwenVL` —— 5/7 个有
- `GetImageSize` —— 5/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `ImageScaleBy` —— 5/7 个有
- `PreviewImage` —— 5/7 个有
- `SeedVR2LoadDiTModel` —— 5/7 个有
- `SeedVR2LoadVAEModel` —— 5/7 个有
- `SeedVR2VideoUpscaler` —— 5/7 个有
- `AIO_Preprocessor` —— 2/7 个有
- `Any Switch (rgthree)` —— 2/7 个有
- `ColorMatch` —— 2/7 个有
- `ImpactMakeAnyList` —— 2/7 个有
- `Text` —— 2/7 个有
- `Text Multiline` —— 2/7 个有
- `easy imageSize` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
