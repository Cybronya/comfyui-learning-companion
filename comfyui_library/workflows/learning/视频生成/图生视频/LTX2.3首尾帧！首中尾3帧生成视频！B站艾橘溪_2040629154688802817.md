---
key: 视频生成/图生视频/LTX2.3首尾帧！首中尾3帧生成视频！B站艾橘溪_2040629154688802817.json
name: LTX2.3首尾帧！首中尾3帧生成视频！B站艾橘溪_2040629154688802817.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2040629154688802817.json
hash: 53e8f36a6587823e
coverage: 0.651685
learned_at: 2026-10-15 22:36:15
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, ManualSigmas, CFGGuider, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVAudioVAEDecode, ComfyMathExpression, LTXVConditioning, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CFGGuider, UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LoraLoaderModelOnly, Note, ShowText|pysssss, GetNode, LayerUtility: If , SetNode, SetNode, SetNode, GetNode, GetNode, LayerUtility: BooleanOperator, SetNode, GetNode, SetNode, SetNode, SimpleMath+, GetNode, SetNode, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM, easy positive, Image Stitch, Image Stitch, GetNode, GetNode, PrimitiveInt, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, LTX2SamplingPreviewOverride, LTX2_NAG, CLIPTextEncode, CLIPTextEncode, PrimitiveBoolean, VAEDecodeTiled, KSamplerSelect, KSamplerSelect, PrimitiveStringMultiline, ShowText|pysssss, EmptyLTXVLatentVideo, ImageScaleDownToSize, AILab_QwenVL_Advanced, ImageResizeKJv2, ResizeImagesByLongerEdge, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, SamplerCustomAdvanced, LTXVConcatAVLatent, PrimitiveInt, PrimitiveInt, LTXVPreprocess, LTXVPreprocess, ResizeImagesByLongerEdge, ImageResizeKJv2, GetNode, SetNode, LoadImage, SetNode, LoadImage, LoadImage, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVAddGuideMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3首尾帧！首中尾3帧生成视频！B站艾橘溪_2040629154688802817.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2040629154688802817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（89 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
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
- `Note`
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
- `VHS_VideoCombine`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`
- `ShowText|pysssss`
- `EmptyLTXVLatentVideo`
- `ImageScaleDownToSize`
- `AILab_QwenVL_Advanced`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
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
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVAddGuideMulti`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（58/89）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`ManualSigmas`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`ComfyMathExpression`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LatentUpscaleModelLoader`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LayerUtility: If `、`LayerUtility: BooleanOperator`、`SimpleMath+`、`LayerUtility: PurgeVRAM`、`easy positive`、`Image Stitch`、`VHS_VideoCombine`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`PrimitiveBoolean`、`VAEDecodeTiled`、`KSamplerSelect`、`EmptyLTXVLatentVideo`、`ImageScaleDownToSize`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoadImage`、`LTXVAddGuideMulti`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
