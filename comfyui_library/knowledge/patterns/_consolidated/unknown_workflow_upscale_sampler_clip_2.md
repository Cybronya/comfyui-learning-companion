---
name: unknown_workflow_upscale_sampler_clip_2
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.7572
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LatentPixelScale, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1亿像素-z image-文生图_2000471696442261505.json, 图片生成/文生图/1亿像素超清Z-Image：文生图_2000551711179669505.json, 图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json, 图片生成/文生图/Z-Image  亿级像素文生图  高清放大_2001654114578776066.json, 图片生成/文生图/Z-Image 亿级像素 文生图  细节毕现 超高清 影像新标准 高清放大_1999343765208920065.json, 图片生成/文生图/Z-Image 亿级像素 文生图  细节毕现 超高清 影像新标准 高清放大_2011435557523558401.json, 图片生成/文生图/Z-Image+TTP（自己用）_1999837825807904769.json, 图片生成/文生图/Z-Image_亿级像素文生图v3，细节纤毫毕现，定义超高清影像新标准！高清放大_2095333918890352642.json, 图片生成/文生图/Z-Image_亿级像素文生图v3，细节纤毫毕现，定义超高清影像新标准！高清放大_2095456966670901249.json, 图片生成/文生图/Z-Image：亿级像素文生图v3，细节纤毫毕现，定义超高清影像新标准！高清放大_1997246493079834625.json, 图片生成/文生图/Z-Image：亿级像素文生图超高清影像新标准！高清放大_2013152177841246210.json, 图片生成/文生图/Z-Image：神级像素文生图_2084914391736209409.json, 图片生成/文生图/qwen2511-千万级像素文生图，终极高清放大版本_2004848765221695489.json, 图片生成/文生图/亿级像素+超清细节放大-Z-Image+SeedVR2_2001658897922441218.json, 图片生成/文生图/文生图_2075454482460274690.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_2

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/1亿像素-z image-文生图_2000471696442261505.json、图片生成/文生图/1亿像素超清Z-Image：文生图_2000551711179669505.json、图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json、图片生成/文生图/Z-Image  亿级像素文生图  高清放大_2001654114578776066.json、图片生成/文生图/Z-Image 亿级像素 文生图  细节毕现 超高清 影像新标准 高清放大_1999343765208920065.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `LatentPixelScale`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 14/15 个有
- `LayerUtility: ImageReel` —— 14/15 个有
- `LayerUtility: ImageReelComposit` —— 14/15 个有
- `LoraLoaderModelOnly` —— 14/15 个有
- `RH_LLMAPI_NODE` —— 12/15 个有
- `PreviewAny` —— 11/15 个有
- `easy showAnything` —— 3/15 个有
- `Anything Everywhere` —— 2/15 个有
- `CR Text Concatenate` —— 2/15 个有
- `LoadImage` —— 2/15 个有
- `AILab_QwenVL` —— 1/15 个有
- `CFGNorm` —— 1/15 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/15 个有
- `ModelSamplingAuraFlow` —— 1/15 个有
- `PlaySound|pysssss` —— 1/15 个有
- `easy imageScaleDownBy` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 15 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | gradient_estimation | - | 15 | 73% |
| 调度器 | sgm_uniform | - | 15 | 93% |
| 重绘幅度 | 1 | 0.25 - 1 | 15 | 65% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，15 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 gradient_estimation，15 个样本，一致性 73%
- 调度器 最常用 sgm_uniform，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，15 个样本
