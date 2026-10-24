---
name: unknown_workflow_upscale_sampler_clip_3
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.744286
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, KSampler, LatentPixelScale, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/001.Z-image生图巅峰017.亿级像素文、图生图_2033754255391199234.json, 图片生成/图生图/锋LORA工作流_1994693188973699074.json, 图片生成/文生图/1亿像素-z image-文生图_2000471696442261505.json, 图片生成/文生图/1亿像素超清Z-Image：文生图_2000551711179669505.json, 图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json, 图片生成/文生图/Z-Image  亿级像素文生图  高清放大_2001654114578776066.json, 图片生成/文生图/Z-Image 亿级像素 文生图  细节毕现 超高清 影像新标准 高清放大_1999343765208920065.json, 图片生成/文生图/Z-Image 亿级像素 文生图  细节毕现 超高清 影像新标准 高清放大_2011435557523558401.json, 图片生成/文生图/Z-Image+TTP（自己用）_1999837825807904769.json, 图片生成/文生图/Z-Image_亿级像素文生图v3，细节纤毫毕现，定义超高清影像新标准！高清放大_2095333918890352642.json, 图片生成/文生图/Z-Image_亿级像素文生图v3，细节纤毫毕现，定义超高清影像新标准！高清放大_2095456966670901249.json, 图片生成/文生图/Z-Image：亿级像素文生图v3，细节纤毫毕现，定义超高清影像新标准！高清放大_1997246493079834625.json, 图片生成/文生图/Z-Image：亿级像素文生图超高清影像新标准！高清放大_2013152177841246210.json, 图片生成/文生图/Z-Image：神级像素文生图_2084914391736209409.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/001.Z-image生图巅峰017.亿级像素文、图生图_2033754255391199234.json、图片生成/图生图/锋LORA工作流_1994693188973699074.json、图片生成/文生图/1亿像素-z image-文生图_2000471696442261505.json、图片生成/文生图/1亿像素超清Z-Image：文生图_2000551711179669505.json、图片生成/文生图/LHSTW30M-DMT.Z-Image亿级像素文生图_1998758421291749377.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 14 个 workflow 都包含：
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
- `JjkText` —— 13/14 个有
- `LayerUtility: ImageReel` —— 13/14 个有
- `LayerUtility: ImageReelComposit` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `RH_LLMAPI_NODE` —— 12/14 个有
- `PreviewAny` —— 10/14 个有
- `easy showAnything` —— 4/14 个有
- `LoadImage` —— 3/14 个有
- `Anything Everywhere` —— 2/14 个有
- `CR Text Concatenate` —— 2/14 个有
- `AILab_QwenVL` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `Int` —— 1/14 个有
- `JoinStrings` —— 1/14 个有
- `ModelSamplingAuraFlow` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有
- `Qwen3_VQA` —— 1/14 个有
- `SetNode` —— 1/14 个有
- `easy loraStack` —— 1/14 个有
- `easy loraStackApply` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 14 | 97% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 14 | 97% |
| 采样算法 | gradient_estimation | - | 14 | 79% |
| 调度器 | sgm_uniform | - | 14 | 93% |
| 重绘幅度 | 1 | 0.25 - 1 | 14 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，14 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，14 个样本，取值集中（一致性 97%）
- 采样算法 最常用 gradient_estimation，14 个样本，一致性 79%
- 调度器 最常用 sgm_uniform，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，14 个样本
