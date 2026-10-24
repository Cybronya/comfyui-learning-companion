---
name: unknown_workflow_sampler_clip_unet_201
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.887333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json, 图片生成/图生图/003.FLUX.2智能综合004.手动提示词单图编辑_2035170282356350977.json, 图片生成/图生图/2026最新FLUX2-Klein 9B版文生图_单图多图编辑工作流_2012390556902625281.json, 图片生成/图生图/Flux 2 klein 单图编辑角色卡（多角度图-图生图）工作流_2054450460597202945.json, 图片生成/图生图/Flux2 Klein 指定角度生图  Multiangle Camera 可视化镜头角度控制_2012390917050732546.json, 图片生成/图生图/Flux2-Klein_9B_编辑_角度_光线_双图_2014310579040690177.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_201

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（comfyui-workflow-templates-json/image_flux2_klein_9b_kv_image_edit.json、图片生成/图生图/003.FLUX.2智能综合004.手动提示词单图编辑_2035170282356350977.json、图片生成/图生图/2026最新FLUX2-Klein 9B版文生图_单图多图编辑工作流_2012390556902625281.json、图片生成/图生图/Flux 2 klein 单图编辑角色卡（多角度图-图生图）工作流_2054450460597202945.json、图片生成/图生图/Flux2 Klein 指定角度生图  Multiangle Camera 可视化镜头角度控制_2012390917050732546.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `VAEEncode` —— 5/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `QwenMultiangleCameraNode` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `27eacb9f-0da2-421d-a0bf-b4b4e5fe5709` —— 1/6 个有
- `93041a64-452a-477a-9447-40330b7c1136` —— 1/6 个有
- `Any Switch (rgthree)` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `DWPreprocessor` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `FluxKVCache` —— 1/6 个有
- `ImpactInt` —— 1/6 个有
- `KepStringList` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `QwenMultiangleLightningNode` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
