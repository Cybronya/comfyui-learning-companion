---
key: 视频生成/图生视频/LTX2.3_图生视频_多帧_2045362870476607490.json
name: LTX2.3_图生视频_多帧_2045362870476607490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3_图生视频_多帧_2045362870476607490.json
hash: 193822a0dc66a984
coverage: 0.549383
learned_at: 2026-10-15 22:36:46
nodes: [RandomNoise, KSamplerSelect, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, ManualSigmas, GetNode, GetNode, ModelPatchTorchSettings, GetNode, GetNode, CFGGuider, RandomNoise, KSamplerSelect, CFGGuider, ManualSigmas, GetNode, CFGGuider, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, LTXVCropGuides, GetNode, GetNode, LTXVCropGuides, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXVLatentUpsampler, GetNode, GetNode, LTXVImgToVideoConditionOnly, GetNode, SetNode, GetNode, GetNode, ManualSigmas, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, LTXVSeparateAVLatent, GetNode, LTXVSeparateAVLatent, LTXVSeparateAVLatent, SetNode, SamplerCustomAdvanced, easy cleanGpuUsed, SamplerCustomAdvanced, easy cleanGpuUsed, SetNode, SetNode, SamplerCustomAdvanced, easy cleanGpuUsed, CM_FloatToInt, VAEDecodeTiled, VAEDecodeTiled, VAEDecodeTiled, VHS_VideoCombine, VHS_VideoCombine, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, SetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, SetNode, SetNode, SetNode, LTXAVTextEncoderLoader, GetNode, GetNode, SetNode, GetNode, SetNode, VAELoader, SetNode, CLIPTextEncode, SetNode, LTXVConcatAVLatent, math_calculate, math_calculate, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, math_calculate, EmptyLTXVLatentVideo, LTXVImgToVideoConditionOnly, LoadImage, CLIPTextEncode, SetNode, SetNode, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, SetNode, LTXVAudioVAEDecode, GetNode, LTXVAudioVAEDecode, GetNode, LTXVAudioVAEDecode, GetNode, PreviewImage, PreviewImage, LTXVConditioning, LTX2SamplingPreviewOverride, GetNode, LTX2_NAG, GetNode, UNETLoader, LoraLoaderModelOnly, GetNode, GetNode, GetNode, LTXVImgToVideoInplaceKJ, LoraLoader, Int, Float, LoadImage, LoadImage, Float, math_calculate, RandomNoise, ImageResizeKJv2, LTXVPreprocess, SetNode, PreviewImage, LTXVPreprocess, SetNode, LTXVPreprocess, SetNode, ImageResizeKJv2, ResizeImagesByLongerEdge, ImageResizeKJv2, ResizeImagesByLongerEdge, LoraLoaderModelOnly, BOOLConstant, SetNode, Text, ResizeImagesByLongerEdge, VHS_VideoCombine, VHS_VideoCombine, Int, Int, TTResolutionSelector]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/图生视频/LTX2.3_图生视频_多帧_2045362870476607490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045362870476607490.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（162 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `ModelPatchTorchSettings`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ManualSigmas`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `CM_FloatToInt`
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXAVTextEncoderLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `math_calculate`
- `math_calculate`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `math_calculate`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoConditionOnly`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `LTXVConditioning`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LTX2_NAG`
- `GetNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LoraLoader` ★核心
- `Int`
- `Float`
- `LoadImage`
- `LoadImage`
- `Float`
- `math_calculate`
- `RandomNoise`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `SetNode`
- `PreviewImage`
- `LTXVPreprocess`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LoraLoaderModelOnly` ★核心
- `BOOLConstant`
- `SetNode`
- `Text`
- `ResizeImagesByLongerEdge`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `TTResolutionSelector`

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **55%**（89/162）

**有卡**：`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`ModelPatchTorchSettings`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoConditionOnly`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`CM_FloatToInt`、`VAEDecodeTiled`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTXAVTextEncoderLoader`、`VAELoader`、`CLIPTextEncode`、`math_calculate`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LoadImage`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`UNETLoader`、`LTXVImgToVideoInplaceKJ`、`LoraLoader`、`Int`、`Float`、`ImageResizeKJv2`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`BOOLConstant`、`Text`、`TTResolutionSelector`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
