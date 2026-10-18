---
key: 视频生成/图生视频/图生视频 分镜控制 Ltx2.3 -PromptRelay_2046957180640829441.json
name: 图生视频 分镜控制 Ltx2.3 -PromptRelay_2046957180640829441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频 分镜控制 Ltx2.3 -PromptRelay_2046957180640829441.json
hash: 6e616de0d72e0730
coverage: 0.795455
learned_at: 2026-10-15 22:37:02
nodes: [UNETLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LoraLoaderModelOnly, SetNode, ConditioningZeroOut, LTXVConditioning, BasicScheduler, LTXVImgToVideoInplaceKJ, LTXVPreprocess, VHS_VideoCombine, SetNode, EmptyLTXVLatentVideo, LTXVConcatAVLatent, KSamplerSelect, PromptRelayEncode, RegexExtract, RegexExtract, VHS_VideoCombine, PreviewAny, PathchSageAttentionKJ, RH_LLMAPI_Pro_Node, LayerUtility: ImageScaleByAspectRatio V2, PreviewAny, PreviewAny, SamplerCustom, VisualizeSigmasKJ, LTX2SamplingPreviewOverride, Text, JWInteger, LoadImage, GetNode, GetNode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, VAEDecode, GetNode, SimpleMath+, JWInteger, LTXVEmptyLatentAudio, JWInteger, CM_IntToFloat]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/图生视频 分镜控制 Ltx2.3 -PromptRelay_2046957180640829441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046957180640829441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（44 个）：
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `ConditioningZeroOut`
- `LTXVConditioning`
- `BasicScheduler`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `VHS_VideoCombine`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `PromptRelayEncode`
- `RegexExtract`
- `RegexExtract`
- `VHS_VideoCombine`
- `PreviewAny`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_Pro_Node`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewAny`
- `PreviewAny`
- `SamplerCustom` ★核心
- `VisualizeSigmasKJ`
- `LTX2SamplingPreviewOverride`
- `Text`
- `JWInteger`
- `LoadImage`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SimpleMath+`
- `JWInteger`
- `LTXVEmptyLatentAudio` ★核心
- `JWInteger`
- `CM_IntToFloat`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（35/44）

**有卡**：`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`LTXVConditioning`、`BasicScheduler`、`LTXVImgToVideoInplaceKJ`、`LTXVPreprocess`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`KSamplerSelect`、`PromptRelayEncode`、`RegexExtract`、`PathchSageAttentionKJ`、`RH_LLMAPI_Pro_Node`、`LayerUtility: ImageScaleByAspectRatio V2`、`SamplerCustom`、`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`、`Text`、`JWInteger`、`LoadImage`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`SimpleMath+`、`LTXVEmptyLatentAudio`、`CM_IntToFloat`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
