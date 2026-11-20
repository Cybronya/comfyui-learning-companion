---
name: unknown_workflow_upscale_lora_sampler_64
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.733667
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, CropWithPadInfo, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, Get Image Size, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageStitch, KSampler, LoadImage, Lora Loader Stack (rgthree), PreviewImage, PrimitiveStringMultiline, QwenEditAdaptiveLongestEdge, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, easy cleanGpuUsed, easy imageScaleToNormPixels, easy showAnything, 数学运算_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/pixelsmile_表情编辑器_2083239651464278018.json, 图片生成/图生图/pixelsmile_表情编辑神器_2039524998611738625.json, 图片生成/图生图/真人转动漫🔸神级还原🔸QwenEdit-2511_2038531454111584258.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_64

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/pixelsmile_表情编辑器_2083239651464278018.json、图片生成/图生图/pixelsmile_表情编辑神器_2039524998611738625.json、图片生成/图生图/真人转动漫🔸神级还原🔸QwenEdit-2511_2038531454111584258.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `Get Image Size`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenEditAdaptiveLongestEdge`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`
- `easy cleanGpuUsed`
- `easy imageScaleToNormPixels`
- `easy showAnything`
- `数学运算_孤海`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `PixelSmileConditioning` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `easy whileLoopStart` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
