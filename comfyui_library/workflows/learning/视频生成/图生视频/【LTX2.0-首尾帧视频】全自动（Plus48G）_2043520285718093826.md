---
key: 视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2043520285718093826.json
name: 【LTX2.0-首尾帧视频】全自动（Plus48G）_2043520285718093826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2043520285718093826.json
hash: f0484c293de9f600
coverage: 0.73
learned_at: 2026-10-15 22:36:32
nodes: [KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, LTXVConcatAVLatent, LoraLoaderModelOnly, Compare, GetImageSize, GetImageSize, ImageScaleBy, GetImageSize, Compare, easy ifElse, PreviewImage, GetImageSize, LTXVScheduler, LTXVPreprocess, PreviewImage, LTXVPreprocess, PreviewImage, easy ifElse, EmptyImage, PreviewImage, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, LTXVEmptyLatentAudio, GetNode, GetNode, CR Text, LTXVFirstLastFrameControl_TTP, MathExpression|pysssss, Int, Note, Note, GetNode, GetNode, LTXVConditioning, Seed_, LTXVConcatAVLatent, Note, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, GetNode, LTXVLatentUpsampler, LTXVFirstLastFrameControl_TTP, GetNode, GetNode, CFGGuider, VHS_VideoCombine, EmptyLTXVLatentVideo, easy cleanGpuUsed, CFGGuider, CheckpointLoaderSimple, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, RHHiddenNodes, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, Note, LTXVSeparateAVLatent, GetNode, VAEDecode, LTXVAudioVAEDecode, VAEDecodeTiled, Note, HAIGC_VideoSubtitleTimestampPro, HAIGC_TimestampTextReplace, AudioSeparation, VideoTranscribe, SubtitleOptimizer, easy showAnything, TranscribeConfig, PrimitiveNode, VHS_VideoCombine, CR Text, Note, LTXVCropGuides, SamplerCustomAdvanced, VHS_VideoCombine, VAEDecode, LTXVAudioVAEDecode, LTXVSeparateAVLatent, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2-19b-dev-fp8.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/【LTX2.0-首尾帧视频】全自动（Plus48G）_2043520285718093826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043520285718093826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LoraLoaderModelOnly` ★核心
- `Compare`
- `GetImageSize`
- `GetImageSize`
- `ImageScaleBy`
- `GetImageSize`
- `Compare`
- `easy ifElse`
- `PreviewImage`
- `GetImageSize`
- `LTXVScheduler`
- `LTXVPreprocess`
- `PreviewImage`
- `LTXVPreprocess`
- `PreviewImage`
- `easy ifElse`
- `EmptyImage`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `CR Text`
- `LTXVFirstLastFrameControl_TTP`
- `MathExpression|pysssss`
- `Int`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `LTXVConditioning`
- `Seed_`
- `LTXVConcatAVLatent`
- `Note`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVFirstLastFrameControl_TTP`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`
- `easy cleanGpuUsed`
- `CFGGuider`
- `CheckpointLoaderSimple` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `RHHiddenNodes`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `Note`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `Note`
- `HAIGC_VideoSubtitleTimestampPro`
- `HAIGC_TimestampTextReplace`
- `AudioSeparation`
- `VideoTranscribe`
- `SubtitleOptimizer`
- `easy showAnything`
- `TranscribeConfig`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `CR Text`
- `Note`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2-19b-dev-fp8.safetensors`

## 知识

覆盖率 **73%**（73/100）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`RandomNoise`、`LTXVConcatAVLatent`、`LoraLoaderModelOnly`、`Compare`、`GetImageSize`、`ImageScaleBy`、`LTXVScheduler`、`LTXVPreprocess`、`EmptyImage`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`CR Text`、`LTXVFirstLastFrameControl_TTP`、`MathExpression|pysssss`、`Int`、`LTXVConditioning`、`Seed_`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`CFGGuider`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`easy cleanGpuUsed`、`CheckpointLoaderSimple`、`LayerUtility: PurgeVRAM V2`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`RHHiddenNodes`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`HAIGC_VideoSubtitleTimestampPro`、`HAIGC_TimestampTextReplace`、`AudioSeparation`、`VideoTranscribe`、`SubtitleOptimizer`、`TranscribeConfig`、`LTXVCropGuides`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
