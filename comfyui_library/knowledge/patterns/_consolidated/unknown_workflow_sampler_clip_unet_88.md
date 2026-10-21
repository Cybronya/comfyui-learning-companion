---
name: unknown_workflow_sampler_clip_unet_88
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.970714
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Text]
members: [图片生成/图生图/2093623432524156930.json, 图片生成/图生图/2102605007383261185.json, 图片生成/文生图/AI一键生成12张绝美新年写真集_2024044240682098690.json, 图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json, 图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json, 图片生成/文生图/Flux2 Klein 多图编辑&文生图 自由控制 平替全能图片 4B 极速 & 9B 质量_2012361850310107138.json, 图片生成/文生图/换装Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2035315458378833922.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_88

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/2093623432524156930.json、图片生成/图生图/2102605007383261185.json、图片生成/文生图/AI一键生成12张绝美新年写真集_2024044240682098690.json、图片生成/文生图/AI换脸丨Flux2-Klein丨参考图生成_2100837158843146242.json、图片生成/文生图/FLUX.2 Klein 4B工作流，8G显存1秒生成1张图片！_2012164022556172289.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
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
- `ConditioningZeroOut` —— 5/7 个有
- `EmptyFlux2LatentImage` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `CR Text` —— 4/7 个有
- `GetImageSize` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `ImageConcanate` —— 2/7 个有
- `Int` —— 2/7 个有
- `JWFloat` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `AspectRatio` —— 1/7 个有
- `HAIGC_LoadImagesFromZip` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `InpaintCropImproved` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有
- `InpaintStitchImproved` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `easy imageSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text
