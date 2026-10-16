---
key: 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2033156764371263490.json
name: LTX2.3 _ 双图-首尾帧 优化版_2033156764371263490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033156764371263490.json
hash: 153393f93e37c356
coverage: 0.847458
learned_at: 2026-10-15 22:35:38
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAELoader, CFGGuider, LTXVConditioning, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, CLIPTextEncode, ResizeImagesByLongerEdge, LTXVPreprocess, LatentUpscaleModelLoader, CreateVideo, PrimitiveInt, VAEDecodeTiled, CheckpointLoaderSimple, LTXVConcatAVLatent, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVLatentUpsampler, LTXVImgToVideoInplace, FloatConstant, SaveVideo, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, LoraLoaderModelOnly, Resize, ManualSigmas, SimpleMath+, easy showAnything, MarkdownNote, LTXVImgToVideoInplaceKJ, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LoadImage, Resize, RH_LLMAPI_Pro_Node, PrimitiveInt, LoadImage, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2033156764371263490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033156764371263490.json`

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
- `CLIPTextEncode` ★核心
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
- `ResizeImagesByLongerEdge`
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
- `FloatConstant`
- `SaveVideo`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `Resize`
- `ManualSigmas`
- `SimpleMath+`
- `easy showAnything`
- `MarkdownNote`
- `LTXVImgToVideoInplaceKJ`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LoadImage`
- `Resize`
- `RH_LLMAPI_Pro_Node`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **85%**（50/59）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`LTXVConditioning`、`RandomNoise`、`LTXAVTextEncoderLoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`CreateVideo`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`ComfyMathExpression`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`FloatConstant`、`SaveVideo`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`Resize`、`SimpleMath+`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
