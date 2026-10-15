---
key: 视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流_2040214667628384257.json
name: ltx2.3 +ID LORA 自定义音频工作流_2040214667628384257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流_2040214667628384257.json
hash: 3a48398214611299
coverage: 0.931034
learned_at: 2026-10-15 22:47:22
nodes: [VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, Int, Reroute, CLIPTextEncode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVConditioning, SamplerCustomAdvanced, PrimitiveInt, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, RandomNoise, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVCropGuides, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, ComfyMathExpression, LTXVImgToVideoInplace, easy cleanGpuUsed, SetNode, easy showAnything, SimpleMath+, SimpleMath+, SimpleMath+, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, MelBandRoFormerSampler, DualCLIPLoader, TrimAudioDuration, LoadAudio, LTX2_NAG, CLIPTextEncode, ResizeImageMaskNode, LTXVReferenceAudio, LoraLoaderModelOnly, UNETLoader, PreviewAudio, PreviewAudio, MelBandRoFormerModelLoader, ModelMemoryUsageFactorOverride, LoraLoaderModelOnly, QZ_ResolutionPreset, ImageResizeKJv2, LoadImage, SaveVideo, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流_2040214667628384257.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流_2040214667628384257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `Int`
- `Reroute`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `RandomNoise`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `easy cleanGpuUsed`
- `SetNode`
- `easy showAnything`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `MelBandRoFormerSampler` ★核心
- `DualCLIPLoader`
- `TrimAudioDuration`
- `LoadAudio`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `ResizeImageMaskNode`
- `LTXVReferenceAudio`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PreviewAudio`
- `PreviewAudio`
- `MelBandRoFormerModelLoader`
- `ModelMemoryUsageFactorOverride`
- `LoraLoaderModelOnly` ★核心
- `QZ_ResolutionPreset`
- `ImageResizeKJv2`
- `LoadImage`
- `SaveVideo`
- `RH_LLMAPI_Pro_Node`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（54/58）

**有卡**：`VAELoaderKJ`、`LatentUpscaleModelLoader`、`Int`、`CLIPTextEncode`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVConcatAVLatent`、`ComfyMathExpression`、`easy cleanGpuUsed`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`MelBandRoFormerSampler`、`DualCLIPLoader`、`TrimAudioDuration`、`LoadAudio`、`LTX2_NAG`、`ResizeImageMaskNode`、`LTXVReferenceAudio`、`LoraLoaderModelOnly`、`UNETLoader`、`PreviewAudio`、`MelBandRoFormerModelLoader`、`ModelMemoryUsageFactorOverride`、`QZ_ResolutionPreset`、`ImageResizeKJv2`、`LoadImage`、`SaveVideo`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
