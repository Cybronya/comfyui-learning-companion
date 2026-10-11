---
key: 视频生成/文生视频/LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482.json
name: LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482.json
hash: a04d93f91becc8ed
coverage: 0.612245
learned_at: 2026-10-11 20:21:27
nodes: [LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, SetNode, ConditioningZeroOut, SamplerCustom, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplaceKJ, SetNode, DF_Int_to_Float, GetNode, StringFunction|pysssss, UNETLoader, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, ModelSamplingSD3, AILab_QwenVL_Advanced, LayerUtility: If , LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, SimpleMath+, JjkText, ShowText|pysssss, PrimitiveInt, Int, PrimitiveInt, PrimitiveInt, VHS_VideoCombine, LoadImage, LTXVPreprocess, ImageResizeKJv2, easy positive]
patterns: []
missing: [LayerUtility: BooleanOperatorV2, LayerUtility: If , LayerUtility: NumberCalculatorV2, SimpleMath+, StringFunction|pysssss, easy positive]
parameters: {"batch_size": 1, "height": 24, "width": 305}
discoveries: [次要节点 `LayerUtility: BooleanOperatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频KJ版 音画同步+提示词润色_2070637012666900482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（49 个）：
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAELoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `SetNode`
- `ConditioningZeroOut`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `DF_Int_to_Float`
- `GetNode`
- `StringFunction|pysssss`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `AILab_QwenVL_Advanced`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `JjkText`
- `ShowText|pysssss`
- `PrimitiveInt`
- `Int`
- `PrimitiveInt`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LoadImage`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `easy positive`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **61%**（30/49）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`ConditioningZeroOut`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`UNETLoader`、`DualCLIPLoader`、`ModelSamplingSD3`、`AILab_QwenVL_Advanced`、`Int`、`VHS_VideoCombine`、`LoadImage`、`LTXVPreprocess`、`ImageResizeKJv2`

**缺卡**（6）：`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`StringFunction|pysssss`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

## 学习发现

- 次要节点 `LayerUtility: BooleanOperatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
