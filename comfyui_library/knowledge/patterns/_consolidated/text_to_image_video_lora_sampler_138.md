---
name: text_to_image_video_lora_sampler_138
type: Text To Image
frequency: 5
level: moderate
coverage: 0.737
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, ConditioningZeroOut, EmptyLTXVLatentVideo, EmptyLatentImage, EnhancedLoadDiffusionModel, ExtractNFrames, FluxKontextMultiReferenceLatentMethod, GetNode, INTConstant, ImageResizeKJv2, ImageScaleToTotalPixels, Int, JWInteger, KSampler, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LiconMSR, LoadImage, LoraLoaderModelOnly, LowVRAMCheckpointLoader, ManualSigmas, PreviewImage, RH_Captioner, RandomInt, RandomNoise, SamplerCustomAdvanced, SetNode, Split String by Commas, StringReplace, Text, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader, VHS_VideoCombine, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy imageCount, easy indexAnything, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/ltx-animate联合图生视频漫剧电商服装分镜真人_2074464289334845442.json, 视频生成/图生视频/ltx-scail2联合多参图生视频漫剧电商服装分镜真人_2074449807627874305.json, 视频生成/图生视频/最新版 LTX 无API图生多参分镜视频漫剧打斗电商服装分镜真人_2073690383254646785.json, 视频生成/图生视频/最新版LTX-ANIMATE多参联合漫剧电商服装分镜真人_2074389976934080514.json, 视频生成/图生视频/最新版LTX-SCAIL2多参联合图生视频漫剧电商服装分镜真人_2073960338130817025.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_138

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/ltx-animate联合图生视频漫剧电商服装分镜真人_2074464289334845442.json、视频生成/图生视频/ltx-scail2联合多参图生视频漫剧电商服装分镜真人_2074449807627874305.json、视频生成/图生视频/最新版 LTX 无API图生多参分镜视频漫剧打斗电商服装分镜真人_2073690383254646785.json、视频生成/图生视频/最新版LTX-ANIMATE多参联合漫剧电商服装分镜真人_2074389976934080514.json、视频生成/图生视频/最新版LTX-SCAIL2多参联合图生视频漫剧电商服装分镜真人_2073960338130817025.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `EmptyLTXVLatentVideo`
- `EmptyLatentImage`
- `EnhancedLoadDiffusionModel`
- `ExtractNFrames`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `Int`
- `JWInteger`
- `KSampler`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LiconMSR`
- `LoadImage`
- `LoraLoaderModelOnly`
- `LowVRAMCheckpointLoader`
- `ManualSigmas`
- `PreviewImage`
- `RH_Captioner`
- `RandomInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `Split String by Commas`
- `StringReplace`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy indexAnything`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatenate_UTK` —— 4/5 个有
- `CR Prompt Text` —— 3/5 个有
- `DrawViTPose` —— 3/5 个有
- `OnnxDetectionModelLoader` —— 3/5 个有
- `PoseAndFaceDetection` —— 3/5 个有
- `TextConcatenate_UTK` —— 3/5 个有
- `WanAnimatePlus BlockSwap` —— 3/5 个有
- `WanVideoAnimateEmbeds` —— 3/5 个有
- `WanVideoClipVisionEncode` —— 3/5 个有
- `WanVideoDecode` —— 3/5 个有
- `WanVideoLoraSelectMulti` —— 3/5 个有
- `WanVideoModelLoader` —— 3/5 个有
- `WanVideoSampler` —— 3/5 个有
- `WanVideoSetBlockSwap` —— 3/5 个有
- `WanVideoSetLoRAs` —— 3/5 个有
- `WanVideoTextEncodeCached` —— 3/5 个有
- `WanVideoVAELoader` —— 3/5 个有
- `BatchImagesNode` —— 2/5 个有
- `CLIPVisionEncode` —— 2/5 个有
- `CheckpointLoaderSimple` —— 2/5 个有
- `DiffusionModelLoaderKJ` —— 2/5 个有
- `ModelSamplingSD3` —— 2/5 个有
- `SAM3_VideoTrack` —— 2/5 个有
- `SCAIL2ColoredMask` —— 2/5 个有
- `WanChunkFeedForward` —— 2/5 个有
- `WanContextWindowsManual` —— 2/5 个有
- `WanSCAILMultirefInfinity` —— 2/5 个有
- `WanVideoMemoryEfficientSageAttentionPatch` —— 2/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/5 个有
- `GIMMVFI_interpolate` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1280 | 241 - 1280 | 5 | 41% |
| 高度 | 720 | 50 - 720 | 5 | 27% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 241 - 1280，5 个样本，取值分散，一致性仅 41%
- 高度 中位数 720，观测区间 50 - 720，5 个样本，取值分散，一致性仅 27%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
