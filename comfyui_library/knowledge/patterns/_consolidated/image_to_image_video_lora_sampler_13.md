---
name: image_to_image_video_lora_sampler_13
type: Image To Image
frequency: 3
level: strong
coverage: 0.681
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, INTConstant, ImageConcatMulti, ImageFromBatch, ImageResizeKJv2, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy float]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/【AI小兵哥】Wan2_2_Animate_去全能视频S视频水印工作流_1977304029283930114.json, 平台全量/【AI小兵哥】Wan2_2_Animate_自动去全能视频S视频水印工作流_1989572501850214401.json, 平台全量/【AI小兵哥】wan2_2_Animate_画遮罩去水印去字幕工作流_1988637817196732417.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/【AI小兵哥】Wan2_2_Animate_去全能视频S视频水印工作流_1977304029283930114.json、平台全量/【AI小兵哥】Wan2_2_Animate_自动去全能视频S视频水印工作流_1989572501850214401.json、平台全量/【AI小兵哥】wan2_2_Animate_画遮罩去水印去字幕工作流_1988637817196732417.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `INTConstant`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `DualCLIPLoader` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `ImageBatchToList` —— 2/3 个有
- `Masks Add` —— 2/3 个有
- `PointsEditor` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `UltralyticsDetectorProvider` —— 2/3 个有
- `VHS_DuplicateMasks` —— 2/3 个有
- `BboxDetectorCombined_v2` —— 1/3 个有
- `CFGNorm` —— 1/3 个有
- `CLIPLoader` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `IntMath` —— 1/3 个有
- `JWImageBatchCount` —— 1/3 个有
- `MaskListToMaskBatch` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `SeCModelLoader` —— 1/3 个有
- `SeCVideoSegmentation` —— 1/3 个有
- `SegmDetectorCombined_v2` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy indexAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
