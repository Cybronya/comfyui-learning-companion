---
key: 视频生成/图生视频/LTX2.3_数字人口播_v1.2_（同步KJ优化版）_2054800786185564162.json
name: LTX2.3_数字人口播_v1.2_（同步KJ优化版）_2054800786185564162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3_数字人口播_v1.2_（同步KJ优化版）_2054800786185564162.json
hash: 67be10a0fb4d3486
coverage: 0.754098
learned_at: 2026-10-15 22:37:52
nodes: [LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, SetNode, ConditioningZeroOut, SamplerCustom, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplaceKJ, SetNode, DF_Int_to_Float, GetNode, StringFunction|pysssss, JjkText, UNETLoader, VAELoaderKJ, GetNode, GetNode, ModelSamplingSD3, AILab_QwenVL_Advanced, LayerUtility: If , LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, ShowText|pysssss, PrimitiveInt, DualCLIPLoader, easy positive, LoadImage, CR Text, StringConcatenate, CR Text, PreviewAny, StringConcatenate, PreviewAny, RunningHub_VoxCPM_LoadModel, RunningHub_VoxCPM_Generate, LoadAudio, ImageResizeKJv2, PreviewAny, SoundFlow_GetLength, LTXVPreprocess, BasicScheduler, EmptyLTXVLatentVideo, SimpleMath+, CR Text, PrimitiveInt, Int, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3_数字人口播_v1.2_（同步KJ优化版）_2054800786185564162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054800786185564162.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（61 个）：
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
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `AILab_QwenVL_Advanced`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: NumberCalculatorV2`
- `ShowText|pysssss`
- `PrimitiveInt`
- `DualCLIPLoader`
- `easy positive`
- `LoadImage`
- `CR Text`
- `StringConcatenate`
- `CR Text`
- `PreviewAny`
- `StringConcatenate`
- `PreviewAny`
- `RunningHub_VoxCPM_LoadModel`
- `RunningHub_VoxCPM_Generate`
- `LoadAudio`
- `ImageResizeKJv2`
- `PreviewAny`
- `SoundFlow_GetLength`
- `LTXVPreprocess`
- `BasicScheduler`
- `EmptyLTXVLatentVideo`
- `SimpleMath+`
- `CR Text`
- `PrimitiveInt`
- `Int`
- `VHS_VideoCombine`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（46/61）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`ConditioningZeroOut`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`StringFunction|pysssss`、`UNETLoader`、`ModelSamplingSD3`、`AILab_QwenVL_Advanced`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`LayerUtility: NumberCalculatorV2`、`DualCLIPLoader`、`easy positive`、`LoadImage`、`CR Text`、`StringConcatenate`、`RunningHub_VoxCPM_LoadModel`、`RunningHub_VoxCPM_Generate`、`LoadAudio`、`ImageResizeKJv2`、`SoundFlow_GetLength`、`LTXVPreprocess`、`BasicScheduler`、`EmptyLTXVLatentVideo`、`SimpleMath+`、`Int`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
