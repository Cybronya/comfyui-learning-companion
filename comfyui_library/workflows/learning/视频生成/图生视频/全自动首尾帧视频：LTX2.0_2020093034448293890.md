---
key: 视频生成/图生视频/全自动首尾帧视频：LTX2.0_2020093034448293890.json
name: 全自动首尾帧视频：LTX2.0_2020093034448293890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/全自动首尾帧视频：LTX2.0_2020093034448293890.json
hash: 4447af83f6499689
coverage: 0.75
learned_at: 2026-10-15 22:35:05
nodes: [KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, GetImageSize, Compare, GetImageSize, LTXVScheduler, GetNode, GetNode, LTXVAudioVAEDecode, Int, LTXVConditioning, Seed_, LTXVConcatAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, SamplerCustomAdvanced, GetNode, LTXVLatentUpsampler, LTXVFirstLastFrameControl_TTP, GetNode, CFGGuider, CFGGuider, LTXVCropGuides, LayerUtility: PurgeVRAM V2, VAEDecode, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, LTXVSeparateAVLatent, GetNode, PrimitiveNode, AudioSeparation, VAEDecode, LTXVAudioVAEDecode, VideoTranscribe, TranscribeConfig, VAEDecodeTiled, Note, VHS_VideoCombine, SubtitleOptimizer, easy showAnything, HAIGC_VideoSubtitleTimestampPro, CR Text, HAIGC_TimestampTextReplace, Note, CheckpointLoaderSimple, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, easy cleanGpuUsed, easy cleanGpuUsed, ImageResizeKJv2, RHHiddenNodes, CLIPTextEncode, GetNode, GetNode, CLIPTextEncode, easy ifElse, PreviewImage, Compare, EmptyImage, ImageScaleBy, ResizeImagesByLongerEdge, GetImageSize, PreviewImage, GetImageSize, LTXVPreprocess, easy ifElse, ResizeImagesByLongerEdge, LTXVPreprocess, PreviewImage, PreviewImage, MathExpression|pysssss, GetNode, GetNode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVFirstLastFrameControl_TTP, Note, GetNode, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/全自动首尾帧视频：LTX2.0_2020093034448293890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2020093034448293890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `GetImageSize`
- `Compare`
- `GetImageSize`
- `LTXVScheduler`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `Int`
- `LTXVConditioning`
- `Seed_`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVFirstLastFrameControl_TTP`
- `GetNode`
- `CFGGuider`
- `CFGGuider`
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVSeparateAVLatent`
- `GetNode`
- `PrimitiveNode`
- `AudioSeparation`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VideoTranscribe`
- `TranscribeConfig`
- `VAEDecodeTiled` ★核心
- `Note`
- `VHS_VideoCombine`
- `SubtitleOptimizer`
- `easy showAnything`
- `HAIGC_VideoSubtitleTimestampPro`
- `CR Text`
- `HAIGC_TimestampTextReplace`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `RHHiddenNodes`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy ifElse`
- `PreviewImage`
- `Compare`
- `EmptyImage`
- `ImageScaleBy`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `PreviewImage`
- `GetImageSize`
- `LTXVPreprocess`
- `easy ifElse`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `PreviewImage`
- `PreviewImage`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVFirstLastFrameControl_TTP`
- `Note`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 关键参数

- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（72/96）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LTXVConcatAVLatent`、`GetImageSize`、`Compare`、`LTXVScheduler`、`LTXVAudioVAEDecode`、`Int`、`LTXVConditioning`、`Seed_`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`LTXVFirstLastFrameControl_TTP`、`CFGGuider`、`LTXVCropGuides`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`ImageResizeKJv2`、`AudioSeparation`、`VideoTranscribe`、`TranscribeConfig`、`VAEDecodeTiled`、`VHS_VideoCombine`、`SubtitleOptimizer`、`HAIGC_VideoSubtitleTimestampPro`、`CR Text`、`HAIGC_TimestampTextReplace`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`easy cleanGpuUsed`、`RHHiddenNodes`、`CLIPTextEncode`、`EmptyImage`、`ImageScaleBy`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`MathExpression|pysssss`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
