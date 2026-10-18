---
key: 视频生成/图生视频/LTX2.3 双人对话！图生视频音画同步_2047561690383917057.json
name: LTX2.3 双人对话！图生视频音画同步_2047561690383917057.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 双人对话！图生视频音画同步_2047561690383917057.json
hash: 1fe60231230642ce
coverage: 0.672727
learned_at: 2026-10-15 22:37:05
nodes: [UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, VAELoader, PathchSageAttentionKJ, SetNode, SetNode, ModelSamplingSD3, LTX2SamplingPreviewOverride, LayerUtility: If , SetNode, CLIPTextEncode, CLIPTextEncode, ShowText|pysssss, JjkText, GetNode, StringFunction|pysssss, AILab_QwenVL_Advanced, SamplerCustom, LTXVAudioVAEDecode, LTXVSeparateAVLatent, VAEDecode, GetNode, GetNode, SetNode, SetNode, LTX2_NAG, KSamplerSelect, VisualizeSigmasKJ, LTXVImgToVideoInplaceKJ, BasicScheduler, LTXVConcatAVLatent, GetNode, GetNode, LTXVEmptyLatentAudio, LTXVConditioning, LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, PrimitiveInt, JoinStrings, PrimitiveStringMultiline, LTXVPreprocess, PrimitiveInt, EmptyLTXVLatentVideo, ImageResizeKJv2, PrimitiveInt, Int, VHS_VideoCombine, SimpleMath+, GetNode, GetNode, DF_Int_to_Float, LoadImage, easy positive]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3 双人对话！图生视频音画同步_2047561690383917057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047561690383917057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（55 个）：
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `LTX2SamplingPreviewOverride`
- `LayerUtility: If `
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText|pysssss`
- `JjkText`
- `GetNode`
- `StringFunction|pysssss`
- `AILab_QwenVL_Advanced`
- `SamplerCustom` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTX2_NAG`
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `LTXVImgToVideoInplaceKJ`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: NumberCalculatorV2`
- `PrimitiveInt`
- `JoinStrings`
- `PrimitiveStringMultiline`
- `LTXVPreprocess`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `Int`
- `VHS_VideoCombine`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `DF_Int_to_Float`
- `LoadImage`
- `easy positive`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（37/55）

**有卡**：`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LTX2SamplingPreviewOverride`、`LayerUtility: If `、`CLIPTextEncode`、`StringFunction|pysssss`、`AILab_QwenVL_Advanced`、`SamplerCustom`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTX2_NAG`、`KSamplerSelect`、`VisualizeSigmasKJ`、`LTXVImgToVideoInplaceKJ`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`LayerUtility: BooleanOperatorV2`、`LayerUtility: NumberCalculatorV2`、`JoinStrings`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`Int`、`VHS_VideoCombine`、`SimpleMath+`、`DF_Int_to_Float`、`LoadImage`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
