---
key: 视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json
name: Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json
hash: 0bee4bc4dd00c680
coverage: 0.74
learned_at: 2026-10-15 22:45:21
nodes: [SetNode, SetNode, LTXVAudioVAEDecode, easy getNode, easy getNode, easy getNode, LoraLoaderModelOnly, LTXVPreprocess, Int, GetNode, DualCLIPLoader, GetNode, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, GetNode, easy setNode, EmptyLTXVLatentVideo, Float, easy setNode, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, SetNode, UNETLoader, easy getNode, GetNode, LTXVSeparateAVLatent, GetNode, VAEDecode, easy setNode, easy setNode, LTXVConditioning, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, GetNode, LTXVImgToVideoInplaceKJ, LTX2SamplingPreviewOverride, PreviewImage, Int, ConditioningZeroOut, VHS_VideoCombine, VisualizeSigmasKJ, SamplerCustom, Float to Int, LTXVEmptyLatentAudio, GetNode, LoadImage, PromptRelayEncodeTimeline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Ltx2.3（单图）PromptRelayEncode(Timeline)_2059942776380420097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVPreprocess`
- `Int`
- `GetNode`
- `DualCLIPLoader`
- `GetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy setNode`
- `EmptyLTXVLatentVideo`
- `Float`
- `easy setNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader` ★核心
- `easy getNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecode` ★核心
- `easy setNode`
- `easy setNode`
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `Int`
- `ConditioningZeroOut`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `SamplerCustom` ★核心
- `Float to Int`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `LoadImage`
- `PromptRelayEncodeTimeline`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（37/50）

**有卡**：`LTXVAudioVAEDecode`、`easy getNode`、`LoraLoaderModelOnly`、`LTXVPreprocess`、`Int`、`DualCLIPLoader`、`VAELoaderKJ`、`easy setNode`、`EmptyLTXVLatentVideo`、`Float`、`LayerUtility: ImageScaleByAspectRatio V2`、`PathchSageAttentionKJ`、`UNETLoader`、`LTXVSeparateAVLatent`、`VAEDecode`、`LTXVConditioning`、`KSamplerSelect`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`LTX2SamplingPreviewOverride`、`ConditioningZeroOut`、`VHS_VideoCombine`、`VisualizeSigmasKJ`、`SamplerCustom`、`Float to Int`、`LTXVEmptyLatentAudio`、`LoadImage`、`PromptRelayEncodeTimeline`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
