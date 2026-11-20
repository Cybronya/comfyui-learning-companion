---
name: image_to_image_video_lora_sampler_21
type: Image To Image
frequency: 2
level: weak
coverage: 0.5725
common_nodes: [AudioCrop, AudioSeparation, CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CreateVideo, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ModelSamplingSD3, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, SaveImage, SaveVideo, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/动漫版“高育良的最后一课”，AI漫画二创《人民的名义》教程_1973066378200657921.json, 平台全量/大猩猩躲在车底深情开唱《他一定很爱你》，还能顺便带货？ InfiniteTalk实战教程！_1959096136642539521.json]
source: knowledge_consolidation
---

# image_to_image_video_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/动漫版“高育良的最后一课”，AI漫画二创《人民的名义》教程_1973066378200657921.json、平台全量/大猩猩躲在车底深情开唱《他一定很爱你》，还能顺便带货？ InfiniteTalk实战教程！_1959096136642539521.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：57%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ModelSamplingSD3`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `SaveImage`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowInt` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `Display Int (rgthree)` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageBatch` —— 1/2 个有
- `ImageBatchMulti` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `LoadAudio` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `ReverseImageBatch` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `SoundFlow_GetLength` —— 1/2 个有
- `TextEncodeQwenImageEdit` —— 1/2 个有
- `TextEncodeQwenImageEditPlus` —— 1/2 个有
- `ToInt` —— 1/2 个有
- `TrimVideoLatent` —— 1/2 个有
- `WanAnimateToVideo` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27 | - | 2 | 15% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 27，样本不足，未给区间，2 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（16/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
