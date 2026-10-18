---
key: 视频生成/图生视频/ltx2.3单采+多图参考_2032437460713611266.json
name: ltx2.3单采+多图参考_2032437460713611266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3单采+多图参考_2032437460713611266.json
hash: f1edde9849ec0632
coverage: 0.8
learned_at: 2026-10-15 22:35:36
nodes: [easy cleanGpuUsed, easy clearCacheAll, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, RH_LLMAPI_Pro_Node, MarkdownNote, PrimitiveStringMultiline, LoraLoaderModelOnly, LTXVReferenceAudio, LoadAudio, easy showAnything, VHS_LoadVideo, SamplerCustomAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, Note, LTXVAudioVAEEncode, SolidMask, PreviewImage, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Reroute, LoadImage, easy cleanGpuUsed, ComfyMathExpression, ManualSigmas, easy float, easy float, KSamplerSelect, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, KSamplerSelect, easy float, LTXVChunkFeedForward, easy float, LTXVAudioVAELoader, LTXAVTextEncoderLoader, VHS_VideoCombine, PrimitiveInt, LoadImage, easy int, ComfyMathExpression, DualCLIPLoader, DualCLIPLoader, LoadImage, TextGenerateLTX2Prompt, ShowText|pysssss, LTXVPreprocess, LoraLoaderModelOnly, easy int, RandomNoise, easy int, easy int, LoadImage, easy int, LoadImage, ImageResize+, easy int, LoadImage, easy int, LoraLoaderModelOnly, SeedVR2VideoUpscaler, UNETLoader, LoraLoaderModelOnly, UNETLoader, PrimitiveInt, PrimitiveInt, PrimitiveInt, VAEDecodeTiled, BasicScheduler, ComfyMathExpression, Note, Note, LTXVPreprocess, Note, Note, LTXVPreprocess, Note, CheckpointLoaderSimple, SetLatentNoiseMask, LTXVPreprocess, CFGGuider, ImageResize+, LoadAudio, ManualSigmas, LTXVConcatAVLatent, LTXVEmptyLatentAudio, TwoWaySwitch, easy int, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, Text Multiline, LTX2_NAG, EmptyLTXVLatentVideo, ComfyMathExpression, LTXVSeparateAVLatent, LTXVAudioVAEDecode, easy cleanGpuUsed, LTXVCropGuides, LTXVAddGuideMulti, LTXVPreprocess, ImageResize+, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, Note, VHS_VideoCombine, PreviewImage, easy float, easy int]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/ltx2.3单采+多图参考_2032437460713611266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032437460713611266.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（115 个）：
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `RH_LLMAPI_Pro_Node`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LTXVReferenceAudio`
- `LoadAudio`
- `easy showAnything`
- `VHS_LoadVideo`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Note`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `LoadImage`
- `easy cleanGpuUsed`
- `ComfyMathExpression`
- `ManualSigmas`
- `easy float`
- `easy float`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `easy float`
- `LTXVChunkFeedForward`
- `easy float`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `LoadImage`
- `easy int`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `DualCLIPLoader`
- `LoadImage`
- `TextGenerateLTX2Prompt`
- `ShowText|pysssss`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `RandomNoise`
- `easy int`
- `easy int`
- `LoadImage`
- `easy int`
- `LoadImage`
- `ImageResize+`
- `easy int`
- `LoadImage`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `SeedVR2VideoUpscaler`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecodeTiled` ★核心
- `BasicScheduler`
- `ComfyMathExpression`
- `Note`
- `Note`
- `LTXVPreprocess`
- `Note`
- `Note`
- `LTXVPreprocess`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `SetLatentNoiseMask`
- `LTXVPreprocess`
- `CFGGuider`
- `ImageResize+`
- `LoadAudio`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `TwoWaySwitch`
- `easy int`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `LTX2_NAG`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `easy cleanGpuUsed`
- `LTXVCropGuides`
- `LTXVAddGuideMulti`
- `LTXVPreprocess`
- `ImageResize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `PreviewImage`
- `easy float`
- `easy int`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（92/115）

**有卡**：`easy cleanGpuUsed`、`easy clearCacheAll`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`RH_LLMAPI_Pro_Node`、`LoraLoaderModelOnly`、`LTXVReferenceAudio`、`LoadAudio`、`VHS_LoadVideo`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVAudioVAEEncode`、`SolidMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ComfyMathExpression`、`ManualSigmas`、`easy float`、`KSamplerSelect`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`LTXVChunkFeedForward`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`easy int`、`DualCLIPLoader`、`TextGenerateLTX2Prompt`、`LTXVPreprocess`、`RandomNoise`、`ImageResize+`、`SeedVR2VideoUpscaler`、`UNETLoader`、`VAEDecodeTiled`、`BasicScheduler`、`CheckpointLoaderSimple`、`SetLatentNoiseMask`、`CFGGuider`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`TwoWaySwitch`、`LTXVConditioning`、`CLIPTextEncode`、`Text Multiline`、`LTX2_NAG`、`EmptyLTXVLatentVideo`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
