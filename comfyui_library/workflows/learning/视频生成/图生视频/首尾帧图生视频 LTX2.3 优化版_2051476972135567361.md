---
key: 视频生成/图生视频/首尾帧图生视频 LTX2.3 优化版_2051476972135567361.json
name: 首尾帧图生视频 LTX2.3 优化版_2051476972135567361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧图生视频 LTX2.3 优化版_2051476972135567361.json
hash: 3abd2901f4f8197a
coverage: 0.854545
learned_at: 2026-10-15 22:37:22
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, KSamplerSelect, CLIPTextEncode, LTXVEmptyLatentAudio, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, RandomNoise, RandomNoise, CLIPTextEncode, LatentUpscaleModelLoader, CheckpointLoaderSimple, LTXVConcatAVLatent, FloatConstant, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, ManualSigmas, LTXVImgToVideoInplaceKJ, ComfyMathExpression, LTXVConditioning, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVPreprocess, SimpleMath+, LTXVPreprocess, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, Reroute, LTXVLatentUpsampler, LTXVImgToVideoInplace, PrimitiveInt, ImageResizeKJv2, ImageResizeKJv2, LTXVAudioVAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXAVTextEncoderLoader, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/首尾帧图生视频 LTX2.3 优化版_2051476972135567361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051476972135567361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `RandomNoise`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `LatentUpscaleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `FloatConstant`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `ManualSigmas`
- `LTXVImgToVideoInplaceKJ`
- `ComfyMathExpression`
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVPreprocess`
- `SimpleMath+`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `Reroute`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXAVTextEncoderLoader`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **85%**（47/55）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`RandomNoise`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`FloatConstant`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LTXVImgToVideoInplaceKJ`、`ComfyMathExpression`、`LTXVConditioning`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVPreprocess`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`ImageResizeKJv2`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LoadImage`、`LTXAVTextEncoderLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
