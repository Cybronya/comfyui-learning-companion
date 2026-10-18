---
key: 视频生成/图生视频/LTX2.3 人物角色丝滑转场 首尾帧+转场优化版！Plus版！_2081282783539982338.json
name: LTX2.3 人物角色丝滑转场 首尾帧+转场优化版！Plus版！_2081282783539982338.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 人物角色丝滑转场 首尾帧+转场优化版！Plus版！_2081282783539982338.json
hash: 7277783f6315e179
coverage: 0.639535
learned_at: 2026-10-15 22:42:21
nodes: [LTXVConcatAVLatent, CFGGuider, LTXVLatentUpsampler, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, VAELoaderKJ, GetNode, SetNode, SetNode, LTX2SamplingPreviewOverride, ResizeImagesByLongerEdge, PrimitiveBoolean, SetNode, SetNode, ComfyMathExpression, LTXVConcatAVLatent, Image Stitch, GetNode, GetNode, SimpleMath+, GetNode, GetNode, GetNode, SetNode, LayerUtility: If , SetNode, GetNode, GetNode, ManualSigmas, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ResizeImagesByLongerEdge, GetNode, SetNode, SetNode, LTXVAudioVAEDecode, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVCropGuides, RandomNoise, ImageScaleDownToSize, LTXVPreprocess, SamplerCustomAdvanced, PrimitiveInt, SetNode, GetNode, GetNode, LayerUtility: PurgeVRAM, DualCLIPLoader, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, easy positive, VAEDecodeTiled, UNETLoader, LoraLoaderModelOnly, LTXVConditioning, SimpleMath+, ShowText|pysssss, KSamplerSelect, KSamplerSelect, LTXVPreprocess, ImageResizeKJv2, ImageResizeKJv2, AILab_QwenVL_Advanced, LayerUtility: BooleanOperator, SetNode, SetNode, GetNode, GetNode, ComfyMathExpression, LTXVAddGuideMulti, PrimitiveInt, LoadImage, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 人物角色丝滑转场 首尾帧+转场优化版！Plus版！_2081282783539982338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2081282783539982338.json`

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
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **64%**（55/86）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`LTX2SamplingPreviewOverride`、`ResizeImagesByLongerEdge`、`PrimitiveBoolean`、`ComfyMathExpression`、`Image Stitch`、`SimpleMath+`、`LayerUtility: If `、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVCropGuides`、`ImageScaleDownToSize`、`LTXVPreprocess`、`LayerUtility: PurgeVRAM`、`DualCLIPLoader`、`LTX2_NAG`、`CLIPTextEncode`、`easy positive`、`VAEDecodeTiled`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXVConditioning`、`KSamplerSelect`、`ImageResizeKJv2`、`AILab_QwenVL_Advanced`、`LayerUtility: BooleanOperator`、`LTXVAddGuideMulti`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
