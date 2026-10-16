---
key: 视频生成/图生视频/Ltx2.3-多镜头-PromptRelay控制时间（KJ版）_2046850819689029634.json
name: Ltx2.3-多镜头-PromptRelay控制时间（KJ版）_2046850819689029634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046850819689029634.json
hash: 3966686bdb31c022
coverage: 0.674419
learned_at: 2026-10-15 22:37:01
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, VisualizeSigmasKJ, LTXVPreprocess, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVConcatAVLatent, LTXVConditioning, GetNode, BasicScheduler, KSamplerSelect, PathchSageAttentionKJ, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, RegexExtract, SamplerCustom, Note, SetNode, PreviewImage, UNETLoader, PreviewAny, PreviewAny, RegexExtract, ConditioningZeroOut, GetNode, PromptRelayEncode, LayerUtility: ImageScaleByAspectRatio V2, LTXVImgToVideoInplaceKJ, LoadImage, CR Prompt Text, JWInteger, Note, Note, Note, PreviewAny, RH_LLMAPI_Pro_Node, VHS_VideoCombine, EmptyLTXVLatentVideo]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3-多镜头-PromptRelay控制时间（KJ版）_2046850819689029634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046850819689029634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `VisualizeSigmasKJ`
- `LTXVPreprocess`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `PathchSageAttentionKJ`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `RegexExtract`
- `SamplerCustom` ★核心
- `Note`
- `SetNode`
- `PreviewImage`
- `UNETLoader` ★核心
- `PreviewAny`
- `PreviewAny`
- `RegexExtract`
- `ConditioningZeroOut`
- `GetNode`
- `PromptRelayEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `Note`
- `Note`
- `Note`
- `PreviewAny`
- `RH_LLMAPI_Pro_Node`
- `VHS_VideoCombine`
- `EmptyLTXVLatentVideo`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（29/43）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVConditioning`、`BasicScheduler`、`KSamplerSelect`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`DualCLIPLoader`、`RegexExtract`、`SamplerCustom`、`UNETLoader`、`ConditioningZeroOut`、`PromptRelayEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`CR Prompt Text`、`JWInteger`、`RH_LLMAPI_Pro_Node`、`VHS_VideoCombine`、`EmptyLTXVLatentVideo`

**用到的条目**：VAEDecode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
