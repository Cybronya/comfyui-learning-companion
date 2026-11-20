---
name: unknown_workflow_upscale_unet_vae
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.868125
common_nodes: [CLIPLoader, Image Comparer (rgthree), ImageFromBatch, LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LayerFilter: GaussianBlurV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculator, LoadImage, MathExpression|pysssss, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein+SeedVR2+TTP超分放大_2065468154469502978.json, 图片生成/图生图/Klein+seedvr2+ttp一键高清放大_2074747188219043842.json, 图片生成/图生图/豹豹喵呜制作：超分放大V2_2062471464711966721.json, 图片生成/图生图/豹豹喵呜：Z-IMAGE+SEEDVR2分块放大，图片一键4k像素，纹理清晰可见。_2021915195823624193.json, 图片生成/图生图/超分放大工作流_2111020544844976130.json, 平台全量/SeedVR2 分块高清放大_2066097947745538049.json, 平台全量/SeedVR2 图像放大_2074703672457646081.json, 平台全量/超分放大工作流_2074685289825652738.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_unet_vae

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Klein+SeedVR2+TTP超分放大_2065468154469502978.json、图片生成/图生图/Klein+seedvr2+ttp一键高清放大_2074747188219043842.json、图片生成/图生图/豹豹喵呜制作：超分放大V2_2062471464711966721.json、图片生成/图生图/豹豹喵呜：Z-IMAGE+SEEDVR2分块放大，图片一键4k像素，纹理清晰可见。_2021915195823624193.json、图片生成/图生图/超分放大工作流_2111020544844976130.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `LayerColor: BrightnessContrastV2`
- `LayerFilter: AddGrain`
- `LayerFilter: GaussianBlurV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculator`
- `LoadImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `Fast Bypasser (rgthree)` —— 6/8 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 6/8 个有
- `KSampler` —— 6/8 个有
- `LayerUtility: ImageScaleRestore V2` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `easy imageColorMatch` —— 6/8 个有
- `Anything Everywhere3` —— 5/8 个有
- `BasicScheduler` —— 2/8 个有
- `CLIPTextEncode` —— 2/8 个有
- `SamplerCustom` —— 2/8 个有
- `SamplerEulerAncestral` —— 2/8 个有
- `VAEEncode` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `CheckpointLoaderSimple` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有
- `SUPIR_Upscale` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `UltimateSDUpscale` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有
- `easy int` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 1 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | res_2s | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
