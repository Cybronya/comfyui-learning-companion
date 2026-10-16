---
key: 视频生成/图生视频/LTX2.3音频参考、图生视频、首尾帧、多帧参考三模一致性_去字幕全面优化版_2051946649047576577.json
name: LTX2.3音频参考、图生视频、首尾帧、多帧参考三模一致性_去字幕全面优化版_2051946649047576577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2051946649047576577.json
hash: 4cee552ed0226719
coverage: 0.960784
learned_at: 2026-10-15 22:37:25
nodes: [easy setNode, easy int, easy int, easy setNode, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, easy getNode, CFGGuider, easy getNode, easy getNode, easy setNode, easy setNode, easy getNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, VAELoaderKJ, easy setNode, easy getNode, LTXVCropGuides, VAEDecodeTiled, VAEDecodeTiled, KSamplerSelect, ManualSigmas, easy getNode, VHS_VideoCombine, CLIPTextEncode, LTXVConcatAVLatent, DualCLIPLoader, LoadImage, easy int, RandomNoise, easy getNode, easy getNode, easy getNode, VAELoaderKJ, easy getNode, LTX2_NAG, JWIntegerToString, JWIntegerToString, LoadAudio, easy setNode, easy setNode, AudioCrop, Audio Duration (mtb), MathExpression|pysssss, easy showAnything, LTXVAudioVAEEncode, LTXVAudioVAEEncode, easy setNode, easy getNode, easy getNode, easy getNode, Int, easy getNode, Int, MathExpression|pysssss, easy int, MathExpression|pysssss, MathExpression|pysssss, easy setNode, SetLatentNoiseMask, easy setNode, easy setNode, MathExpression|pysssss, easy getNode, easy setNode, LTXVEmptyLatentAudio, easy setNode, LTXVScheduler, LTXVConcatAVLatent, MarkdownNote, LTXVPreprocess, AudioSeparation, ManualSigmas, ManualSigmas, LoadImage, easy getNode, LTXVConditioning, Int, SetLatentNoiseMask, easy showAnything, SamplerEulerAncestral, VHS_VideoCombine, Audio Duration (mtb), easy getNode, easy getNode, AudioSeparation, easy setNode, RunningHub_VoxCPM_LoadModel, LoadAudio, RunningHub_VoxCPM_Generate, easy setNode, easy setNode, easy getNode, DF_Int_to_Float, easy getNode, easy setNode, easy getNode, DF_Int_to_Float, PreviewAudio, Int, easy setNode, easy getNode, easy getNode, LTXVSeparateAVLatent, ShowAnything|Mie, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageResizeKJv2, ImageResizeKJv2, easy getNode, easy getNode, ImageResizeKJv2, easy getNode, easy getNode, LoadImage, easy setNode, easy getNode, easy getNode, MarkdownNote, CLIPTextEncode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, SolidMask, easy getNode, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVPreprocess, easy int, easy getNode, easy getNode, LTXVAudioVAEDecode, EmptyLTXVLatentVideo, easy setNode, MarkdownNote, MarkdownNote, LoadImage, LoraLoaderModelOnly, DiffusionModelLoaderKJ, LoraLoaderModelOnly, easy setNode, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3音频参考、图生视频、首尾帧、多帧参考三模一致性_去字幕全面优化版_2051946649047576577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051946649047576577.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（153 个）：
- `easy setNode`
- `easy int`
- `easy int`
- `easy setNode`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy getNode`
- `CFGGuider`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `VAELoaderKJ`
- `easy setNode`
- `easy getNode`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `easy getNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `DualCLIPLoader`
- `LoadImage`
- `easy int`
- `RandomNoise`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `VAELoaderKJ`
- `easy getNode`
- `LTX2_NAG`
- `JWIntegerToString`
- `JWIntegerToString`
- `LoadAudio`
- `easy setNode`
- `easy setNode`
- `AudioCrop`
- `Audio Duration (mtb)`
- `MathExpression|pysssss`
- `easy showAnything`
- `LTXVAudioVAEEncode` ★核心
- `LTXVAudioVAEEncode` ★核心
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `Int`
- `easy getNode`
- `Int`
- `MathExpression|pysssss`
- `easy int`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy setNode`
- `SetLatentNoiseMask`
- `easy setNode`
- `easy setNode`
- `MathExpression|pysssss`
- `easy getNode`
- `easy setNode`
- `LTXVEmptyLatentAudio` ★核心
- `easy setNode`
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `LTXVPreprocess`
- `AudioSeparation`
- `ManualSigmas`
- `ManualSigmas`
- `LoadImage`
- `easy getNode`
- `LTXVConditioning`
- `Int`
- `SetLatentNoiseMask`
- `easy showAnything`
- `SamplerEulerAncestral` ★核心
- `VHS_VideoCombine`
- `Audio Duration (mtb)`
- `easy getNode`
- `easy getNode`
- `AudioSeparation`
- `easy setNode`
- `RunningHub_VoxCPM_LoadModel`
- `LoadAudio`
- `RunningHub_VoxCPM_Generate`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `DF_Int_to_Float`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `DF_Int_to_Float`
- `PreviewAudio`
- `Int`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `LTXVSeparateAVLatent`
- `ShowAnything|Mie`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy getNode`
- `easy getNode`
- `ImageResizeKJv2`
- `easy getNode`
- `easy getNode`
- `LoadImage`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `SolidMask`
- `easy getNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `easy int`
- `easy getNode`
- `easy getNode`
- `LTXVAudioVAEDecode` ★核心
- `EmptyLTXVLatentVideo`
- `easy setNode`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `easy setNode`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（147/153）

**有卡**：`easy setNode`、`easy int`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`easy getNode`、`LTXVSeparateAVLatent`、`RandomNoise`、`VAELoaderKJ`、`LTXVCropGuides`、`VAEDecodeTiled`、`ManualSigmas`、`VHS_VideoCombine`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`DualCLIPLoader`、`LoadImage`、`LTX2_NAG`、`JWIntegerToString`、`LoadAudio`、`AudioCrop`、`Audio Duration (mtb)`、`MathExpression|pysssss`、`LTXVAudioVAEEncode`、`Int`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`LTXVScheduler`、`LTXVPreprocess`、`AudioSeparation`、`LTXVConditioning`、`SamplerEulerAncestral`、`RunningHub_VoxCPM_LoadModel`、`RunningHub_VoxCPM_Generate`、`DF_Int_to_Float`、`PreviewAudio`、`ShowAnything|Mie`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`SolidMask`、`LTXVImgToVideoInplaceKJ`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`DiffusionModelLoaderKJ`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、SamplerEulerAncestral、LTXVConcatAVLatent
