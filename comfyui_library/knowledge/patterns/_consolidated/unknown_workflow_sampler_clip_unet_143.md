---
name: unknown_workflow_sampler_clip_unet_143
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.931625
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json, 图片生成/反推提示词/37e-commerceiamge_2049772682647969794.json, 图片生成/反推提示词/82huantou_2053067673583529985.json, 图片生成/图生图/003.FLUX.2智能综合004.手动提示词单图编辑_2035170282356350977.json, 图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json, 图片生成/图生图/FLUX克莱因指令编辑_2019953559508361217.json, 图片生成/图生图/Flux2 klein kv高速图片编辑_2040977793638469634.json, 图片生成/图生图/电商万物迁移 Flux klein_2021109944589754370.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_143

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json、图片生成/反推提示词/37e-commerceiamge_2049772682647969794.json、图片生成/反推提示词/82huantou_2053067673583529985.json、图片生成/图生图/003.FLUX.2智能综合004.手动提示词单图编辑_2035170282356350977.json、图片生成/图生图/FLUX.2-klein_官方基础工作流（图像编辑）_2048613383078944770.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 7/8 个有
- `ReferenceLatent` —— 7/8 个有
- `VAEEncode` —— 7/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `FluxKVCache` —— 2/8 个有
- `ImpactInt` —— 2/8 个有
- `JjkText` —— 2/8 个有
- `RTXVideoSuperResolution` —— 2/8 个有
- `easy int` —— 2/8 个有
- `27eacb9f-0da2-421d-a0bf-b4b4e5fe5709` —— 1/8 个有
- `93041a64-452a-477a-9447-40330b7c1136` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `Colored Image (mtb)` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `LayerUtility: CropByMask V3` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `LayerUtility: RestoreCropBox` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
