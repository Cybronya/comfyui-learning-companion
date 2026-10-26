---
key: 图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json
name: LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json
hash: 187161fcf079ec70
coverage: 0.722222
learned_at: 2026-10-26 01:45:33
nodes: [VAELoaderKJ, ImageResizeKJv2, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, GetNode, SetNode, UNETLoader, VAELoader, DualCLIPLoader, VAELoaderKJ, LTXVPreprocess, SimpleMath+, DF_Int_to_Float, LTXVSeparateAVLatent, ShowText|pysssss, CLIPTextEncode, LTXVConditioning, ConditioningZeroOut, LTX2_NAG, LTX2SamplingPreviewOverride, KSamplerSelect, VisualizeSigmasKJ, LTXVConcatAVLatent, SamplerCustom, GetNode, LTXVImgToVideoInplaceKJ, CLIPTextEncode, GetNode, GetNode, VAEDecode, LTXVAudioVAEDecode, VHS_VideoCombine, Int, PrimitiveInt, PrimitiveInt, LoadImage, PrimitiveInt, LayerUtility: If , AILab_QwenVL_Advanced, SetNode, SetNode, StringFunction|pysssss, LayerUtility: BooleanOperatorV2, PathchSageAttentionKJ, BasicScheduler, ModelSamplingSD3, LayerUtility: NumberCalculatorV2, Text, Text, JjkText, GetNode, 孤海注释, JjkText, easy positive]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/LTX2.3图生视频音画同步_面部稳定_真人短剧电商带货视频工作流_2070027521416060929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（54 个）：
- `VAELoaderKJ`
- `ImageResizeKJv2`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTXVPreprocess`
- `SimpleMath+`
- `DF_Int_to_Float`
- `LTXVSeparateAVLatent`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `Int`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveInt`
- `LayerUtility: If `
- `AILab_QwenVL_Advanced`
- `SetNode`
- `SetNode`
- `StringFunction|pysssss`
- `LayerUtility: BooleanOperatorV2`
- `PathchSageAttentionKJ`
- `BasicScheduler`
- `ModelSamplingSD3`
- `LayerUtility: NumberCalculatorV2`
- `Text`
- `Text`
- `JjkText`
- `GetNode`
- `孤海注释`
- `JjkText`
- `easy positive`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（39/54）

**有卡**：`VAELoaderKJ`、`ImageResizeKJv2`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`LTXVPreprocess`、`SimpleMath+`、`DF_Int_to_Float`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVConditioning`、`ConditioningZeroOut`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`KSamplerSelect`、`VisualizeSigmasKJ`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVImgToVideoInplaceKJ`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`Int`、`LoadImage`、`LayerUtility: If `、`AILab_QwenVL_Advanced`、`StringFunction|pysssss`、`LayerUtility: BooleanOperatorV2`、`PathchSageAttentionKJ`、`BasicScheduler`、`ModelSamplingSD3`、`LayerUtility: NumberCalculatorV2`、`Text`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
