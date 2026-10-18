---
key: 视频生成/图生视频/LTX2.3首尾帧双图生视频-手动提示词版--注释含提示词模板_2051911216334942209.json
name: LTX2.3首尾帧双图生视频-手动提示词版--注释含提示词模板_2051911216334942209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧双图生视频-手动提示词版--注释含提示词模板_2051911216334942209.json
hash: d90ac4ee91baf16a
coverage: 0.885246
learned_at: 2026-10-15 22:37:24
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, PreviewAny, easy showAnything, TextGenerateLTX2Prompt, LTXVConcatAVLatent, LTXVEmptyLatentAudio, CreateVideo, RandomNoise, LTXVCropGuides, SamplerCustomAdvanced, ManualSigmas, LTXVConditioning, LTXVSeparateAVLatent, RandomNoise, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVAudioVAEDecode, VAEDecodeTiled, ModelPatchTorchSettings, LTXVChunkFeedForward, PathchSageAttentionKJ, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVImgToVideoInplace, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVImgToVideoInplaceKJ, easy int, ComfyMathExpression, PrimitiveInt, SimpleMath+, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, FloatConstant, LoadImage, LoadImage, PrimitiveInt, LoraLoaderModelOnly, Note, CR Prompt Text, DualCLIPLoader, SaveVideo, Note, CLIPTextEncode, CLIPTextEncode, Note]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧双图生视频-手动提示词版--注释含提示词模板_2051911216334942209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051911216334942209.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `PreviewAny`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `CreateVideo`
- `RandomNoise`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplaceKJ`
- `easy int`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `FloatConstant`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CR Prompt Text`
- `DualCLIPLoader`
- `SaveVideo`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Note`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **89%**（54/61）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`TextGenerateLTX2Prompt`、`LTXVEmptyLatentAudio`、`CreateVideo`、`RandomNoise`、`LTXVCropGuides`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`LTXVImgToVideoInplace`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`easy int`、`SimpleMath+`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`FloatConstant`、`LoadImage`、`CR Prompt Text`、`DualCLIPLoader`、`SaveVideo`、`CLIPTextEncode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
