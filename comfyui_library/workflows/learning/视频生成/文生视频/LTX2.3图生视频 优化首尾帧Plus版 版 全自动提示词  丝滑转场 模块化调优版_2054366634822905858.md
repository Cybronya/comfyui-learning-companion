---
key: 视频生成/文生视频/LTX2.3图生视频 优化首尾帧Plus版 版 全自动提示词  丝滑转场 模块化调优版_2054366634822905858.json
name: LTX2.3图生视频 优化首尾帧Plus版 版 全自动提示词  丝滑转场 模块化调优版_2054366634822905858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频 优化首尾帧Plus版 版 全自动提示词  丝滑转场 模块化调优版_2054366634822905858.json
hash: de98dca44b371b26
coverage: 0.555556
learned_at: 2026-10-11 19:49:38
nodes: [LTXVConcatAVLatent, CFGGuider, LTXVConditioning, LTXVLatentUpsampler, LatentUpscaleModelLoader, VAELoaderKJ, LTXVSeparateAVLatent, LTXVImgToVideoInplace, CFGGuider, VAELoaderKJ, KSamplerSelect, KSamplerSelect, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, SetNode, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, ImageResizeKJv2, ResizeImagesByLongerEdge, LayerUtility: BooleanOperator, PrimitiveBoolean, SetNode, SetNode, ComfyMathExpression, LTXVConcatAVLatent, Image Stitch, GetNode, GetNode, SimpleMath+, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, GetNode, SetNode, LayerUtility: If , SetNode, GetNode, GetNode, ManualSigmas, ManualSigmas, RandomNoise, LTXVSeparateAVLatent, SamplerCustomAdvanced, ResizeImagesByLongerEdge, GetNode, ShowText|pysssss, VAEDecodeTiled, SetNode, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, ComfyMathExpression, PrimitiveInt, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, ResizeImageMaskNode, LTXVCropGuides, RandomNoise, CLIPTextEncode, CLIPTextEncode, easy positive, ImageScaleDownToSize, LTXVPreprocess, LTXVPreprocess, SamplerCustomAdvanced, PrimitiveInt, SetNode, LTX2_NAG, LTXVAddGuideMulti, SimpleMath+, GetNode, GetNode, LayerUtility: PurgeVRAM, AILab_QwenVL_Advanced, DualCLIPLoader, UNETLoader, PrimitiveInt, VHS_VideoCombine, Note, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, Fast Groups Bypasser (rgthree), LoadImage, LoadImage]
patterns: []
missing: [Image Stitch, LayerUtility: BooleanOperator, LayerUtility: If , LayerUtility: PurgeVRAM, SimpleMath+, SimpleMath+, easy positive]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `Image Stitch` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: BooleanOperator` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3图生视频 优化首尾帧Plus版 版 全自动提示词  丝滑转场 模块化调优版_2054366634822905858.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频 优化首尾帧Plus版 版 全自动提示词  丝滑转场 模块化调优版_2054366634822905858.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（90 个）：
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
- `AILab_QwenVL_Advanced`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `VHS_VideoCombine`
- `Note`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **56%**（50/90）

**有卡**：`LTXVConcatAVLatent`、`CFGGuider`、`LTXVConditioning`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`LTXVSeparateAVLatent`、`LTXVImgToVideoInplace`、`KSamplerSelect`、`ComfyMathExpression`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`ResizeImagesByLongerEdge`、`PrimitiveBoolean`、`ManualSigmas`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ResizeImageMaskNode`、`LTXVCropGuides`、`CLIPTextEncode`、`ImageScaleDownToSize`、`LTXVPreprocess`、`LTX2_NAG`、`LTXVAddGuideMulti`、`AILab_QwenVL_Advanced`、`DualCLIPLoader`、`UNETLoader`、`VHS_VideoCombine`、`LoadImage`

**缺卡**（7）：`Image Stitch`、`LayerUtility: BooleanOperator`、`LayerUtility: If `、`LayerUtility: PurgeVRAM`、`SimpleMath+`、`SimpleMath+`、`easy positive`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `Image Stitch` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: BooleanOperator` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
