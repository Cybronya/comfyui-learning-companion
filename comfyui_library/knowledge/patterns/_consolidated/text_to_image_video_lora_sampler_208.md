---
name: text_to_image_video_lora_sampler_208
type: Text To Image
frequency: 2
level: weak
coverage: 0.938
common_nodes: [AudioCrop, AudioSeparation, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CR Text, CheckpointLoaderSimple, ConditioningZeroOut, DownloadAndLoadWav2VecModel, EmptyAudio, EmptyLatentImage, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), FlashVSRNode, FluxKontextImageScale, GetImageRangeFromBatch, GetImageSizeAndCount, ImageConcanate, ImageConcatMulti, ImageFromBatch+, ImageResizeKJ, ImageResizeKJv2, ImpactInt, IndexTTS2Run, Int, KSampler, KSamplerAdvanced, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, MaskPreview+, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, Mute / Bypass Repeater (rgthree), PainterI2V, PathchSageAttentionKJ, PlaySound|pysssss, PreviewAny, PreviewAudio, PreviewImage, PrimitiveInt, Qwen3_VQA, QwenMultiangleCameraNode, RIFE VFI, RandomNoise, SamplerCustomAdvanced, SaveImage, SeparateMasks, ShowText|pysssss, SimpleMath+, Text, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlusAdvance_lrzjason, TwoWaySwitch, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanFirstLastFrameToVideo, WanMoeKSampler, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoNAG, WanVideoSampler, WanVideoTextEncode, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, ZML_TextInput, easy cleanGpuUsed, easy imageConcat, easy imageRemBg, easy promptConcat, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2027381590065680386.json, 视频生成/图生视频/2025518081585451009.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_208

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2027381590065680386.json、视频生成/图生视频/2025518081585451009.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
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
- `BasicGuider` —— 1/2 个有
- `BasicScheduler` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `CR Prompt List` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EG_FX_BDAPI` —— 1/2 个有
- `EmptyFlux2LatentImage` —— 1/2 个有
- `Flux2Scheduler` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `JWStringConcat` —— 1/2 个有
- `JoinStrings` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `ReferenceLatent` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `UpscaleImageByUsingModel` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy promptLine` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 22% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | lcm | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 22%
- 调度器 最常用 lcm，2 个样本，一致性 50%
- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（5/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
