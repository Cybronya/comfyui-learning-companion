---
name: image_to_image_video_upscale_sampler
type: Image To Image
frequency: 10
level: strong
coverage: 0.8476
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GrowMaskWithBlur, Image Comparer (rgthree), ImageCompositeMasked, ImageFromBatch, ImageUpscaleWithModel, KSampler, LoadImage, MaskToImage, PreviewImage, ReferenceLatent, RepeatImageBatch, SaveImage, SolidMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEncode, WanVideoMiniMaxRemoverEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片去水印+视频去水印工作流_2001580253623513090.json, 图片生成/图生图/图片去水印+视频去水印工作流_2005194586215645186.json, 图片生成/图生图/图片去水印API_2040108289907761154.json, 图片生成/图生图/图片去水印（放大）+视频去水印_2063868546186305537.json, 图片生成/文生图/图片去水印+视频去水印工作流_2045441948609155073.json, 平台全量/图片去水印+视频去水印工作流_1995393670646050818.json, 平台全量/图片去水印+视频去水印工作流_2006699649188499458.json, 平台全量/图片去水印+视频去水印工作流_2010551323225231362.json, 平台全量/图片去水印+视频去水印工作流_2072924282866458625.json, 平台全量/工作流实用推荐篇2-图片去水印+视频去水印工作流_2016853716518834177.json]
source: knowledge_consolidation
---

# image_to_image_video_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图片去水印+视频去水印工作流_2001580253623513090.json、图片生成/图生图/图片去水印+视频去水印工作流_2005194586215645186.json、图片生成/图生图/图片去水印API_2040108289907761154.json、图片生成/图生图/图片去水印（放大）+视频去水印_2063868546186305537.json、图片生成/文生图/图片去水印+视频去水印工作流_2045441948609155073.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `ReferenceLatent`
- `RepeatImageBatch`
- `SaveImage`
- `SolidMask`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoMiniMaxRemoverEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 6/10 个有
- `ImageToMask` —— 6/10 个有
- `Int` —— 6/10 个有
- `LayerColor: AutoBrightness` —— 6/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/10 个有
- `LayerUtility: PurgeVRAM` —— 6/10 个有
- `LoadWanVideoT5TextEncoder` —— 6/10 个有
- `VHS_VideoInfoSource` —— 6/10 个有
- `WanVideoBlockSwap` —— 6/10 个有
- `WanVideoSetBlockSwap` —— 6/10 个有
- `WanVideoTextEncode` —— 6/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `GetImageSize+` —— 4/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
