---
name: text_to_image_video_lora_sampler_176
type: Text To Image
frequency: 3
level: strong
coverage: 0.939667
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, DownloadAndLoadWav2VecModel, EmptyAudio, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), FlashVSRNode, FluxKontextImageScale, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcanate, ImageConcatMulti, ImageFromBatch+, ImageResizeKJ, ImageResizeKJv2, ImpactInt, IndexTTS2Run, Int, KSampler, KSamplerAdvanced, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, Mute / Bypass Repeater (rgthree), PainterI2V, PathchSageAttentionKJ, PlaySound|pysssss, PreviewAny, PreviewAudio, PreviewImage, PrimitiveInt, Qwen3_VQA, QwenMultiangleCameraNode, RIFE VFI, RandomNoise, SamplerCustomAdvanced, SaveImage, SeparateMasks, ShowText|pysssss, SimpleMath+, Text, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, TwoWaySwitch, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanFirstLastFrameToVideo, WanMoeKSampler, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoNAG, WanVideoSampler, WanVideoTextEncode, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, ZML_TextInput, easy cleanGpuUsed, easy imageConcat, easy imageRemBg, easy promptConcat, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图高清运镜_2042074029347053569.json, 视频生成/图生视频/WH-AI-Studio新短剧生产一条龙工作流（文生图、分镜、运镜、图生视频、视频生视频、数字人等）_2027381590065680386.json, 视频生成/图生视频/WH-AI-Studio短剧生产一条龙工作流（文生图、分镜、运镜、图生视频、视频生视频、数字人等）_2025518081585451009.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_176

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/文生图高清运镜_2042074029347053569.json、视频生成/图生视频/WH-AI-Studio新短剧生产一条龙工作流（文生图、分镜、运镜、图生视频、视频生视频、数字人等）_2027381590065680386.json、视频生成/图生视频/WH-AI-Studio短剧生产一条龙工作流（文生图、分镜、运镜、图生视频、视频生视频、数字人等）_2025518081585451009.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CR Text`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DownloadAndLoadWav2VecModel`
- `EmptyAudio`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `FlashVSRNode`
- `FluxKontextImageScale`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `ImpactInt`
- `IndexTTS2Run`
- `Int`
- `KSampler`
- `KSamplerAdvanced`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `Mute / Bypass Repeater (rgthree)`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewAny`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveInt`
- `Qwen3_VQA`
- `QwenMultiangleCameraNode`
- `RIFE VFI`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeparateMasks`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `TwoWaySwitch`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoNAG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `ZML_TextInput`
- `easy cleanGpuUsed`
- `easy imageConcat`
- `easy imageRemBg`
- `easy promptConcat`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 2/3 个有
- `EmptyFlux2LatentImage` —— 2/3 个有
- `Flux2Scheduler` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `JWStringConcat` —— 2/3 个有
- `RMBG` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `UpscaleImageByUsingModel` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `BasicGuider` —— 1/3 个有
- `BasicScheduler` —— 1/3 个有
- `CR Prompt List` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `EG_FX_BDAPI` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `JoinStrings` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 33% |
| Prompt 约束强度(CFG) | 6 | 1 - 8 | 3 | 41% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 3 | 33% |
| 重绘幅度 | euler_ancestral | - | 3 | 33% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 33%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 8，3 个样本，取值分散，一致性仅 41%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 1，3 个样本，一致性 33%
- 重绘幅度 最常用 euler_ancestral，3 个样本，一致性 33%
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高发问题（7/3 个样本）：Steps较低可能导致细节不足
