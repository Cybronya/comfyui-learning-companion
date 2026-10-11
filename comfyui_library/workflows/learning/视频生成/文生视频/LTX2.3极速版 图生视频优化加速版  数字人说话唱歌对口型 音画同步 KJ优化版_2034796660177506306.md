---
key: 视频生成/文生视频/LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306.json
name: LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306.json
hash: b2d3e0b29a7743bf
coverage: 0.62
learned_at: 2026-10-11 03:48:36
nodes: [LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, SetNode, ConditioningZeroOut, SamplerCustom, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplaceKJ, SetNode, DF_Int_to_Float, GetNode, StringFunction|pysssss, JjkText, UNETLoader, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, ModelSamplingSD3, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, SimpleMath+, ShowText|pysssss, PrimitiveInt, VHS_VideoCombine, PrimitiveInt, easy positive, PrimitiveInt, Int, LoadImage]
patterns: []
missing: [LayerUtility: BooleanOperatorV2, LayerUtility: If , LayerUtility: NumberCalculatorV2, SimpleMath+, StringFunction|pysssss, easy positive]
parameters: {"batch_size": 1, "height": 24, "width": 305}
discoveries: [次要节点 `LayerUtility: BooleanOperatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3极速版 图生视频优化加速版  数字人说话唱歌对口型 音画同步 KJ优化版_2034796660177506306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
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
- `PathchSageAttentionKJ`
- `SetNode`
- `VAELoaderKJ`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `LTXVPreprocess`
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
- `JjkText`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `AILab_QwenVL_Advanced`
- `ImageResizeKJv2`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `ShowText|pysssss`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `PrimitiveInt`
- `easy positive`
- `PrimitiveInt`
- `Int`
- `LoadImage`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（31/50）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ConditioningZeroOut`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`UNETLoader`、`DualCLIPLoader`、`ModelSamplingSD3`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`VHS_VideoCombine`、`Int`、`LoadImage`

**缺卡**（6）：`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`StringFunction|pysssss`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

## 学习发现

- 次要节点 `LayerUtility: BooleanOperatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
