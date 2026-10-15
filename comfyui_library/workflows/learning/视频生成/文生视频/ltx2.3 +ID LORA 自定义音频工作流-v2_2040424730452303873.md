---
key: 视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流-v2_2040424730452303873.json
name: ltx2.3 +ID LORA 自定义音频工作流-v2_2040424730452303873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流-v2_2040424730452303873.json
hash: 4a4063284bec53be
coverage: 0.929825
learned_at: 2026-10-15 22:47:22
nodes: [VAELoaderKJ, VAELoaderKJ, Reroute, CLIPTextEncode, RandomNoise, CFGGuider, SamplerCustomAdvanced, LTXVConditioning, SamplerCustomAdvanced, PrimitiveInt, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, RandomNoise, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVCropGuides, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVSeparateAVLatent, ComfyMathExpression, LTXVImgToVideoInplace, SimpleMath+, SimpleMath+, SimpleMath+, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVConcatAVLatent, ResizeImageMaskNode, ImageResizeKJv2, QZ_ResolutionPreset, MelBandRoFormerModelLoader, MelBandRoFormerSampler, TrimAudioDuration, CLIPTextEncode, ManualSigmas, KSamplerSelect, LoadImage, ModelMemoryUsageFactorOverride, LoraLoaderModelOnly, DualCLIPLoader, UNETLoader, LatentUpscaleModelLoader, LTX2_NAG, LoadAudio, PreviewAudio, Int, PreviewAudio, easy showAnything, RH_LLMAPI_Pro_Node, SetNode, SaveVideo, LoraLoaderModelOnly, LTXVReferenceAudio]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流-v2_2040424730452303873.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 +ID LORA 自定义音频工作流-v2_2040424730452303873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `Reroute`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `CFGGuider`
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
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `ImageResizeKJv2`
- `QZ_ResolutionPreset`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `TrimAudioDuration`
- `CLIPTextEncode` ★核心
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LoadImage`
- `ModelMemoryUsageFactorOverride`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `LTX2_NAG`
- `LoadAudio`
- `PreviewAudio`
- `Int`
- `PreviewAudio`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `SetNode`
- `SaveVideo`
- `LoraLoaderModelOnly` ★核心
- `LTXVReferenceAudio`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（53/57）

**有卡**：`VAELoaderKJ`、`CLIPTextEncode`、`RandomNoise`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`ComfyMathExpression`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImageMaskNode`、`ImageResizeKJv2`、`QZ_ResolutionPreset`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`TrimAudioDuration`、`LoadImage`、`ModelMemoryUsageFactorOverride`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTX2_NAG`、`LoadAudio`、`PreviewAudio`、`Int`、`RH_LLMAPI_Pro_Node`、`SaveVideo`、`LTXVReferenceAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler
