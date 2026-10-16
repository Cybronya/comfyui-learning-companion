---
key: 视频生成/图生视频/LTX2.3图生视频双人对话_2044774391241777153.json
name: LTX2.3图生视频双人对话_2044774391241777153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044774391241777153.json
hash: 6d53d40c28a7223e
coverage: 0.672727
learned_at: 2026-10-15 22:36:41
nodes: [LTXVSeparateAVLatent, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, VAELoaderKJ, BasicScheduler, SetNode, SetNode, StringFunction|pysssss, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, Int, JjkText, PathchSageAttentionKJ, KSamplerSelect, LayerUtility: NumberCalculatorV2, SimpleMath+, PrimitiveStringMultiline, JoinStrings, EmptyLTXVLatentVideo, ModelSamplingSD3, UNETLoader, LTX2SamplingPreviewOverride, CLIPTextEncode, CLIPTextEncode, LTX2_NAG, LTXVPreprocess, SamplerCustom, SetNode, VAEDecode, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, LTXVAudioVAEDecode, GetNode, SetNode, GetNode, DF_Int_to_Float, GetNode, GetNode, VHS_VideoCombine, ShowText|pysssss, GetNode, SetNode, PrimitiveInt, easy positive, LoadImage, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3图生视频双人对话_2044774391241777153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044774391241777153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `LTXVSeparateAVLatent`
- `VAELoader`
- `LTXVConditioning`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
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
- `Int`
- `JjkText`
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `LayerUtility: NumberCalculatorV2`
- `SimpleMath+`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `EmptyLTXVLatentVideo`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LTX2SamplingPreviewOverride`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVPreprocess`
- `SamplerCustom` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `GetNode`
- `SetNode`
- `PrimitiveInt`
- `easy positive`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（37/55）

**有卡**：`LTXVSeparateAVLatent`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`VAELoaderKJ`、`BasicScheduler`、`StringFunction|pysssss`、`DualCLIPLoader`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`Int`、`PathchSageAttentionKJ`、`KSamplerSelect`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`JoinStrings`、`EmptyLTXVLatentVideo`、`ModelSamplingSD3`、`UNETLoader`、`LTX2SamplingPreviewOverride`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVPreprocess`、`SamplerCustom`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`LTXVAudioVAEDecode`、`DF_Int_to_Float`、`VHS_VideoCombine`、`easy positive`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
