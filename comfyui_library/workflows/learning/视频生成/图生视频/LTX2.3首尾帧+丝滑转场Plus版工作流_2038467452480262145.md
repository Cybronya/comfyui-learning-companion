---
key: 视频生成/图生视频/LTX2.3首尾帧+丝滑转场Plus版工作流_2038467452480262145.json
name: LTX2.3首尾帧+丝滑转场Plus版工作流_2038467452480262145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3首尾帧+丝滑转场Plus版工作流_2038467452480262145.json
hash: 014e614ce9ed2ce0
coverage: 0.647727
learned_at: 2026-10-15 22:36:02
nodes: [LTXVConcatAVLatent, CFGGuider, LTXVConditioning, LTXVLatentUpsampler, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, VAELoaderKJ, KSamplerSelect, KSamplerSelect, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, SetNode, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, ImageResizeKJv2, ResizeImagesByLongerEdge, LayerUtility: BooleanOperator, PrimitiveBoolean, SetNode, SetNode, PrimitiveInt, ComfyMathExpression, LTXVConcatAVLatent, Image Stitch, GetNode, GetNode, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, GetNode, SetNode, LayerUtility: If , SetNode, GetNode, GetNode, ManualSigmas, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ResizeImagesByLongerEdge, GetNode, ShowText|pysssss, VAEDecodeTiled, SetNode, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, ComfyMathExpression, PrimitiveInt, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ResizeImageMaskNode, LTXVCropGuides, RandomNoise, CLIPTextEncode, CLIPTextEncode, easy positive, ImageScaleDownToSize, LTXVPreprocess, LTXVPreprocess, SamplerCustomAdvanced, PrimitiveInt, SetNode, LTX2_NAG, LTXVAddGuideMulti, SimpleMath+, GetNode, GetNode, LayerUtility: PurgeVRAM, VHS_VideoCombine, PrimitiveInt, PrimitiveInt, AILab_QwenVL_Advanced, DualCLIPLoader, UNETLoader, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧+丝滑转场Plus版工作流_2038467452480262145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038467452480262145.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（88 个）：
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXVConditioning`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `LayerUtility: BooleanOperator`
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
- `ImageResizeKJv2`
- `ImageResizeKJv2`
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
- `ShowText|pysssss`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImageMaskNode`
- `LTXVCropGuides`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy positive`
- `ImageScaleDownToSize`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `SetNode`
- `LTX2_NAG`
- `LTXVAddGuideMulti`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `PrimitiveInt`
- `AILab_QwenVL_Advanced`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（57/88）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`ComfyMathExpression`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`LayerUtility: BooleanOperator`、`PrimitiveBoolean`、`Image Stitch`、`SimpleMath+`、`LayerUtility: If `、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImageMaskNode`、`LTXVCropGuides`、`CLIPTextEncode`、`easy positive`、`ImageScaleDownToSize`、`LTXVPreprocess`、`LTX2_NAG`、`LTXVAddGuideMulti`、`LayerUtility: PurgeVRAM`、`VHS_VideoCombine`、`AILab_QwenVL_Advanced`、`DualCLIPLoader`、`UNETLoader`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
