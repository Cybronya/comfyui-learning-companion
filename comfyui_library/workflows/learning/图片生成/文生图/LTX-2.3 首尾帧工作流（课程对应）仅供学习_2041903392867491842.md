---
key: 图片生成/文生图/LTX-2.3 首尾帧工作流（课程对应）仅供学习_2041903392867491842.json
name: LTX-2.3 首尾帧工作流（课程对应）仅供学习_2041903392867491842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/LTX-2.3 首尾帧工作流（课程对应）仅供学习_2041903392867491842.json
hash: ccb0e0175ed14434
coverage: 0.734043
learned_at: 2026-10-19 22:45:34
nodes: [ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImageMaskNode, PrimitiveNode, LoadImage, Fast Groups Bypasser (rgthree), PreviewAny, PrimitiveNode, Fast Groups Bypasser (rgthree), PrimitiveNode, PrimitiveInt, GetImageSize, PrimitiveNode, PrimitiveNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, EmptyImage, LTXVCropGuides, LTXVScheduler, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, LTXVAudioVAEDecode, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, FL_IntToFloat, ImpactSwitch, ImpactSwitch, GetImageSize, ImpactSwitch, FL_IntToFloat, FL_IntToFloat, FL_Math, FL_Math, VAEDecodeTiled, PrimitiveInt, LTXVImgToVideoInplace, EmptyLTXVLatentVideo, FL_IntToFloat, LTXVConditioning, ResizeImagesByLongerEdge, ImpactSwitch, VHS_VideoCombine, MarkdownNote, KSamplerSelect, ManualSigmas, CR Float To Integer, CR Float To Integer, LTXVSeparateAVLatent, RandomNoise, ImageScaleBy, ImpactSwitch, LTXVLatentUpsampler, ManualSigmas, ImpactSwitch, ImpactSwitch, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), FL_IntToFloat, FL_IntToFloat, VHS_VideoCombine, RIFE VFI, VAELoaderKJ, VAELoaderKJ, LatentUpscaleModelLoader, SetLatentNoiseMask, TrimAudioDuration, LoadAudio, MelBandRoFormerSampler, MelBandRoFormerModelLoader, PrimitiveInt, LTXVAudioVAEEncode, CreateShapeMask, INTConstant, INTConstant, CFGGuider, CFGGuider, DualCLIPLoader, UnetLoaderGGUF, PrimitiveNode, Note, Note, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, LoadImage, LoadImage, ResizeImagesByLongerEdge, PrimitiveInt, LTXVPreprocess, LTXVPreprocess, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 121}
---

# 图片生成/文生图/LTX-2.3 首尾帧工作流（课程对应）仅供学习_2041903392867491842.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/LTX-2.3 首尾帧工作流（课程对应）仅供学习_2041903392867491842.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（94 个）：
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `PrimitiveNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `PrimitiveNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveNode`
- `PrimitiveInt`
- `GetImageSize`
- `PrimitiveNode`
- `PrimitiveNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `EmptyImage`
- `LTXVCropGuides`
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `FL_IntToFloat`
- `ImpactSwitch`
- `ImpactSwitch`
- `GetImageSize`
- `ImpactSwitch`
- `FL_IntToFloat`
- `FL_IntToFloat`
- `FL_Math`
- `FL_Math`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `LTXVImgToVideoInplace`
- `EmptyLTXVLatentVideo`
- `FL_IntToFloat`
- `LTXVConditioning`
- `ResizeImagesByLongerEdge`
- `ImpactSwitch`
- `VHS_VideoCombine`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CR Float To Integer`
- `CR Float To Integer`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `ImageScaleBy`
- `ImpactSwitch`
- `LTXVLatentUpsampler` ★核心
- `ManualSigmas`
- `ImpactSwitch`
- `ImpactSwitch`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `FL_IntToFloat`
- `FL_IntToFloat`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `SetLatentNoiseMask`
- `TrimAudioDuration`
- `LoadAudio`
- `MelBandRoFormerSampler` ★核心
- `MelBandRoFormerModelLoader`
- `PrimitiveInt`
- `LTXVAudioVAEEncode` ★核心
- `CreateShapeMask`
- `INTConstant`
- `INTConstant`
- `CFGGuider`
- `CFGGuider`
- `DualCLIPLoader`
- `UnetLoaderGGUF` ★核心
- `PrimitiveNode`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `PrimitiveInt`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `121`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（69/94）

**有卡**：`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ResizeImageMaskNode`、`LoadImage`、`GetImageSize`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`EmptyImage`、`LTXVCropGuides`、`LTXVScheduler`、`LTXVImgToVideoInplace`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`FL_IntToFloat`、`FL_Math`、`VAEDecodeTiled`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`VHS_VideoCombine`、`ManualSigmas`、`CR Float To Integer`、`ImageScaleBy`、`LTXVLatentUpsampler`、`RIFE VFI`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`SetLatentNoiseMask`、`TrimAudioDuration`、`LoadAudio`、`MelBandRoFormerSampler`、`MelBandRoFormerModelLoader`、`LTXVAudioVAEEncode`、`CreateShapeMask`、`INTConstant`、`CFGGuider`、`DualCLIPLoader`、`UnetLoaderGGUF`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、MelBandRoFormerSampler、LTXVLatentUpsampler
