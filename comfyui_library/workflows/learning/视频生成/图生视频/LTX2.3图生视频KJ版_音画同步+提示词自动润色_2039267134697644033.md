---
key: 视频生成/图生视频/LTX2.3图生视频KJ版_音画同步+提示词自动润色_2039267134697644033.json
name: LTX2.3图生视频KJ版_音画同步+提示词自动润色_2039267134697644033.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2039267134697644033.json
hash: 9e7636b3ed2d4742
coverage: 0.74
learned_at: 2026-10-15 22:36:07
nodes: [LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, SetNode, ConditioningZeroOut, SamplerCustom, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplaceKJ, SetNode, DF_Int_to_Float, GetNode, StringFunction|pysssss, UNETLoader, VAELoaderKJ, DualCLIPLoader, GetNode, GetNode, ModelSamplingSD3, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, SimpleMath+, JjkText, VHS_VideoCombine, ShowText|pysssss, Int, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, easy positive]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3图生视频KJ版_音画同步+提示词自动润色_2039267134697644033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2039267134697644033.json`

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
- `JjkText`
- `VHS_VideoCombine`
- `ShowText|pysssss`
- `Int`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `easy positive`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（37/50）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ConditioningZeroOut`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`StringFunction|pysssss`、`UNETLoader`、`DualCLIPLoader`、`ModelSamplingSD3`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`LayerUtility: NumberCalculatorV2`、`SimpleMath+`、`VHS_VideoCombine`、`Int`、`LoadImage`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
