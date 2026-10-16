---
key: 视频生成/图生视频/Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046812792329609218.json
name: Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046812792329609218.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046812792329609218.json
hash: 38abbe668a46f240
coverage: 0.731707
learned_at: 2026-10-15 22:37:00
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, VisualizeSigmasKJ, LTXVPreprocess, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, VHS_VideoCombine, GetNode, LTXVConcatAVLatent, LTXVConditioning, GetNode, BasicScheduler, KSamplerSelect, LoraLoaderModelOnly, PathchSageAttentionKJ, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, RegexExtract, SamplerCustom, Note, SetNode, PreviewImage, UNETLoader, PreviewAny, PreviewAny, RegexExtract, PreviewAny, ConditioningZeroOut, GetNode, RH_LLMAPI_Pro_Node, PromptRelayEncode, CR Prompt Text, JWInteger, EmptyLTXVLatentVideo, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LTXVImgToVideoInplaceKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046812792329609218.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046812792329609218.json`

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
- `VHS_VideoCombine`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `CR Prompt Text`
- `JWInteger`
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVImgToVideoInplaceKJ`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`VHS_VideoCombine`、`LTXVConcatAVLatent`、`LTXVConditioning`、`BasicScheduler`、`KSamplerSelect`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`DualCLIPLoader`、`RegexExtract`、`SamplerCustom`、`UNETLoader`、`ConditioningZeroOut`、`RH_LLMAPI_Pro_Node`、`PromptRelayEncode`、`CR Prompt Text`、`JWInteger`、`EmptyLTXVLatentVideo`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVImgToVideoInplaceKJ`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
