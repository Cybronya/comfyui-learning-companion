---
key: 数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json
name: LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json
hash: dda2190d0a17f4f9
coverage: 0.46281
learned_at: 2026-10-18 19:07:41
nodes: [GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LoraLoaderModelOnly, VAELoaderKJ, VAELoaderKJ, LoraLoaderModelOnly, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, ImageResizeKJv2, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LoadAudio, Seed (rgthree), SetNode, Note, ManualSigmas, SetNode, LTXVPreprocess, KSamplerSelect, ManualSigmas, VAEDecodeTiled, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, LTXVEmptyLatentAudio, LTXVConcatAVLatent, EmptyLTXVLatentVideo, LTXVImgToVideoInplaceKJ, SetNode, SetNode, GetNode, ResizeImageMaskNode, LTXVConditioning, SimpleMath+, GetImageSize, GetNode, SamplerCustom, LayerUtility: PurgeVRAM, LTXVAudioVAEEncode, MelBandRoFormerModelLoader, MelBandRoFormerSampler, SetNode, SolidMask, SimpleMath+, SetLatentNoiseMask, AudioInfo, GetNode, SetNode, SimpleMath+, SetNode, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, KSamplerSelect, GetNode, SimpleMath+, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustom, DiffusionModelLoaderKJ, LoraLoaderModelOnly, DualCLIPLoader, LatentUpscaleModelLoader, VHS_VideoCombine, VHS_VideoCombine, Note, TTResolutionSelector, CLIPTextEncode, CLIPTextEncode, INTConstant, wanBlock_Swap, WanVideoBlockSwap]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3+（图+音频）数字人口播+高清优化版工作流_2083406138854428674.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（121 个）：
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadAudio`
- `Seed (rgthree)`
- `SetNode`
- `Note`
- `ManualSigmas`
- `SetNode`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `LTXVConditioning`
- `SimpleMath+`
- `GetImageSize`
- `GetNode`
- `SamplerCustom` ★核心
- `LayerUtility: PurgeVRAM`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `SolidMask`
- `SimpleMath+`
- `SetLatentNoiseMask`
- `AudioInfo`
- `GetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `GetNode`
- `SimpleMath+`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustom` ★核心
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `TTResolutionSelector`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `INTConstant`
- `wanBlock_Swap`
- `WanVideoBlockSwap`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（56/121）

**有卡**：`LoraLoaderModelOnly`、`VAELoaderKJ`、`ImageResizeKJv2`、`SimpleMath+`、`LoadImage`、`LoadAudio`、`Seed (rgthree)`、`ManualSigmas`、`LTXVPreprocess`、`KSamplerSelect`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`ResizeImageMaskNode`、`LTXVConditioning`、`GetImageSize`、`SamplerCustom`、`LayerUtility: PurgeVRAM`、`LTXVAudioVAEEncode`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`SolidMask`、`SetLatentNoiseMask`、`AudioInfo`、`LTXVLatentUpsampler`、`DiffusionModelLoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`TTResolutionSelector`、`CLIPTextEncode`、`INTConstant`、`wanBlock_Swap`、`WanVideoBlockSwap`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVLatentUpsampler、Seed (rgthree)
