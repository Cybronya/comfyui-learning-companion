---
key: 视频生成/图生视频/LTX-2.3_动作参考并保持脸部一致性_2048694979278671873.json
name: LTX-2.3_动作参考并保持脸部一致性_2048694979278671873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.3_动作参考并保持脸部一致性_2048694979278671873.json
hash: cbd4af924807e60d
coverage: 0.704082
learned_at: 2026-10-15 22:37:10
nodes: [LTXVEmptyLatentAudio, SamplerCustomAdvanced, KSamplerSelect, LTXVAudioVAEDecode, VAEDecodeTiled, CannyEdgePreprocessor, DWPreprocessor, DepthAnythingPreprocessor, RandomNoise, LTXVImgToVideoConditionOnly, SetNode, SetNode, EmptyLTXVLatentVideo, SimpleMath+, PrimitiveBoolean, GetNode, GetNode, KSamplerSelect, ManualSigmas, RandomNoise, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, GetNode, LTXVImgToVideoInplace, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, VHS_VideoInfo, CFGGuider, RandomNoise, VHS_VideoCombine, LTXVConcatAVLatent, GetNode, LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, INTConstant, INTConstant, SetNode, LTXVConcatAVLatent, GetImageSize, ImageResizeKJv2, SetNode, SetNode, SimpleMath+, GetNode, GetNode, SetNode, ManualSigmas, SetNode, LTXAddVideoICLoRAGuide, SetNode, UNETLoader, LTXVCropGuides, GetNode, GetNode, GetNode, VHS_VideoCombine, VAEDecodeTiled, RTXVideoSuperResolution, ComfyMathExpression, LTXVAudioVAEDecode, SimpleMath+, SimpleMath+, LatentUpscaleModelLoader, LTXVImgToVideoInplace, SamplerCustomAdvanced, VHS_LoadVideo, ImageResizeKJv2, LoadImage, Label (rgthree), LTXVLatentUpsampler, GetNode, GetNode, Label (rgthree), DualCLIPLoader, CFGGuider, LoraLoaderModelOnly, LTXICLoRALoaderModelOnly, CLIPTextEncode, LTXVConditioning, SetNode, VHS_VideoCombine, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3_动作参考并保持脸部一致性_2048694979278671873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048694979278671873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（98 个）：
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CannyEdgePreprocessor`
- `DWPreprocessor`
- `DepthAnythingPreprocessor`
- `RandomNoise`
- `LTXVImgToVideoConditionOnly`
- `SetNode`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `PrimitiveBoolean`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `VHS_VideoInfo`
- `CFGGuider`
- `RandomNoise`
- `VHS_VideoCombine`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetImageSize`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `SetNode`
- `LTXAddVideoICLoRAGuide`
- `SetNode`
- `UNETLoader` ★核心
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `RTXVideoSuperResolution`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `LoadImage`
- `Label (rgthree)`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `DualCLIPLoader`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SetNode`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（69/98）

**有卡**：`LTXVEmptyLatentAudio`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CannyEdgePreprocessor`、`DWPreprocessor`、`DepthAnythingPreprocessor`、`RandomNoise`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`PrimitiveBoolean`、`ManualSigmas`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`VAELoaderKJ`、`ImageResizeKJv2`、`VHS_VideoInfo`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`INTConstant`、`GetImageSize`、`LTXAddVideoICLoRAGuide`、`UNETLoader`、`RTXVideoSuperResolution`、`ComfyMathExpression`、`LatentUpscaleModelLoader`、`VHS_LoadVideo`、`LoadImage`、`Label (rgthree)`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LTXICLoRALoaderModelOnly`、`CLIPTextEncode`、`LTXVConditioning`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、DepthAnythingPreprocessor、CannyEdgePreprocessor、CFGGuider、KSamplerSelect
