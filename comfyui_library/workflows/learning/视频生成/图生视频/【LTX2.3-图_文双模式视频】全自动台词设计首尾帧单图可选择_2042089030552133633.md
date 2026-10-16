---
key: 视频生成/图生视频/【LTX2.3-图_文双模式视频】全自动台词设计首尾帧单图可选择_2042089030552133633.json
name: 【LTX2.3-图_文双模式视频】全自动台词设计首尾帧单图可选择_2042089030552133633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2042089030552133633.json
hash: 70bc6eebb037d71b
coverage: 0.747664
learned_at: 2026-10-15 22:36:24
nodes: [RandomNoise, Compare, GetImageSize, ImageScaleBy, Compare, PreviewImage, GetImageSize, PreviewImage, LTXVPreprocess, PreviewImage, EmptyImage, SetNode, GetNode, Seed_, Note, RandomNoise, LTXVLatentUpsampler, GetNode, CFGGuider, LayerUtility: PurgeVRAM V2, PrimitiveNode, AudioSeparation, VAEDecode, LTXVAudioVAEDecode, VideoTranscribe, TranscribeConfig, VHS_VideoCombine, SubtitleOptimizer, easy showAnything, HAIGC_VideoSubtitleTimestampPro, CR Text, HAIGC_TimestampTextReplace, Note, SamplerCustomAdvanced, LTXVCropGuides, easy cleanGpuUsed, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVConcatAVLatent, LTXVAudioVAEDecode, easy ifElse, PreviewImage, Int, MathExpression|pysssss, LatentUpscaleModelLoader, ImageResizeKJv2, ImageResizeKJv2, ResizeImagesByLongerEdge, ImageResizeKJv2, ImageResizeKJv2, LTXVEmptyLatentAudio, Note, LoraLoaderModelOnly, Float, Float, GetImageSize, LayerUtility: PurgeVRAM V2, VAEDecode, GetNode, GetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, GetImageSize, EmptyLTXVLatentVideo, VHS_VideoCombine, CheckpointLoaderSimple, LTXVConditioning, CLIPTextEncode, LTXVConcatAVLatent, CFGGuider, LTXVSeparateAVLatent, VHS_VideoCombine, KSamplerSelect, easy ifElse, LTXVPreprocess, KSamplerSelect, BasicScheduler, ResizeImagesByLongerEdge, PathchSageAttentionKJ, LTXVScheduler, ManualSigmas, ModelPatchTorchSettings, LTXVChunkFeedForward, easy cleanGpuUsed, Note, LTXVFirstLastFrameControl_TTP, LTXVImgToVideoInplace, LTXVFirstLastFrameControl_TTP, GetNode, GetNode, Note, PrimitiveBoolean, Note, SetNode, SetNode, GetNode, LTXVImgToVideoInplace, GetNode, GetNode, GetNode, CLIPTextEncode, RHHiddenNodes, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 24, "width": 97}
---

# 视频生成/图生视频/【LTX2.3-图_文双模式视频】全自动台词设计首尾帧单图可选择_2042089030552133633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042089030552133633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `RandomNoise`
- `Compare`
- `GetImageSize`
- `ImageScaleBy`
- `Compare`
- `PreviewImage`
- `GetImageSize`
- `PreviewImage`
- `LTXVPreprocess`
- `PreviewImage`
- `EmptyImage`
- `SetNode`
- `GetNode`
- `Seed_`
- `Note`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `CFGGuider`
- `LayerUtility: PurgeVRAM V2`
- `PrimitiveNode`
- `AudioSeparation`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VideoTranscribe`
- `TranscribeConfig`
- `VHS_VideoCombine`
- `SubtitleOptimizer`
- `easy showAnything`
- `HAIGC_VideoSubtitleTimestampPro`
- `CR Text`
- `HAIGC_TimestampTextReplace`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `easy cleanGpuUsed`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `easy ifElse`
- `PreviewImage`
- `Int`
- `MathExpression|pysssss`
- `LatentUpscaleModelLoader`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVEmptyLatentAudio` ★核心
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Float`
- `Float`
- `GetImageSize`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `KSamplerSelect` ★核心
- `easy ifElse`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ResizeImagesByLongerEdge`
- `PathchSageAttentionKJ`
- `LTXVScheduler`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `easy cleanGpuUsed`
- `Note`
- `LTXVFirstLastFrameControl_TTP`
- `LTXVImgToVideoInplace`
- `LTXVFirstLastFrameControl_TTP`
- `GetNode`
- `GetNode`
- `Note`
- `PrimitiveBoolean`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **75%**（80/107）

**有卡**：`RandomNoise`、`Compare`、`GetImageSize`、`ImageScaleBy`、`LTXVPreprocess`、`EmptyImage`、`Seed_`、`LTXVLatentUpsampler`、`CFGGuider`、`LayerUtility: PurgeVRAM V2`、`AudioSeparation`、`VAEDecode`、`LTXVAudioVAEDecode`、`VideoTranscribe`、`TranscribeConfig`、`VHS_VideoCombine`、`SubtitleOptimizer`、`HAIGC_VideoSubtitleTimestampPro`、`CR Text`、`HAIGC_TimestampTextReplace`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`easy cleanGpuUsed`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVConcatAVLatent`、`Int`、`MathExpression|pysssss`、`LatentUpscaleModelLoader`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`LTXVEmptyLatentAudio`、`LoraLoaderModelOnly`、`Float`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`CheckpointLoaderSimple`、`LTXVConditioning`、`CLIPTextEncode`、`KSamplerSelect`、`BasicScheduler`、`PathchSageAttentionKJ`、`LTXVScheduler`、`ManualSigmas`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LTXVFirstLastFrameControl_TTP`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`RHHiddenNodes`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
