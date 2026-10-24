---
name: text_to_image_video_lora_sampler_191
type: Text To Image
frequency: 3
level: strong
coverage: 0.534333
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DrawMaskOnImage, EmptyLatentImage, FaceMaskFromPoseKeypoints, GetNode, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), GrowMask, ImageBatch, ImageCropByMaskAndResize, ImageFromBatch, ImageResizeKJv2, JjkText, KSampler, LoadImage, LoadImageFromPath, LoraLoaderModelOnly, MaskPreview, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PixelPerfectResolution, PreviewImage, PrimitiveInt, SAMModelLoader (segment anything), SetNode, TorchCompileModel, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_LoadVideoPath, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy forLoopEnd, easy forLoopStart, easy showAnything, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2088682068170600450.json, 视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2090421078559645697.json, 视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2091762747024433154.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_191

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2088682068170600450.json、视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2090421078559645697.json、视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2091762747024433154.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawMaskOnImage`
- `EmptyLatentImage`
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `ImageBatch`
- `ImageCropByMaskAndResize`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoadImageFromPath`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PixelPerfectResolution`
- `PreviewImage`
- `PrimitiveInt`
- `SAMModelLoader (segment anything)`
- `SetNode`
- `TorchCompileModel`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_LoadVideoPath`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（9/3 个样本）：Steps较低可能导致细节不足
