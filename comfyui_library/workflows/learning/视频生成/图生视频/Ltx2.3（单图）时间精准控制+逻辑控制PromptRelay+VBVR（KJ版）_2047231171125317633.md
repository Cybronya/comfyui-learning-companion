---
key: 视频生成/图生视频/Ltx2.3（单图）时间精准控制+逻辑控制PromptRelay+VBVR（KJ版）_2047231171125317633.json
name: Ltx2.3（单图）时间精准控制+逻辑控制PromptRelay+VBVR（KJ版）_2047231171125317633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047231171125317633.json
hash: 72959bebdb93d1ed
coverage: 0.865385
learned_at: 2026-10-15 22:37:04
nodes: [LTXVSeparateAVLatent, SetNode, SetNode, LTXVConcatAVLatent, easy setNode, MathExpression|pysssss, easy setNode, easy setNode, easy setNode, Float, Int, Int, VAELoaderKJ, LTX2SamplingPreviewOverride, BasicScheduler, easy getNode, Float to Int, GetNode, easy getNode, LTXVConditioning, KSamplerSelect, LTXVEmptyLatentAudio, SamplerCustom, VAEDecode, easy setNode, LTXVAudioVAEDecode, easy setNode, easy getNode, easy getNode, easy getNode, EmptyLTXVLatentVideo, VAELoaderKJ, LTXVImgToVideoInplaceKJ, GetNode, GetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LTXVPreprocess, PathchSageAttentionKJ, VHS_VideoCombine, PromptRelayEncode, easy getNode, easy getNode, ConditioningZeroOut, UNETLoader, VisualizeSigmasKJ, CR Prompt Text, CR Prompt Text, PreviewImage, LoadImage, DualCLIPLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3（单图）时间精准控制+逻辑控制PromptRelay+VBVR（KJ版）_2047231171125317633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047231171125317633.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `easy setNode`
- `MathExpression|pysssss`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `Float`
- `Int`
- `Int`
- `VAELoaderKJ`
- `LTX2SamplingPreviewOverride`
- `BasicScheduler`
- `easy getNode`
- `Float to Int`
- `GetNode`
- `easy getNode`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `LTXVAudioVAEDecode` ★核心
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `EmptyLTXVLatentVideo`
- `VAELoaderKJ`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVPreprocess`
- `PathchSageAttentionKJ`
- `VHS_VideoCombine`
- `PromptRelayEncode`
- `easy getNode`
- `easy getNode`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VisualizeSigmasKJ`
- `CR Prompt Text`
- `CR Prompt Text`
- `PreviewImage`
- `LoadImage`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（45/52）

**有卡**：`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`easy setNode`、`MathExpression|pysssss`、`Float`、`Int`、`VAELoaderKJ`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`easy getNode`、`Float to Int`、`LTXVConditioning`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`SamplerCustom`、`VAEDecode`、`LTXVAudioVAEDecode`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVPreprocess`、`PathchSageAttentionKJ`、`VHS_VideoCombine`、`PromptRelayEncode`、`ConditioningZeroOut`、`UNETLoader`、`VisualizeSigmasKJ`、`CR Prompt Text`、`LoadImage`、`DualCLIPLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
