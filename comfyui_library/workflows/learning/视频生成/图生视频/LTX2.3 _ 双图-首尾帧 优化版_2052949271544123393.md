---
key: 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2052949271544123393.json
name: LTX2.3 _ 双图-首尾帧 优化版_2052949271544123393.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2052949271544123393.json
hash: 1d0f9df11842cf35
coverage: 0.847458
learned_at: 2026-10-15 22:37:34
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAELoader, CFGGuider, LTXVConditioning, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, CLIPTextEncode, LTXVPreprocess, LatentUpscaleModelLoader, CreateVideo, PrimitiveInt, VAEDecodeTiled, CheckpointLoaderSimple, LTXVConcatAVLatent, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVLatentUpsampler, LTXVImgToVideoInplace, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, LoraLoaderModelOnly, ManualSigmas, SimpleMath+, MarkdownNote, LTXVImgToVideoInplaceKJ, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, MarkdownNote, ImageResize+, ResizeImagesByLongerEdge, PrimitiveInt, PrimitiveInt, ImageResize+, SaveVideo, easy showAnything, LoadImage, LoadImage, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, CLIPTextEncode, FloatConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2052949271544123393.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052949271544123393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `CFGGuider`
- `LTXVConditioning`
- `RandomNoise`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `SimpleMath+`
- `MarkdownNote`
- `LTXVImgToVideoInplaceKJ`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `MarkdownNote`
- `ImageResize+`
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `PrimitiveInt`
- `ImageResize+`
- `SaveVideo`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `CLIPTextEncode` ★核心
- `FloatConstant`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **85%**（50/59）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`LTXVConditioning`、`RandomNoise`、`LTXAVTextEncoderLoader`、`CLIPTextEncode`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`CreateVideo`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`ComfyMathExpression`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`SimpleMath+`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`ImageResize+`、`SaveVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`FloatConstant`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
