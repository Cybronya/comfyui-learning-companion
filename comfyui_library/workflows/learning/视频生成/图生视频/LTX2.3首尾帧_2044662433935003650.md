---
key: 视频生成/图生视频/LTX2.3首尾帧_2044662433935003650.json
name: LTX2.3首尾帧_2044662433935003650.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044662433935003650.json
hash: 1d848de1bd121be9
coverage: 0.647727
learned_at: 2026-10-15 22:36:39
nodes: [LTXVLatentUpsampler, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, VAELoaderKJ, KSamplerSelect, GetNode, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, ResizeImagesByLongerEdge, LayerUtility: BooleanOperator, PrimitiveBoolean, SetNode, SetNode, LTXVConcatAVLatent, GetNode, GetNode, SetNode, LayerUtility: If , SetNode, GetNode, GetNode, ManualSigmas, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, ComfyMathExpression, LTXVCropGuides, RandomNoise, LTXVPreprocess, LTXVPreprocess, SamplerCustomAdvanced, PrimitiveInt, SimpleMath+, GetNode, GetNode, LTX2_NAG, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, SetNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, SetNode, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, RandomNoise, CFGGuider, LTXVAddGuideMulti, LTXVAudioVAEDecode, VAEDecodeTiled, ResizeImageMaskNode, EmptyLTXVLatentVideo, ComfyMathExpression, ImageResizeKJv2, ComfyMathExpression, LatentUpscaleModelLoader, VAELoaderKJ, DualCLIPLoader, LTXVEmptyLatentAudio, SetNode, SetNode, PrimitiveInt, PrimitiveInt, SetNode, SetNode, PrimitiveInt, SimpleMath+, GetNode, GetNode, UNETLoader, AILab_QwenVL_Advanced, LayerUtility: PurgeVRAM, SetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, easy positive, ImageScaleDownToSize, Image Stitch, VHS_VideoCombine, PrimitiveInt, ShowText|pysssss, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧_2044662433935003650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044662433935003650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（88 个）：
- `LTXVLatentUpsampler` ★核心
- `LTXVSeparateAVLatent`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `LayerUtility: BooleanOperator`
- `PrimitiveBoolean`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: If `
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `RandomNoise`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveInt`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `LTX2_NAG`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `AILab_QwenVL_Advanced`
- `LayerUtility: PurgeVRAM`
- `SetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy positive`
- `ImageScaleDownToSize`
- `Image Stitch`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（57/88）

**有卡**：`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`CFGGuider`、`VAELoaderKJ`、`KSamplerSelect`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`LayerUtility: BooleanOperator`、`PrimitiveBoolean`、`LTXVConcatAVLatent`、`LayerUtility: If `、`ManualSigmas`、`ComfyMathExpression`、`LTXVCropGuides`、`RandomNoise`、`LTXVPreprocess`、`SamplerCustomAdvanced`、`SimpleMath+`、`LTX2_NAG`、`LTXVConditioning`、`CLIPTextEncode`、`LTXVAddGuideMulti`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`LTXVEmptyLatentAudio`、`UNETLoader`、`AILab_QwenVL_Advanced`、`LayerUtility: PurgeVRAM`、`easy positive`、`ImageScaleDownToSize`、`Image Stitch`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
