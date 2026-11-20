---
name: image_to_image_video_lora_sampler_12
type: Image To Image
frequency: 3
level: strong
coverage: 0.801333
common_nodes: [CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, GetNode, ImageResizeKJv2, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, Power Lora Loader (rgthree), PreviewImage, ReferenceLatent, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux kontext + ani全能视频S 2.0 ai 视频 - 打造卡通风格视频工作流_1945854630372798466.json, 平台全量/【港片秒变动漫】index-ani全能视频S：b站最强开源动漫生成模型ai二创神器来了_1947270538915893249.json, 平台全量/用index-ani全能视频S把电影1_1复刻成动漫视频_1947883979467829249.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/flux kontext + ani全能视频S 2.0 ai 视频 - 打造卡通风格视频工作流_1945854630372798466.json、平台全量/【港片秒变动漫】index-ani全能视频S：b站最强开源动漫生成模型ai二创神器来了_1947270538915893249.json、平台全量/用index-ani全能视频S把电影1_1复刻成动漫视频_1947883979467829249.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `GetNode`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `ReferenceLatent`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 2/3 个有
- `AudioSeparation` —— 2/3 个有
- `DownloadAndLoadWav2VecModel` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `MultiTalkModelLoader` —— 2/3 个有
- `MultiTalkWav2VecEmbeds` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `WanVideoExperimentalArgs` —— 2/3 个有
- `WanVideoFreeInitArgs` —— 2/3 个有
- `Bjornulf_ShowInt` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/3 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `Image To Mask` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `SAMLoader` —— 1/3 个有
- `Separate Mask Components` —— 1/3 个有
- `VHS_LoadAudioUpload` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `WanVideoContextOptions` —— 1/3 个有
- `WanVideoTorchCompileSettings` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
