---
key: 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2044341747362304001.json
name: LTX2.3 _ 双图-首尾帧 优化版_2044341747362304001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044341747362304001.json
hash: b13b08955796394e
coverage: 0.833333
learned_at: 2026-10-15 22:36:37
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAELoader, CFGGuider, LTXVConditioning, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, CLIPTextEncode, ResizeImagesByLongerEdge, LTXVPreprocess, LatentUpscaleModelLoader, CreateVideo, PrimitiveInt, VAEDecodeTiled, CheckpointLoaderSimple, LTXVConcatAVLatent, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVLatentUpsampler, LTXVImgToVideoInplace, FloatConstant, SaveVideo, PathchSageAttentionKJ, LTXVChunkFeedForward, ModelPatchTorchSettings, LoraLoaderModelOnly, ManualSigmas, SimpleMath+, easy showAnything, MarkdownNote, LTXVImgToVideoInplaceKJ, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, LoadImage, RH_LLMAPI_Pro_Node, PrimitiveInt, LoadImage, PrimitiveStringMultiline, MarkdownNote, Reroute, kkResize, kkResize, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2044341747362304001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044341747362304001.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
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
- `RH_LLMAPI_Pro_Node`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `Reroute`
- `kkResize`
- `kkResize`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`LTXVConditioning`、`RandomNoise`、`LTXAVTextEncoderLoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`CreateVideo`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`ComfyMathExpression`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`FloatConstant`、`SaveVideo`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`SimpleMath+`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`kkResize`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
