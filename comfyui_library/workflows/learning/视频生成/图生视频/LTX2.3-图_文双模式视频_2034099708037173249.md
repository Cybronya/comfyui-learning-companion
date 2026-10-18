---
key: 视频生成/图生视频/LTX2.3-图_文双模式视频_2034099708037173249.json
name: LTX2.3-图_文双模式视频_2034099708037173249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-图_文双模式视频_2034099708037173249.json
hash: 88065a3e6832cac9
coverage: 0.767442
learned_at: 2026-10-15 22:35:43
nodes: [Compare, GetImageSize, ImageScaleBy, PreviewImage, EmptyImage, SetNode, LTXVLatentUpsampler, GetNode, PrimitiveNode, AudioSeparation, VideoTranscribe, TranscribeConfig, VHS_VideoCombine, SubtitleOptimizer, easy showAnything, HAIGC_VideoSubtitleTimestampPro, CR Text, HAIGC_TimestampTextReplace, Note, LTXVAudioVAEDecode, PreviewImage, ImageResizeKJv2, ImageResizeKJv2, GetImageSize, LayerUtility: PurgeVRAM V2, VAEDecode, GetNode, GetNode, GetImageSize, CheckpointLoaderSimple, LTXVSeparateAVLatent, easy ifElse, LTXVPreprocess, ResizeImagesByLongerEdge, GetNode, LTXVImgToVideoInplace, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXAVTextEncoderLoader, SetNode, LTXVChunkFeedForward, easy cleanGpuUsed, LTXVAudioVAELoader, SetNode, LoraLoaderModelOnly, easy cleanGpuUsed, LatentUpscaleModelLoader, GetNode, CLIPTextEncode, CLIPTextEncode, GetNode, RHHiddenNodes, Int, MathExpression|pysssss, GetNode, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, GetNode, LTXVImgToVideoInplace, CR Text, LoadImage, CFGGuider, LTXVConditioning, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, LTXVConcatAVLatent, LTXVScheduler, Seed_, VHS_VideoCombine, RandomNoise, LTXVCropGuides, CFGGuider, BasicScheduler, KSamplerSelect, LTXVConcatAVLatent, GetNode, VAEDecode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LTXVAudioVAEDecode, GetNode, VHS_VideoCombine, PrimitiveBoolean, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/LTX2.3-图_文双模式视频_2034099708037173249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2034099708037173249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `Compare`
- `GetImageSize`
- `ImageScaleBy`
- `PreviewImage`
- `EmptyImage`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `PrimitiveNode`
- `AudioSeparation`
- `VideoTranscribe`
- `TranscribeConfig`
- `VHS_VideoCombine`
- `SubtitleOptimizer`
- `easy showAnything`
- `HAIGC_VideoSubtitleTimestampPro`
- `CR Text`
- `HAIGC_TimestampTextReplace`
- `Note`
- `LTXVAudioVAEDecode` ★核心
- `PreviewImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetImageSize`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetImageSize`
- `CheckpointLoaderSimple` ★核心
- `LTXVSeparateAVLatent`
- `easy ifElse`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `LTXVImgToVideoInplace`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `LTXVChunkFeedForward`
- `easy cleanGpuUsed`
- `LTXVAudioVAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `LatentUpscaleModelLoader`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `RHHiddenNodes`
- `Int`
- `MathExpression|pysssss`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVImgToVideoInplace`
- `CR Text`
- `LoadImage`
- `CFGGuider`
- `LTXVConditioning`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVScheduler`
- `Seed_`
- `VHS_VideoCombine`
- `RandomNoise`
- `LTXVCropGuides`
- `CFGGuider`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **77%**（66/86）

**有卡**：`Compare`、`GetImageSize`、`ImageScaleBy`、`EmptyImage`、`LTXVLatentUpsampler`、`AudioSeparation`、`VideoTranscribe`、`TranscribeConfig`、`VHS_VideoCombine`、`SubtitleOptimizer`、`HAIGC_VideoSubtitleTimestampPro`、`CR Text`、`HAIGC_TimestampTextReplace`、`LTXVAudioVAEDecode`、`ImageResizeKJv2`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`CheckpointLoaderSimple`、`LTXVSeparateAVLatent`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LTXVImgToVideoInplace`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXAVTextEncoderLoader`、`LTXVChunkFeedForward`、`easy cleanGpuUsed`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`RHHiddenNodes`、`Int`、`MathExpression|pysssss`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LoadImage`、`CFGGuider`、`LTXVConditioning`、`RandomNoise`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVScheduler`、`Seed_`、`LTXVCropGuides`、`BasicScheduler`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
