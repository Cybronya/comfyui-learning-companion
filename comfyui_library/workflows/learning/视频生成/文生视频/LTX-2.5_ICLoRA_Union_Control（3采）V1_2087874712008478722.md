---
key: 视频生成/文生视频/LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722.json
name: LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722.json
hash: 588ec6586d782c71
coverage: 0.555556
learned_at: 2026-10-15 22:44:43
nodes: [KSamplerSelect, ManualSigmas, CFGGuider, GetNode, GetNode, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVSeparateAVLatent, GetNode, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, VAEDecode, GetNode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, SetNode, SetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, SimpleMath+, GetNode, GetNode, LTXVCropGuides, SetNode, LTXVImgToVideoConditionOnly, GetNode, GetNode, SetNode, SetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVConditioning, VAEDecode, LTXVAudioVAEDecode, VHS_VideoInfo, SetNode, SetNode, SetNode, GetNode, LTXVConcatAVLatent, SetNode, SetNode, LTXAddVideoICLoRAGuide, GetNode, SetNode, GetNode, GetNode, GetImageSize, SetNode, SimpleMath+, GetNode, CLIPTextEncode, VHS_VideoCombine, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, CLIPTextEncode, EmptyLTXVLatentVideo, SetNode, CannyEdgePreprocessor, CFGGuider, DWPreprocessor, SetNode, SetNode, GetNode, VHS_VideoCombine, GetNode, RandomNoise, DepthAnythingPreprocessor, ImageResizeKJv2, LatentUpscaleModelLoader, CLIPLoader, VAELoader, VAELoader, UNETLoader, GetNode, GetNode, GetNode, LTXICLoRALoaderModelOnly, SetNode, RandomNoise, MathExpression|pysssss, VHS_VideoCombine, VHS_LoadVideo, Text, INTConstant, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.5_ICLoRA_Union_Control（3采）V1_2087874712008478722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（108 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `SetNode`
- `SetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `SetNode`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `SetNode`
- `CannyEdgePreprocessor`
- `CFGGuider`
- `DWPreprocessor`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `RandomNoise`
- `DepthAnythingPreprocessor`
- `ImageResizeKJv2`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `SetNode`
- `RandomNoise`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Text`
- `INTConstant`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（60/108）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`VAEDecode`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`LTXVImgToVideoConditionOnly`、`LTXVConditioning`、`VHS_VideoInfo`、`LTXAddVideoICLoRAGuide`、`GetImageSize`、`CLIPTextEncode`、`VHS_VideoCombine`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`CannyEdgePreprocessor`、`DWPreprocessor`、`RandomNoise`、`DepthAnythingPreprocessor`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`MathExpression|pysssss`、`VHS_LoadVideo`、`Text`、`INTConstant`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2、DepthAnythingPreprocessor
