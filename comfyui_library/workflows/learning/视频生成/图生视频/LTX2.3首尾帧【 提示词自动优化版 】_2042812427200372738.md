---
key: 视频生成/图生视频/LTX2.3首尾帧【 提示词自动优化版 】_2042812427200372738.json
name: LTX2.3首尾帧【 提示词自动优化版 】_2042812427200372738.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧【 提示词自动优化版 】_2042812427200372738.json
hash: 120674d64339cab8
coverage: 0.881356
learned_at: 2026-10-15 22:36:29
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAELoader, CFGGuider, RandomNoise, LTXAVTextEncoderLoader, ResizeImagesByLongerEdge, LTXVPreprocess, LatentUpscaleModelLoader, CreateVideo, PrimitiveInt, LTXVConcatAVLatent, ComfyMathExpression, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVChunkFeedForward, ModelPatchTorchSettings, LoraLoaderModelOnly, SimpleMath+, LTXVImgToVideoInplaceKJ, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, ComfyMathExpression, PrimitiveInt, PrimitiveInt, Image Resize, ManualSigmas, PrimitiveInt, easy showAnything, CLIPTextEncode, CheckpointLoaderSimple, PathchSageAttentionKJ, Image Resize, CLIPTextEncode, LTXVConditioning, VAEDecodeTiled, RandomNoise, RHHiddenNodes, RH_LLMAPI_Pro_Node, LoadImage, LoadImage, FloatConstant, LoadImage, SaveVideo, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧【 提示词自动优化版 】_2042812427200372738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042812427200372738.json`

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
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `PrimitiveInt`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVChunkFeedForward`
- `ModelPatchTorchSettings`
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `LTXVImgToVideoInplaceKJ`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `Image Resize`
- `ManualSigmas`
- `PrimitiveInt`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `PathchSageAttentionKJ`
- `Image Resize`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `RandomNoise`
- `RHHiddenNodes`
- `RH_LLMAPI_Pro_Node`
- `LoadImage`
- `LoadImage`
- `FloatConstant`
- `LoadImage`
- `SaveVideo`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **88%**（52/59）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVAudioVAELoader`、`RandomNoise`、`LTXAVTextEncoderLoader`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LatentUpscaleModelLoader`、`CreateVideo`、`ComfyMathExpression`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVChunkFeedForward`、`ModelPatchTorchSettings`、`LoraLoaderModelOnly`、`SimpleMath+`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`Image Resize`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`PathchSageAttentionKJ`、`LTXVConditioning`、`VAEDecodeTiled`、`RHHiddenNodes`、`RH_LLMAPI_Pro_Node`、`LoadImage`、`FloatConstant`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
