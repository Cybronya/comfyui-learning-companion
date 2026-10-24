---
name: unknown_workflow_sampler_clip_unet_186
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.883
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商万物迁移 Flux klein_2021109944589754370.json, 图片生成/图生图/电商产品场景图生成_2069077696059105281.json, 图片生成/图生图/电商产品换材质 flux2 klein_2026838584275247105.json, 图片生成/图生图/电商移除图片指定位置内容_2026115966425374721.json, 图片生成/图生图/🦖Flux2-klein单图编辑_2013897331980111873.json, 图片生成/文生图/AI一键生成12张绝美新年写真集_2024044240682098690.json, 图片生成/文生图/图片生成和编辑_Flux-2-Klein_2012115517577891842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_186

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/电商万物迁移 Flux klein_2021109944589754370.json、图片生成/图生图/电商产品场景图生成_2069077696059105281.json、图片生成/图生图/电商产品换材质 flux2 klein_2026838584275247105.json、图片生成/图生图/电商移除图片指定位置内容_2026115966425374721.json、图片生成/图生图/🦖Flux2-klein单图编辑_2013897331980111873.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
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
- `EmptyFlux2LatentImage` —— 6/7 个有
- `GetImageSize` —— 6/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `JjkText` —— 4/7 个有
- `Colored Image (mtb)` —— 2/7 个有
- `easy int` —— 2/7 个有
- `AILab_QwenVL` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `HAIGC_LoadImagesFromZip` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LayerUtility: CropByMask V3` —— 1/7 个有
- `LayerUtility: RestoreCropBox` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `Qwen2.5` —— 1/7 个有
- `SetNode` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
