---
key: 视频生成/图生视频/Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）_2046813603185037314.json
name: Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）_2046813603185037314.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046813603185037314.json
hash: 13f05de0140c26b4
coverage: 0.731707
learned_at: 2026-10-15 22:37:00
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, VisualizeSigmasKJ, LTXVPreprocess, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVConcatAVLatent, GetNode, BasicScheduler, KSamplerSelect, PathchSageAttentionKJ, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, RegexExtract, SamplerCustom, Note, SetNode, PreviewImage, UNETLoader, PreviewAny, PreviewAny, RegexExtract, PreviewAny, ConditioningZeroOut, GetNode, RH_LLMAPI_Pro_Node, PromptRelayEncode, JWInteger, EmptyLTXVLatentVideo, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CR Prompt Text, LTXVImgToVideoInplaceKJ, LTXVConditioning, LoraLoaderModelOnly, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）_2046813603185037314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046813603185037314.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
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
- `PreviewAny`
- `ConditioningZeroOut`
- `GetNode`
- `RH_LLMAPI_Pro_Node`
- `PromptRelayEncode`
- `JWInteger`
- `EmptyLTXVLatentVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CR Prompt Text`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConditioning`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`DualCLIPLoader`、`RegexExtract`、`SamplerCustom`、`UNETLoader`、`ConditioningZeroOut`、`RH_LLMAPI_Pro_Node`、`PromptRelayEncode`、`JWInteger`、`EmptyLTXVLatentVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Prompt Text`、`LTXVImgToVideoInplaceKJ`、`LTXVConditioning`、`LoraLoaderModelOnly`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
