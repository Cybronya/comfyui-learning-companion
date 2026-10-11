---
key: 视频生成/文生视频/ltx2.3 视频编辑工作流 保留原生语音-v2版_2042177519486509057.json
name: ltx2.3 视频编辑工作流 保留原生语音-v2版_2042177519486509057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3 视频编辑工作流 保留原生语音-v2版_2042177519486509057.json
hash: ed1d3408421c525c
coverage: 0.72973
learned_at: 2026-10-11 19:49:44
nodes: [LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, Reroute, VAELoaderKJ, SetNode, SetNode, UNETLoader, KSamplerSelect, SetNode, GetImageSize, easy showAnything, easy showAnything, LTXVPreprocess, ImageScaleBy, LTXVConditioning, SamplerCustomAdvanced, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, CFGGuider, GetNode, CLIPTextEncode, LTXVConcatAVLatent, BasicScheduler, LTXVLatentUpsampler, LTXVAddGuideMulti, CFGGuider, GetNode, LTXVSeparateAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, CreateVideo, SolidMask, LTXVAudioVAEEncode, GetNode, LTXVConcatAVLatent, LTXVAddGuideMulti, VAEEncode, GetNode, GetNode, SetLatentNoiseMask, LTX2SamplingPreviewOverride, VHS_LoadVideo, CLIPTextEncode, QZ_ResolutionPreset, ImageResizeKJv2, SetNode, GetImageSizeAndCount, ImageFromBatch, UNETLoader, LoraLoaderModelOnly, SetNode, PrimitiveInt, SimpleMath+, DF_Int_to_Float, SetNode, SAM3Segment, GrowMaskWithBlur, BlockifyMask, SetNode, DrawMaskOnImage, SetNode, GetNode, LTXVCropGuides, VAEDecodeTiled, GetNode, LTXVAudioVAEDecode, ImageConcanate, Int, SaveVideo, VHS_VideoCombine, RandomNoise, RandomNoise]
patterns: []
missing: [SimpleMath+]
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/ltx2.3 视频编辑工作流 保留原生语音-v2版_2042177519486509057.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3 视频编辑工作流 保留原生语音-v2版_2042177519486509057.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `Reroute`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `SetNode`
- `GetImageSize`
- `easy showAnything`
- `easy showAnything`
- `LTXVPreprocess`
- `ImageScaleBy`
- `LTXVConditioning`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `CFGGuider`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `LTXVLatentUpsampler` ★核心
- `LTXVAddGuideMulti`
- `CFGGuider`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVAddGuideMulti`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `SetLatentNoiseMask`
- `LTX2SamplingPreviewOverride`
- `VHS_LoadVideo`
- `CLIPTextEncode` ★核心
- `QZ_ResolutionPreset`
- `ImageResizeKJv2`
- `SetNode`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `PrimitiveInt`
- `SimpleMath+`
- `DF_Int_to_Float`
- `SetNode`
- `SAM3Segment`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `LTXVCropGuides`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `ImageConcanate`
- `Int`
- `SaveVideo`
- `VHS_VideoCombine`
- `RandomNoise`
- `RandomNoise`

## 知识

覆盖率 **73%**（54/74）

**有卡**：`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`KSamplerSelect`、`GetImageSize`、`LTXVPreprocess`、`ImageScaleBy`、`LTXVConditioning`、`SamplerCustomAdvanced`、`ManualSigmas`、`CFGGuider`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVAddGuideMulti`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`CreateVideo`、`SolidMask`、`LTXVAudioVAEEncode`、`VAEEncode`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`VHS_LoadVideo`、`QZ_ResolutionPreset`、`ImageResizeKJv2`、`GetImageSizeAndCount`、`ImageFromBatch`、`LoraLoaderModelOnly`、`DF_Int_to_Float`、`SAM3Segment`、`GrowMaskWithBlur`、`BlockifyMask`、`DrawMaskOnImage`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`ImageConcanate`、`Int`、`SaveVideo`、`VHS_VideoCombine`、`RandomNoise`

**缺卡**（1）：`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
