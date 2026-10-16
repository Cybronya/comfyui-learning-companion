---
key: 视频生成/图生视频/LTX2.5首尾帧图生视频_2087801270798217218.json
name: LTX2.5首尾帧图生视频_2087801270798217218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧图生视频_2087801270798217218.json
hash: a2f3ce9cbf286016
coverage: 0.826923
learned_at: 2026-10-16 21:27:37
nodes: [LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, LTXVAddGuide, ManualSigmas, LTXVAddGuide, LTXVEmptyLatentAudio, LTXVCropGuides, EmptyLTXVLatentVideo, LTXVConditioning, SamplerEulerAncestral, LTXVDualCFGGuider, RandomNoise, CLIPTextEncode, CLIPTextEncode, GetImageSize, LTXVPreprocess, LTXVPreprocess, ResizeImageMaskNode, UNETLoader, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, PrimitiveInt, ComfyMathExpression, PrimitiveInt, SamplerCustomAdvanced, LTXVSeparateAVLatent, CR Text, VHS_VideoCombine, ReversalCaptionOptions, easy showAnything, Dapao_LlamaCaptionOptions, LatentUpscaleModelLoader, LTXVLatentUpsampler, TrimVideoLatent, Fast Groups Bypasser (rgthree), Dapao_LlamaCaption, PrimitiveInt, ResizeImageMaskNode, PrimitiveInt, ResolutionSelector, ReversalLlamaCaption, easy showAnything, Fast Groups Bypasser (rgthree), easy promptConcat, CR Text, LoadImage, LoadImage, RHLLMChatNode, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.5首尾帧图生视频_2087801270798217218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5首尾帧图生视频_2087801270798217218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（52 个）：
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVAddGuide`
- `ManualSigmas`
- `LTXVAddGuide`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SamplerEulerAncestral` ★核心
- `LTXVDualCFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CR Text`
- `VHS_VideoCombine`
- `ReversalCaptionOptions`
- `easy showAnything`
- `Dapao_LlamaCaptionOptions`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `TrimVideoLatent`
- `Fast Groups Bypasser (rgthree)`
- `Dapao_LlamaCaption`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `ResolutionSelector`
- `ReversalLlamaCaption`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `easy promptConcat`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `RHLLMChatNode`
- `easy showAnything`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（43/52）

**有卡**：`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVAddGuide`、`ManualSigmas`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`SamplerEulerAncestral`、`LTXVDualCFGGuider`、`RandomNoise`、`CLIPTextEncode`、`GetImageSize`、`LTXVPreprocess`、`ResizeImageMaskNode`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`CR Text`、`VHS_VideoCombine`、`ReversalCaptionOptions`、`Dapao_LlamaCaptionOptions`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`TrimVideoLatent`、`Dapao_LlamaCaption`、`ResolutionSelector`、`ReversalLlamaCaption`、`easy promptConcat`、`LoadImage`、`RHLLMChatNode`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、SamplerEulerAncestral
