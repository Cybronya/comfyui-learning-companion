---
key: 视频生成/图生视频/Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）0506_2051845619093909505.json
name: Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）0506_2051845619093909505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）0506_2051845619093909505.json
hash: 70c66201be33d79f
coverage: 0.738095
learned_at: 2026-10-15 22:37:23
nodes: [GetNode, GetNode, VAEDecode, PromptRelayEncode, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, GetNode, GetNode, LTXVPreprocess, UNETLoader, PathchSageAttentionKJ, EmptyLTXVLatentVideo, SetNode, SetNode, VAELoaderKJ, LoraLoaderModelOnly, VAELoaderKJ, LTXVConditioning, KSamplerSelect, ConditioningZeroOut, BasicScheduler, VisualizeSigmasKJ, PreviewImage, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LayerUtility: ImageScaleByAspectRatio V2, LTX2SamplingPreviewOverride, LTXVConcatAVLatent, Int, SimpleMath+, easy showAnything, Int, CR Prompt Text, CR Prompt Text, LoadImage, DualCLIPLoader, MarkdownNote, CLIPTextEncode, MarkdownNote, VHS_VideoCombine, Note, SamplerCustom]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/Ltx2.3单图生视频-多镜头逻辑控制PromptRelay+VBVR（KJ版）0506_2051845619093909505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051845619093909505.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `PromptRelayEncode`
- `LTXVImgToVideoInplaceKJ`
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
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `DualCLIPLoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `VHS_VideoCombine`
- `Note`
- `SamplerCustom` ★核心

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（31/42）

**有卡**：`VAEDecode`、`PromptRelayEncode`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`LTXVPreprocess`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`LTXVConditioning`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VisualizeSigmasKJ`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTX2SamplingPreviewOverride`、`LTXVConcatAVLatent`、`Int`、`SimpleMath+`、`CR Prompt Text`、`LoadImage`、`DualCLIPLoader`、`CLIPTextEncode`、`VHS_VideoCombine`、`SamplerCustom`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
