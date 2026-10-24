---
name: unknown_workflow_upscale_latent_upscale_lora_60
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6805
common_nodes: [ASRMW, Any To String (mtb), AudioToFPS, CFGGuider, CLIPTextEncode, CR Text, CR Text Concatenate, DualCLIPLoader, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, ImpactSwitch, Int, InversionDemoLazySwitch, JWInteger, KSamplerSelect, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ProcessString, Qwen3_VQA, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, ShowText|pysssss, SolidMask, SomethingToString, Switch any [Crystools], VAEDecodeTiled, VAELoaderKJ, VRAMReserver, easy boolean, easy cleanGpuUsed, easy compare]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3音频对口型【数字人】测试版本+效果如图_2039639579086561281.json, 视频生成/图生视频/LTX2.3首尾帧+音频对口型_2034072615744180226.json, 视频生成/图生视频/QwenTTS+LTX2.0角色说话_2017601157362884610.json, 视频生成/图生视频/对口型LTX【Qwen-TTS音色设计】_2019964726540771330.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_60

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/LTX2.3音频对口型【数字人】测试版本+效果如图_2039639579086561281.json、视频生成/图生视频/LTX2.3首尾帧+音频对口型_2034072615744180226.json、视频生成/图生视频/QwenTTS+LTX2.0角色说话_2017601157362884610.json、视频生成/图生视频/对口型LTX【Qwen-TTS音色设计】_2019964726540771330.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `ASRMW`
- `Any To String (mtb)`
- `AudioToFPS`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `DualCLIPLoader`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `ImpactSwitch`
- `Int`
- `InversionDemoLazySwitch`
- `JWInteger`
- `KSamplerSelect`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ProcessString`
- `Qwen3_VQA`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `ShowText|pysssss`
- `SolidMask`
- `SomethingToString`
- `Switch any [Crystools]`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VRAMReserver`
- `easy boolean`
- `easy cleanGpuUsed`
- `easy compare`

**可变部分**（部分 workflow 才有）：
- `CR String To Combo` —— 3/4 个有
- `CheckpointLoaderSimple` —— 3/4 个有
- `Display Any (rgthree)` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `JoinStrings` —— 3/4 个有
- `LTXVAudioVAEDecode` —— 3/4 个有
- `LTXVImgToVideoInplace` —— 3/4 个有
- `PreviewAudio` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `ttN concat` —— 3/4 个有
- `AudioCrop` —— 2/4 个有
- `AudioDither` —— 2/4 个有
- `AudioPad` —— 2/4 个有
- `AudioResample` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `CreateVideo` —— 2/4 个有
- `LTX2_NAG` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `SaveAudio` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `TextInput_` —— 2/4 个有
- `WhisperSTT` —— 2/4 个有
- `AudioSeparation` —— 1/4 个有
- `FB_Qwen3TTSVoiceClone` —— 1/4 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/4 个有
- `PIP_IntegerCalculator` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `SaveAudioMP3` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
