---
name: unknown_workflow_upscale_sampler_clip_15
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.804
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, LatentPixelScale, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen2511-千万级像素文生图，终极高清放大版本_2004848765221695489.json, 图片生成/文生图/万亿级像素文生图 - 文生图Z-image+SeedVR2.5.1 定义超高清影像新标准高_2034249664538611713.json, 图片生成/文生图/亿级像素+超清细节放大-Z-Image+SeedVR2_2001658897922441218.json, 图片生成/文生图/文生图Z-image+SeedVR2.5.1 万亿级像素文生图，细节纤毫毕现，定义超高清影像新标准高_2033734929732870146.json, 图片生成/文生图/文生图_2075454482460274690.json, 图片生成/文生图/最新亿级像素文生图，细节纤毫毕现，超高清影像，高清放大_2046458596510142465.json, 图片生成/文生图/真实视界 • Z-image 亿级像素现场造像师：定格物理级现实的快门瞬间_2043616304438976514.json, 图片生成/文生图/真实视界 • Z-image 亿级像素现场造像师：定格物理级现实的快门瞬间_2057075322029436930.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/qwen2511-千万级像素文生图，终极高清放大版本_2004848765221695489.json、图片生成/文生图/万亿级像素文生图 - 文生图Z-image+SeedVR2.5.1 定义超高清影像新标准高_2034249664538611713.json、图片生成/文生图/亿级像素+超清细节放大-Z-Image+SeedVR2_2001658897922441218.json、图片生成/文生图/文生图Z-image+SeedVR2.5.1 万亿级像素文生图，细节纤毫毕现，定义超高清影像新标准高_2033734929732870146.json、图片生成/文生图/文生图_2075454482460274690.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `GetImageSize+`
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

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `LayerUtility: ImageReel` —— 5/8 个有
- `LayerUtility: ImageReelComposit` —— 5/8 个有
- `RH_LLMAPI_NODE` —— 5/8 个有
- `LoadImage` —— 3/8 个有
- `KOOK_ImageCompression` —— 2/8 个有
- `RH_LLMAPI_Pro_Node` —— 2/8 个有
- `RunningHub Deepcleaner` —— 2/8 个有
- `CFGNorm` —— 1/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/8 个有
- `HAIGC_SaveImagesToZip` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `easy imageScaleDownBy` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 8 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | gradient_estimation | - | 8 | 50% |
| 调度器 | sgm_uniform | - | 8 | 88% |
| 重绘幅度 | 1 | 0.2 - 1 | 8 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 gradient_estimation，8 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，8 个样本，取值分散，一致性仅 46%
