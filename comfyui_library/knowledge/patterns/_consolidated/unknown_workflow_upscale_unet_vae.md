---
name: unknown_workflow_upscale_unet_vae
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8982
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), ImageFromBatch, LayerColor: BrightnessContrastV2, LayerFilter: AddGrain, LayerFilter: GaussianBlurV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculator, LoadImage, MathExpression|pysssss, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein+SeedVR2+TTP超分放大_2065468154469502978.json, 图片生成/图生图/Klein+seedvr2+ttp一键高清放大_2074747188219043842.json, 图片生成/图生图/豹豹喵呜制作：超分放大V2_2062471464711966721.json, 图片生成/图生图/豹豹喵呜：Z-IMAGE+SEEDVR2分块放大，图片一键4k像素，纹理清晰可见。_2021915195823624193.json, 图片生成/图生图/超分放大工作流_2111020544844976130.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_unet_vae

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein+SeedVR2+TTP超分放大_2065468154469502978.json、图片生成/图生图/Klein+seedvr2+ttp一键高清放大_2074747188219043842.json、图片生成/图生图/豹豹喵呜制作：超分放大V2_2062471464711966721.json、图片生成/图生图/豹豹喵呜：Z-IMAGE+SEEDVR2分块放大，图片一键4k像素，纹理清晰可见。_2021915195823624193.json、图片生成/图生图/超分放大工作流_2111020544844976130.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
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
- `Fast Bypasser (rgthree)` —— 4/5 个有
- `Flux2KleinEditTextEncode_EditUtils` —— 4/5 个有
- `KSampler` —— 4/5 个有
- `LayerUtility: ImageScaleRestore V2` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `Anything Everywhere` —— 1/5 个有
- `BasicScheduler` —— 1/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `SamplerCustom` —— 1/5 个有
- `SamplerEulerAncestral` —— 1/5 个有
- `VAEEncode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1 | 1 - 1 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 75% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
