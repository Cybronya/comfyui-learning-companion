---
name: unknown_workflow_video_upscale_latent_upscale_64
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.592167
common_nodes: [Any To String (mtb), CFGGuider, CLIPTextEncode, CR Text, CR Text Concatenate, Display Any (rgthree), DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, GetNode, ImageScaleBy, ImpactSwitch, Int, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, ProcessString, Qwen3_VQA, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetNode, ShowText|pysssss, SomethingToString, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VRAMReserver, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2009910509788733441.json, 视频生成/图生视频/2011770027745222658.json, 视频生成/图生视频/2016871878190702594.json, 视频生成/图生视频/2033108960152133633.json, 视频生成/图生视频/LTX2.3音频对口型_2087994877064867842.json, 视频生成/图生视频/2034928738709807106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_64

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2009910509788733441.json、视频生成/图生视频/2011770027745222658.json、视频生成/图生视频/2016871878190702594.json、视频生成/图生视频/2033108960152133633.json、视频生成/图生视频/LTX2.3音频对口型_2087994877064867842.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 6 个 workflow 都包含：
- `Any To String (mtb)`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `Display Any (rgthree)`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ProcessString`
- `Qwen3_VQA`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `SomethingToString`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VRAMReserver`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ASRMW` —— 5/6 个有
- `AudioToFPS` —— 5/6 个有
- `CheckpointLoaderSimple` —— 5/6 个有
- `InversionDemoLazySwitch` —— 5/6 个有
- `JWInteger` —— 5/6 个有
- `LTXVAudioVAEDecode` —— 5/6 个有
- `LTXVAudioVAEEncode` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `MelBandRoFormerModelLoader` —— 5/6 个有
- `MelBandRoFormerSampler` —— 5/6 个有
- `SetLatentNoiseMask` —— 5/6 个有
- `SolidMask` —— 5/6 个有
- `Switch any [Crystools]` —— 5/6 个有
- `easy compare` —— 5/6 个有
- `ttN concat` —— 5/6 个有
- `AudioCrop` —— 4/6 个有
- `CR String To Combo` —— 4/6 个有
- `CreateVideo` —— 4/6 个有
- `JoinStrings` —— 4/6 个有
- `LTXVImgToVideoInplace` —— 4/6 个有
- `PreviewAudio` —— 4/6 个有
- `RH_LLMAPI_NODE` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `TextInput_` —— 4/6 个有
- `easy boolean` —— 4/6 个有
- `LTX2_NAG` —— 3/6 个有
- `LTXAVTextEncoderLoader` —— 3/6 个有
- `LTXVAudioVAELoader` —— 3/6 个有
- `UnetLoaderGGUF` —— 3/6 个有
- `easy convertAnything` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `CR Value` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `LTXVAudioVideoMask` —— 2/6 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/6 个有
- `PrimitiveBoolean` —— 2/6 个有
- `WhisperSTT` —— 2/6 个有
- `easy imageConcat` —— 2/6 个有
- `AudioDither` —— 1/6 个有
- `AudioPad` —— 1/6 个有
- `AudioResample` —— 1/6 个有
- `AudioSeparation` —— 1/6 个有
- `DF_Get_image_size` —— 1/6 个有
- `FB_Qwen3TTSVoiceClone` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `LTX2SamplingPreviewOverride` —— 1/6 个有
- `LTXVEmptyLatentAudio` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `ModelScopeVisionPromptInversion_Sevr` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `PIP_IntegerCalculator` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `SaveAudio` —— 1/6 个有
- `SaveAudioMP3` —— 1/6 个有
- `easy int` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 24 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
