---
key: 视频生成/文生视频/LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994.json
name: LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994.json
hash: e70a86e33bcaf885
coverage: 0.755556
learned_at: 2026-10-11 19:49:38
nodes: [RegexExtract, PreviewAny, PreviewAny, PreviewAny, JWInteger, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, RH_LLMAPI_Pro_Node, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, UNETLoader, PathchSageAttentionKJ, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, BasicScheduler, LTX2SamplingPreviewOverride, VisualizeSigmasKJ, KSamplerSelect, LTXVConcatAVLatent, SamplerCustom, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVAudioVAEDecode, GetNode, RegexExtract, LoraLoaderModelOnly, LoraLoaderModelOnly, LTXVConditioning, LoraLoaderModelOnly, ConditioningZeroOut, SimpleMath+, CM_IntToFloat, EmptyLTXVLatentVideo, GetNode, GetNode, LTXVPreprocess, SetNode, SetNode, VHS_VideoCombine, LoadImage, Text, PromptRelayEncodeTimeline, JWInteger]
patterns: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, SimpleMath+]
parameters: {"batch_size": 1, "height": 25, "width": 489}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（45 个）：
- `RegexExtract`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `JWInteger`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RH_LLMAPI_Pro_Node`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `LTXVImgToVideoInplaceKJ`
- `LTXVEmptyLatentAudio` ★核心
- `BasicScheduler`
- `LTX2SamplingPreviewOverride`
- `VisualizeSigmasKJ`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `RegexExtract`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConditioning`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `SimpleMath+`
- `CM_IntToFloat`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `Text`
- `PromptRelayEncodeTimeline`
- `JWInteger`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（34/45）

**有卡**：`RegexExtract`、`JWInteger`、`RH_LLMAPI_Pro_Node`、`VAELoaderKJ`、`DualCLIPLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`BasicScheduler`、`LTX2SamplingPreviewOverride`、`VisualizeSigmasKJ`、`KSamplerSelect`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVAudioVAEDecode`、`LoraLoaderModelOnly`、`LTXVConditioning`、`ConditioningZeroOut`、`CM_IntToFloat`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`VHS_VideoCombine`、`LoadImage`、`Text`、`PromptRelayEncodeTimeline`

**缺卡**（2）：`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
