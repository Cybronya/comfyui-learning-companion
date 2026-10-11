---
key: 视频生成/文生视频/LTX2.3+双人_单人对话+动作真实自然+极速生视频+KJ优化版+图生视频音画同步_2073621545691475970.json
name: LTX2.3+双人_单人对话+动作真实自然+极速生视频+KJ优化版+图生视频音画同步_2073621545691475970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3+双人_单人对话+动作真实自然+极速生视频+KJ优化版+图生视频音画同步_2073621545691475970.json
hash: dc5efccba21d8f53
coverage: 0.551724
learned_at: 2026-10-11 20:38:34
nodes: [GetNode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, SetNode, VAELoaderKJ, BasicScheduler, SetNode, SetNode, StringFunction|pysssss, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, PathchSageAttentionKJ, KSamplerSelect, LayerUtility: NumberCalculatorV2, SimpleMath+, PrimitiveStringMultiline, JoinStrings, EmptyLTXVLatentVideo, ModelSamplingSD3, UNETLoader, LTX2_NAG, LTXVPreprocess, SamplerCustom, SetNode, VAEDecode, LTXVConcatAVLatent, LTXVAudioVAEDecode, SetNode, GetNode, DF_Int_to_Float, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, JjkText, PrimitiveInt, LTXVImgToVideoInplaceKJ, GetNode, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, VHS_VideoCombine, ShowText|pysssss, Int, PrimitiveInt, PrimitiveInt, easy positive, LoadImage, MarkdownNote, MarkdownNote]
patterns: []
missing: [LayerUtility: BooleanOperatorV2, LayerUtility: If , LayerUtility: NumberCalculatorV2, SimpleMath+, StringFunction|pysssss, easy positive]
parameters: {"batch_size": 1, "height": 24, "width": 305}
discoveries: [次要节点 `LayerUtility: BooleanOperatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3+双人_单人对话+动作真实自然+极速生视频+KJ优化版+图生视频音画同步_2073621545691475970.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3+双人_单人对话+动作真实自然+极速生视频+KJ优化版+图生视频音画同步_2073621545691475970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（58 个）：
- `GetNode`
- `VAELoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `VAELoaderKJ`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `StringFunction|pysssss`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `GetNode`
- `GetNode`
- `AILab_QwenVL_Advanced`
- `ImageResizeKJv2`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `EmptyLTXVLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LTX2_NAG`
- `LTXVPreprocess`
- `SamplerCustom` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `PrimitiveInt`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `Int`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy positive`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（32/58）

**有卡**：`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`BasicScheduler`、`DualCLIPLoader`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`PathchSageAttentionKJ`、`KSamplerSelect`、`JoinStrings`、`EmptyLTXVLatentVideo`、`ModelSamplingSD3`、`UNETLoader`、`LTX2_NAG`、`LTXVPreprocess`、`SamplerCustom`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`DF_Int_to_Float`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`LTXVSeparateAVLatent`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`Int`、`LoadImage`

**缺卡**（6）：`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`StringFunction|pysssss`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom

## 学习发现

- 次要节点 `LayerUtility: BooleanOperatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: If ` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: NumberCalculatorV2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
