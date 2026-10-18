---
key: 视频生成/图生视频/LTX2.3首尾帧+丝滑转场！优化版！B站艾橘溪_2038230398714519554.json
name: LTX2.3首尾帧+丝滑转场！优化版！B站艾橘溪_2038230398714519554.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧+丝滑转场！优化版！B站艾橘溪_2038230398714519554.json
hash: 6cd12116eea7398a
coverage: 0.632184
learned_at: 2026-10-15 22:36:01
nodes: [LTXVConcatAVLatent, CFGGuider, LTXVLatentUpsampler, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, VAELoaderKJ, GetNode, SetNode, SetNode, LTX2SamplingPreviewOverride, ResizeImagesByLongerEdge, PrimitiveBoolean, SetNode, SetNode, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, Image Stitch, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, SetNode, LayerUtility: If , SetNode, GetNode, GetNode, ManualSigmas, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ResizeImagesByLongerEdge, GetNode, SetNode, SetNode, LTXVAudioVAEDecode, ComfyMathExpression, PrimitiveInt, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVCropGuides, RandomNoise, ImageScaleDownToSize, LTXVPreprocess, SamplerCustomAdvanced, PrimitiveInt, SetNode, GetNode, GetNode, Note, LayerUtility: PurgeVRAM, VHS_VideoCombine, DualCLIPLoader, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, PrimitiveInt, easy positive, VAEDecodeTiled, UNETLoader, LoraLoaderModelOnly, LTXVConditioning, SimpleMath+, ShowText|pysssss, PrimitiveInt, KSamplerSelect, KSamplerSelect, LTXVPreprocess, PrimitiveStringMultiline, ImageResizeKJv2, ImageResizeKJv2, AILab_QwenVL_Advanced, LayerUtility: BooleanOperator, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, ComfyMathExpression, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧+丝滑转场！优化版！B站艾橘溪_2038230398714519554.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038230398714519554.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（87 个）：
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
- `Note`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `DualCLIPLoader`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `easy positive`
- `VAEDecodeTiled` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `SimpleMath+`
- `ShowText|pysssss`
- `PrimitiveInt`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `AILab_QwenVL_Advanced`
- `LayerUtility: BooleanOperator`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（55/87）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTX2SamplingPreviewOverride`、`ResizeImagesByLongerEdge`、`PrimitiveBoolean`、`ComfyMathExpression`、`Image Stitch`、`SimpleMath+`、`LayerUtility: If `、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`ImageScaleDownToSize`、`LTXVPreprocess`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`DualCLIPLoader`、`LTX2_NAG`、`CLIPTextEncode`、`easy positive`、`VAEDecodeTiled`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVConditioning`、`KSamplerSelect`、`ImageResizeKJv2`、`AILab_QwenVL_Advanced`、`LayerUtility: BooleanOperator`、`LoadImage`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
