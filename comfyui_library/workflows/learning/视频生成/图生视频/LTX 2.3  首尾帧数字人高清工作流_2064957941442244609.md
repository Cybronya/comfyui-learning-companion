---
key: 视频生成/图生视频/LTX 2.3  首尾帧数字人高清工作流_2064957941442244609.json
name: LTX 2.3  首尾帧数字人高清工作流_2064957941442244609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3  首尾帧数字人高清工作流_2064957941442244609.json
hash: 99de11eb314520d9
coverage: 0.460938
learned_at: 2026-10-15 22:39:32
nodes: [SetNode, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, SolidMask, SetNode, SetNode, SetNode, MelBandRoFormerSampler, SetNode, PreviewAudio, GetNode, GetNode, GetNode, GetNode, GetNode, SimpleMath+, SetNode, GetNode, GetNode, INTConstant, GetNode, GetNode, GetNode, GetNode, SamplerCustom, KSamplerSelect, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVLatentUpsampler, GetNode, SetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVConditioning, SetNode, ImageResizeKJv2, GetImageSize, SetNode, GetNode, ImageFlip, VAEDecodeTiled, LTXVConcatAVLatent, SetNode, LTXVEmptyLatentAudio, GetNode, CLIPTextEncode, Seed (rgthree), SetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, KSamplerSelect, VHS_VideoCombine, GetNode, GetNode, LTXVSeparateAVLatent, GetNode, SetNode, VAEDecodeTiled, GetNode, ImageResizeKJv2, ResizeImageMaskNode, GetNode, PreviewAudio, ImageFlip, GetNode, LTXVPreprocess, GetNode, SimpleMath+, AudioInfo, SimpleMath+, GetNode, Display Any (rgthree), VAELoaderKJ, VAELoaderKJ, LTXVImgToVideoInplaceKJ, ManualSigmas, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, GetNode, GetNode, GetNode, GetNode, SimpleMath+, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, MelBandRoFormerModelLoader, DualCLIPLoader, SamplerCustom, ManualSigmas, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, INTConstant, INTConstant, SetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, GetNode, VHS_VideoCombine, GetNode, GetNode, DiffusionModelLoaderKJ, LoadImage, LoadAudio, PrimitiveStringMultiline, MarkdownNote, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 视频生成/图生视频/LTX 2.3  首尾帧数字人高清工作流_2064957941442244609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064957941442244609.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（128 个）：
- `SetNode`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `SolidMask`
- `SetNode`
- `SetNode`
- `SetNode`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `PreviewAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
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
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `SetNode`
- `ImageResizeKJv2`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `ImageFlip`
- `VAEDecodeTiled` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `Seed (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `GetNode`
- `PreviewAudio`
- `ImageFlip`
- `GetNode`
- `LTXVPreprocess`
- `GetNode`
- `SimpleMath+`
- `AudioInfo`
- `SimpleMath+`
- `GetNode`
- `Display Any (rgthree)`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVImgToVideoInplaceKJ`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `MelBandRoFormerModelLoader`
- `DualCLIPLoader`
- `SamplerCustom` ★核心
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `DiffusionModelLoaderKJ`
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（59/128）

**有卡**：`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`SolidMask`、`MelBandRoFormerSampler`、`PreviewAudio`、`SimpleMath+`、`INTConstant`、`SamplerCustom`、`KSamplerSelect`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`ImageResizeKJv2`、`GetImageSize`、`ImageFlip`、`VAEDecodeTiled`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`CLIPTextEncode`、`Seed (rgthree)`、`VHS_VideoCombine`、`ResizeImageMaskNode`、`LTXVPreprocess`、`AudioInfo`、`Display Any (rgthree)`、`VAELoaderKJ`、`LTXVImgToVideoInplaceKJ`、`ManualSigmas`、`LatentUpscaleModelLoader`、`MelBandRoFormerModelLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`DiffusionModelLoaderKJ`、`LoadImage`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustom、MelBandRoFormerSampler、LTXVLatentUpsampler、Seed (rgthree)
