---
key: 视频生成/图生视频/LTX2.3首尾帧+丝滑转场_2086699476626006017.json
name: LTX2.3首尾帧+丝滑转场_2086699476626006017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧+丝滑转场_2086699476626006017.json
hash: c117e2e84597d7b9
coverage: 0.639535
learned_at: 2026-10-16 21:07:15
nodes: [LTXVConcatAVLatent, CFGGuider, LTXVLatentUpsampler, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, VAELoaderKJ, GetNode, SetNode, SetNode, LTX2SamplingPreviewOverride, ResizeImagesByLongerEdge, PrimitiveBoolean, SetNode, SetNode, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, Image Stitch, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, SetNode, LayerUtility: If , SetNode, GetNode, GetNode, ManualSigmas, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ResizeImagesByLongerEdge, GetNode, SetNode, SetNode, LTXVAudioVAEDecode, ComfyMathExpression, PrimitiveInt, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVCropGuides, RandomNoise, ImageScaleDownToSize, LTXVPreprocess, SamplerCustomAdvanced, PrimitiveInt, SetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, DualCLIPLoader, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, easy positive, VAEDecodeTiled, UNETLoader, LoraLoaderModelOnly, LTXVConditioning, SimpleMath+, ShowText|pysssss, KSamplerSelect, KSamplerSelect, LTXVPreprocess, ImageResizeKJv2, ImageResizeKJv2, AILab_QwenVL_Advanced, LayerUtility: BooleanOperator, SetNode, SetNode, GetNode, GetNode, ComfyMathExpression, LTXVAddGuideMulti, PrimitiveInt, VHS_VideoCombine, LoadImage, LoadImage, PrimitiveStringMultiline, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧+丝滑转场_2086699476626006017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧+丝滑转场_2086699476626006017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（86 个）：
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `VAELoaderKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `ResizeImagesByLongerEdge`
- `PrimitiveBoolean`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `Image Stitch`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: If `
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVCropGuides`
- `RandomNoise`
- `ImageScaleDownToSize`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `DualCLIPLoader`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy positive`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `SimpleMath+`
- `ShowText|pysssss`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `AILab_QwenVL_Advanced`
- `LayerUtility: BooleanOperator`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `LTXVAddGuideMulti`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **64%**（55/86）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTX2SamplingPreviewOverride`、`ResizeImagesByLongerEdge`、`PrimitiveBoolean`、`ComfyMathExpression`、`Image Stitch`、`SimpleMath+`、`LayerUtility: If `、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`ImageScaleDownToSize`、`LTXVPreprocess`、`LayerUtility: PurgeVRAM`、`DualCLIPLoader`、`LTX2_NAG`、`CLIPTextEncode`、`easy positive`、`VAEDecodeTiled`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVConditioning`、`KSamplerSelect`、`ImageResizeKJv2`、`AILab_QwenVL_Advanced`、`LayerUtility: BooleanOperator`、`LTXVAddGuideMulti`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
