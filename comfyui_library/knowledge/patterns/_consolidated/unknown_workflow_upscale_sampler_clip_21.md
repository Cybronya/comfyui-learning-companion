---
name: unknown_workflow_upscale_sampler_clip_21
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.7025
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningAverage, Constant Number, Florence2Run, Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, KSampler, Latent Noise Injection, LoadImage, ModelSamplingAuraFlow, SaveImage, TTP_CoordinateSplitter, TTP_Image_Tile_Batch, TTP_Tile_image_size, TTP_condsetarea_merge, TTP_condtobatch, UNETLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageInsetCrop]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/251225001.012.Z-image超级细节极致放大图生图_2004248891866443778.json, 图片生成/图生图/LH-DMT版本-2.生图片类-037.Z-image超级细节极致放大图生图_2016519560576372738.json, 图片生成/图生图/人像高清放大专用 Z image 4k 版 V1_2001955720734076930.json, 图片生成/图生图/人像高清放大专用4k_8k Z image V2_2004119992973049857.json, 图片生成/图生图/图片细节还原Z-image超级细节极致放大_2001552794735767553.json, 图片生成/图生图/🤖图片细节还原Z-image超级细节极致放大 适合细节控🤖_2000430481520947201.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/251225001.012.Z-image超级细节极致放大图生图_2004248891866443778.json、图片生成/图生图/LH-DMT版本-2.生图片类-037.Z-image超级细节极致放大图生图_2016519560576372738.json、图片生成/图生图/人像高清放大专用 Z image 4k 版 V1_2001955720734076930.json、图片生成/图生图/人像高清放大专用4k_8k Z image V2_2004119992973049857.json、图片生成/图生图/图片细节还原Z-image超级细节极致放大_2001552794735767553.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningAverage`
- `Constant Number`
- `Florence2Run`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `Latent Noise Injection`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TTP_CoordinateSplitter`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TTP_condsetarea_merge`
- `TTP_condtobatch`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `TextEncodeQwenImageEditPlus` —— 4/6 个有
- `UnetLoaderGGUF` —— 4/6 个有
- `Upscale Model Loader` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `Anything Everywhere` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `Florence2ModelLoader` —— 2/6 个有
- `ImageResize+` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `UpscaleModelLoader` —— 2/6 个有
- `easy imageScaleToNormPixels` —— 2/6 个有
- `Float` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 8 | 6 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | sgm_uniform | - | 6 | 50% |
| 重绘幅度 | 0.6 | 0.2 - 0.8 | 6 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 6/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 50%
- 重绘幅度 中位数 0.6，观测区间 0.2 - 0.8，6 个样本
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足
- 高发问题（6/6 个样本）：发现KSampler但没有VAEDecode
