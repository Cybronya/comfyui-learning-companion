---
key: 视频生成/图生视频/WH-AI-Studio-LTX2.3图生视频-音画同步（可扩展多图生成-提示词润色）_2044056127922507778.json
name: WH-AI-Studio-LTX2.3图生视频-音画同步（可扩展多图生成-提示词润色）_2044056127922507778.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WH-AI-Studio-LTX2.3图生视频-音画同步（可扩展多图生成-提示词润色）_2044056127922507778.json
hash: a4c6d797cf2ba185
coverage: 0.880952
learned_at: 2026-10-15 22:36:36
nodes: [DualCLIPLoader, UNETLoader, JjkText, SimpleMath+, LayerUtility: NumberCalculatorV2, PathchSageAttentionKJ, CLIPTextEncode, LTX2_NAG, VAELoader, ModelSamplingSD3, StringFunction|pysssss, LayerUtility: BooleanOperatorV2, LTX2SamplingPreviewOverride, BasicScheduler, CLIPTextEncode, AILab_QwenVL_Advanced, LayerUtility: If , EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVPreprocess, ConditioningZeroOut, LTXVConditioning, LTXVConcatAVLatent, SamplerCustom, LTXVSeparateAVLatent, VisualizeSigmasKJ, DF_Int_to_Float, LTXVImgToVideoInplaceKJ, KSamplerSelect, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, VAELoaderKJ, VAELoaderKJ, Int, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoadImage, ShowText|pysssss, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/WH-AI-Studio-LTX2.3图生视频-音画同步（可扩展多图生成-提示词润色）_2044056127922507778.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044056127922507778.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（42 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `JjkText`
- `SimpleMath+`
- `LayerUtility: NumberCalculatorV2`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `VAELoader`
- `ModelSamplingSD3`
- `StringFunction|pysssss`
- `LayerUtility: BooleanOperatorV2`
- `LTX2SamplingPreviewOverride`
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `AILab_QwenVL_Advanced`
- `LayerUtility: If `
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVPreprocess`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `VisualizeSigmasKJ`
- `DF_Int_to_Float`
- `LTXVImgToVideoInplaceKJ`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `ShowText|pysssss`
- `CR Text`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（37/42）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`SimpleMath+`、`LayerUtility: NumberCalculatorV2`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LTX2_NAG`、`VAELoader`、`ModelSamplingSD3`、`StringFunction|pysssss`、`LayerUtility: BooleanOperatorV2`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`AILab_QwenVL_Advanced`、`LayerUtility: If `、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`ConditioningZeroOut`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VisualizeSigmasKJ`、`DF_Int_to_Float`、`LTXVImgToVideoInplaceKJ`、`KSamplerSelect`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`VAELoaderKJ`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
