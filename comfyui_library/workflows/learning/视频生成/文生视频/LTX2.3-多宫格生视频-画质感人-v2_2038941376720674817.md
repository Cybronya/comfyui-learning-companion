---
key: 视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json
name: LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json
hash: 57273172f57eafca
coverage: 0.951613
learned_at: 2026-10-15 22:45:03
nodes: [ManualSigmas, SamplerCustomAdvanced, RandomNoise, KSamplerSelect, RandomNoise, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageResizeKJv2, ImageResizeKJv2, SimpleMath+, SimpleMath+, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, VAEDecodeTiled, KSamplerSelect, ComfyMathExpression, LTXVConcatAVLatent, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, CFGGuider, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, CFGGuider, Reroute, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEDecode, CLIPTextEncode, GuHaiAutoImageSplit, QZ_ResolutionPreset, SimpleMath+, CLIPTextEncode, LoadImage, ConcatTextOfUtils, LTXVConditioning, ManualSigmas, LTXVAddGuideMulti, SaveImage, ImageResizeKJv2, LoraLoaderModelOnly, RH_LLMAPI_Pro_Node, Int, PrimitiveInt, easy showAnything, ImageResizeKJv2, SaveVideo, SimpleMath+, SimpleMath+, SimpleMath+]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-多宫格生视频-画质感人-v2_2038941376720674817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SimpleMath+`
- `SimpleMath+`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `CFGGuider`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `GuHaiAutoImageSplit`
- `QZ_ResolutionPreset`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ConcatTextOfUtils`
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVAddGuideMulti`
- `SaveImage`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `RH_LLMAPI_Pro_Node`
- `Int`
- `PrimitiveInt`
- `easy showAnything`
- `ImageResizeKJv2`
- `SaveVideo`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（59/62）

**有卡**：`ManualSigmas`、`SamplerCustomAdvanced`、`RandomNoise`、`KSamplerSelect`、`ImageFromBatch`、`ImageResizeKJv2`、`SimpleMath+`、`LTXVPreprocess`、`VAEDecodeTiled`、`ComfyMathExpression`、`LTXVConcatAVLatent`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`CreateVideo`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`GuHaiAutoImageSplit`、`QZ_ResolutionPreset`、`LoadImage`、`ConcatTextOfUtils`、`LTXVConditioning`、`LTXVAddGuideMulti`、`SaveImage`、`LoraLoaderModelOnly`、`RH_LLMAPI_Pro_Node`、`Int`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
