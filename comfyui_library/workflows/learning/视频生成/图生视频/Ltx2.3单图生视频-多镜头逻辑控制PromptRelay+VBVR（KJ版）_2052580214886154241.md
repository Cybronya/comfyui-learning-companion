---
key: 视频生成/图生视频/Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）_2052580214886154241.json
name: Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）_2052580214886154241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）_2052580214886154241.json
hash: bdc5ee660c246b3c
coverage: 0.775
learned_at: 2026-10-15 22:37:30
nodes: [GetNode, GetNode, VAEDecode, LTXVEmptyLatentAudio, GetNode, GetNode, LTXVPreprocess, UNETLoader, PathchSageAttentionKJ, EmptyLTXVLatentVideo, SetNode, SetNode, VAELoaderKJ, LoraLoaderModelOnly, VAELoaderKJ, LTXVConditioning, KSamplerSelect, ConditioningZeroOut, BasicScheduler, VisualizeSigmasKJ, PreviewImage, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LTX2SamplingPreviewOverride, LTXVConcatAVLatent, Int, SimpleMath+, easy showAnything, Int, LoadImage, CR Prompt Text, SamplerCustom, PromptRelayEncode, DualCLIPLoader, LTXVImgToVideoInplaceKJ, CLIPTextEncode, Note, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）_2052580214886154241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2052580214886154241.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTX2SamplingPreviewOverride`
- `LTXVConcatAVLatent`
- `Int`
- `SimpleMath+`
- `easy showAnything`
- `Int`
- `LoadImage`
- `CR Prompt Text`
- `SamplerCustom` ★核心
- `PromptRelayEncode`
- `DualCLIPLoader`
- `LTXVImgToVideoInplaceKJ`
- `CLIPTextEncode` ★核心
- `Note`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（31/40）

**有卡**：`VAEDecode`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LTXVConditioning`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VisualizeSigmasKJ`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTX2SamplingPreviewOverride`、`LTXVConcatAVLatent`、`Int`、`SimpleMath+`、`LoadImage`、`CR Prompt Text`、`SamplerCustom`、`PromptRelayEncode`、`DualCLIPLoader`、`LTXVImgToVideoInplaceKJ`、`CLIPTextEncode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
