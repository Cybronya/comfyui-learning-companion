---
name: unknown_workflow_lora_sampler_unet_136
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8578
common_nodes: [CFGGuider, CLIPLoader, Flux2Scheduler, GetImageSize, GrowMaskWithBlur, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, RandomNoise, SamplerCustomAdvanced, SaveImage, SolidMask, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy isMaskEmpty]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein-9b 无偏移换脸-换头_2016697396180291586.json, 图片生成/图生图/lth_2079975063083896833.json, 图片生成/图生图/换头换脸-Flux2-Klein-9B_2097870248031637505.json, 图片生成/图生图/换头换脸-Flux2-Klein-9B_2099409224215384065.json, 图片生成/图生图/终极一键换头+精细换脸lora版无大头超快速_2015997940753502209.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-9b 无偏移换脸-换头_2016697396180291586.json、图片生成/图生图/lth_2079975063083896833.json、图片生成/图生图/换头换脸-Flux2-Klein-9B_2097870248031637505.json、图片生成/图生图/换头换脸-Flux2-Klein-9B_2099409224215384065.json、图片生成/图生图/终极一键换头+精细换脸lora版无大头超快速_2015997940753502209.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `Flux2Scheduler`
- `GetImageSize`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SolidMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy ifElse`
- `easy isMaskEmpty`

**可变部分**（部分 workflow 才有）：
- `LayerMask: MaskPreview` —— 3/5 个有
- `CR Text` —— 2/5 个有
- `LayerUtility: ImageReel` —— 2/5 个有
- `LayerUtility: ImageReelComposit` —— 2/5 个有
- `MaskFillHoles` —— 2/5 个有
- `PreviewImage` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
