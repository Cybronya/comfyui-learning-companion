---
key: 视频生成/图生视频/最新LTX2.6首尾帧！首中尾3帧生成视频_2067259559454007298.json
name: 最新LTX2.6首尾帧！首中尾3帧生成视频_2067259559454007298.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067259559454007298.json
hash: 10f7b78114ec6e1f
coverage: 0.666667
learned_at: 2026-10-15 22:40:00
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVAudioVAEDecode, LTXVConditioning, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CFGGuider, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LoraLoaderModelOnly, ShowText|pysssss, GetNode, LayerUtility: If , SetNode, SetNode, SetNode, GetNode, GetNode, LayerUtility: BooleanOperator, SetNode, GetNode, SetNode, SetNode, SimpleMath+, GetNode, SetNode, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, easy positive, Image Stitch, Image Stitch, GetNode, GetNode, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTX2SamplingPreviewOverride, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, VAEDecodeTiled, KSamplerSelect, KSamplerSelect, ShowText|pysssss, EmptyLTXVLatentVideo, ImageScaleDownToSize, AILab_QwenVL_Advanced, ImageResizeKJv2, ResizeImagesByLongerEdge, ComfyMathExpression, ComfyMathExpression, SamplerCustomAdvanced, LTXVConcatAVLatent, PrimitiveInt, PrimitiveInt, LTXVPreprocess, LTXVPreprocess, ResizeImagesByLongerEdge, ImageResizeKJv2, GetNode, SetNode, SetNode, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVAddGuideMulti, GetNode, GetNode, VHS_VideoCombine, ComfyMathExpression, TT_img_enc, SaveImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/最新LTX2.6首尾帧！首中尾3帧生成视频_2067259559454007298.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067259559454007298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（90 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `GetNode`
- `LayerUtility: If `
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: BooleanOperator`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `easy positive`
- `Image Stitch`
- `Image Stitch`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `ShowText|pysssss`
- `EmptyLTXVLatentVideo`
- `ImageScaleDownToSize`
- `AILab_QwenVL_Advanced`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `TT_img_enc`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（60/90）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LayerUtility: If `、`LayerUtility: BooleanOperator`、`SimpleMath+`、`LayerUtility: PurgeVRAM`、`easy positive`、`Image Stitch`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`PrimitiveBoolean`、`VAEDecodeTiled`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`ImageScaleDownToSize`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`ComfyMathExpression`、`LTXVPreprocess`、`LTXVAddGuideMulti`、`VHS_VideoCombine`、`TT_img_enc`、`SaveImage`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
