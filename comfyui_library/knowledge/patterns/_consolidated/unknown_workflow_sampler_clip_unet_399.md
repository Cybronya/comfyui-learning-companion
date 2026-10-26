---
name: unknown_workflow_sampler_clip_unet_399
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.846
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2图像修复_2064329697353359361.json, 图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json, 图片生成/文生图/image_flux2_1999252927225229314.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_399

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/flux2图像修复_2064329697353359361.json、图片生成/文生图/flux2基础_文生图_图生图_迁移_1993562025060139010.json、图片生成/文生图/image_flux2_1999252927225229314.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `FluxGuidance`
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
- `EmptyFlux2LatentImage` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PiDTextPrompt` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `image_scale_pixel_v2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
