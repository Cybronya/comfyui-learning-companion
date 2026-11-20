---
name: unknown_workflow_lora_sampler_unet_84
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.838333
common_nodes: [CFGGuider, CLIPLoader, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, RandomNoise, SamplerCustomAdvanced, SaveImage, SolidMask, UNETLoader, VAEDecode, VAELoader, easy ifElse, easy isMaskEmpty]
problems: []
missing: []
members: [图片生成/图生图/Flux2-Klein-9b 无偏移换脸-换头_2016697396180291586.json, 图片生成/图生图/lth_2079975063083896833.json, 图片生成/图生图/换头换脸-Flux2-Klein-9B_2097870248031637505.json, 图片生成/图生图/换头换脸-Flux2-Klein-9B_2099409224215384065.json, 图片生成/图生图/终极一键换头+精细换脸lora版无大头超快速_2015997940753502209.json, 平台全量/FLUX2-klein终极换脸 光影、表情、神态高度一致（可自定义发饰是否一起迁移）_2016784228960182274.json, 平台全量/Flux2 Klein  换头_换脸 局部重绘 一致性人物替换 高清放大 增加细节_2022154441562001410.json, 平台全量/Klein 换头_换脸_1900396825642414082.json, 平台全量/换头换脸-Flux2-Klein-9B_2040796731406819329.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_84

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-9b 无偏移换脸-换头_2016697396180291586.json、图片生成/图生图/lth_2079975063083896833.json、图片生成/图生图/换头换脸-Flux2-Klein-9B_2097870248031637505.json、图片生成/图生图/换头换脸-Flux2-Klein-9B_2099409224215384065.json、图片生成/图生图/终极一键换头+精细换脸lora版无大头超快速_2015997940753502209.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `Flux2Scheduler`
- `GetImageSize`
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
- `GrowMaskWithBlur` —— 8/9 个有
- `LayerMask: MaskPreview` —— 7/9 个有
- `MaskFillHoles` —— 6/9 个有
- `PreviewImage` —— 5/9 个有
- `CR Text` —— 3/9 个有
- `LayerUtility: ImageReel` —— 3/9 个有
- `LayerUtility: ImageReelComposit` —— 3/9 个有
- `Any Switch (rgthree)` —— 1/9 个有
- `CR Text Concatenate` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `InpaintCrop` —— 1/9 个有
- `PreviewBridge` —— 1/9 个有
- `Qwen3_VQA` —— 1/9 个有
- `SAM3Segment` —— 1/9 个有
- `SAMLoader` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
