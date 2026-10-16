---
key: 视频生成/图生视频/LTX2.3图生视频-音画同步_2058207702853185537.json
name: LTX2.3图生视频-音画同步_2058207702853185537.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058207702853185537.json
hash: c074e2681ca0c221
coverage: 0.880952
learned_at: 2026-10-15 22:38:19
nodes: [DualCLIPLoader, UNETLoader, JjkText, SimpleMath+, LayerUtility: NumberCalculatorV2, PathchSageAttentionKJ, CLIPTextEncode, LTX2_NAG, VAELoader, ModelSamplingSD3, StringFunction|pysssss, LayerUtility: BooleanOperatorV2, LTX2SamplingPreviewOverride, BasicScheduler, CLIPTextEncode, AILab_QwenVL_Advanced, LayerUtility: If , EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, LTXVPreprocess, ConditioningZeroOut, LTXVConditioning, LTXVConcatAVLatent, SamplerCustom, LTXVSeparateAVLatent, VisualizeSigmasKJ, DF_Int_to_Float, LTXVImgToVideoInplaceKJ, KSamplerSelect, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, VAELoaderKJ, VAELoaderKJ, Int, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, ShowText|pysssss, PrimitiveInt, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3图生视频-音画同步_2058207702853185537.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058207702853185537.json`

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
- `ShowText|pysssss`
- `PrimitiveInt`
- `LoadImage`
- `CR Text`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（37/42）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`SimpleMath+`、`LayerUtility: NumberCalculatorV2`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`LTX2_NAG`、`VAELoader`、`ModelSamplingSD3`、`StringFunction|pysssss`、`LayerUtility: BooleanOperatorV2`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`AILab_QwenVL_Advanced`、`LayerUtility: If `、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`ConditioningZeroOut`、`LTXVConditioning`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VisualizeSigmasKJ`、`DF_Int_to_Float`、`LTXVImgToVideoInplaceKJ`、`KSamplerSelect`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`VAELoaderKJ`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
