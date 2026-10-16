---
key: 视频生成/图生视频/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2090771425203417090.json
name: LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2090771425203417090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2090771425203417090.json
hash: 2c91d0ba13f9cb43
coverage: 0.74
learned_at: 2026-10-16 22:30:32
nodes: [LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoader, LTXVConditioning, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVConcatAVLatent, PathchSageAttentionKJ, SetNode, VAELoaderKJ, EmptyLTXVLatentVideo, BasicScheduler, LTXVPreprocess, SetNode, ConditioningZeroOut, SamplerCustom, VHS_VideoCombine, VAEDecode, KSamplerSelect, CLIPTextEncode, CLIPTextEncode, LTXVImgToVideoInplaceKJ, SetNode, DF_Int_to_Float, GetNode, StringFunction|pysssss, JjkText, UNETLoader, VAELoaderKJ, GetNode, GetNode, ModelSamplingSD3, AILab_QwenVL_Advanced, ImageResizeKJv2, LayerUtility: If , LayerUtility: BooleanOperatorV2, LayerUtility: NumberCalculatorV2, ShowText|pysssss, PrimitiveInt, Int, PrimitiveInt, SimpleMath+, PrimitiveInt, DualCLIPLoader, easy positive, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 305}
---

# 视频生成/图生视频/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2090771425203417090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频音画同步KJ优化版图片加文字直出视频短剧电商带货视频工作流_2090771425203417090.json`

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
- `VHS_VideoCombine`
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
- `ImageResizeKJv2`
- `LayerUtility: If `
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: NumberCalculatorV2`
- `ShowText|pysssss`
- `PrimitiveInt`
- `Int`
- `PrimitiveInt`
- `SimpleMath+`
- `PrimitiveInt`
- `DualCLIPLoader`
- `easy positive`
- `LoadImage`

## 关键参数

- `width` = `305`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（37/50）

**有卡**：`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAELoader`、`LTXVConditioning`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`LTXVPreprocess`、`ConditioningZeroOut`、`SamplerCustom`、`VHS_VideoCombine`、`VAEDecode`、`KSamplerSelect`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`DF_Int_to_Float`、`StringFunction|pysssss`、`UNETLoader`、`ModelSamplingSD3`、`AILab_QwenVL_Advanced`、`ImageResizeKJv2`、`LayerUtility: If `、`LayerUtility: BooleanOperatorV2`、`LayerUtility: NumberCalculatorV2`、`Int`、`SimpleMath+`、`DualCLIPLoader`、`easy positive`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
