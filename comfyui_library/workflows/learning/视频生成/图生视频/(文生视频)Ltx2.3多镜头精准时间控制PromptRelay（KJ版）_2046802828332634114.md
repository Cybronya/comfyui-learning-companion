---
key: 视频生成/图生视频/(文生视频)Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046802828332634114.json
name: (文生视频)Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046802828332634114.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2046802828332634114.json
hash: 685805814142a944
coverage: 0.725
learned_at: 2026-10-15 22:37:00
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, LTXVEmptyLatentAudio, VisualizeSigmasKJ, LTX2SamplingPreviewOverride, LTXVSeparateAVLatent, VAEDecode, GetNode, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, LTXVConditioning, GetNode, BasicScheduler, KSamplerSelect, LoraLoaderModelOnly, PathchSageAttentionKJ, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, RegexExtract, SamplerCustom, Note, SetNode, PreviewImage, UNETLoader, PreviewAny, PreviewAny, RegexExtract, PreviewAny, ConditioningZeroOut, GetNode, RH_LLMAPI_Pro_Node, PromptRelayEncode, JWInteger, EmptyLTXVLatentVideo, JWInteger, JWInteger, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/(文生视频)Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046802828332634114.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046802828332634114.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `VisualizeSigmasKJ`
- `LTX2SamplingPreviewOverride`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
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
- `JWInteger`
- `EmptyLTXVLatentVideo`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVImgToVideoInplaceKJ`、`LTXVConcatAVLatent`、`LTXVConditioning`、`BasicScheduler`、`KSamplerSelect`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoaderKJ`、`DualCLIPLoader`、`RegexExtract`、`SamplerCustom`、`UNETLoader`、`ConditioningZeroOut`、`RH_LLMAPI_Pro_Node`、`PromptRelayEncode`、`JWInteger`、`EmptyLTXVLatentVideo`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
