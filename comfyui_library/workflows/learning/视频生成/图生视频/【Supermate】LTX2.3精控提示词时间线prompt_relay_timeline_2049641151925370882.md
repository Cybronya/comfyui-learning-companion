---
key: 视频生成/图生视频/【Supermate】LTX2.3精控提示词时间线prompt_relay_timeline_2049641151925370882.json
name: 【Supermate】LTX2.3精控提示词时间线prompt_relay_timeline_2049641151925370882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2049641151925370882.json
hash: 42e94d2d32fcff0b
coverage: 0.75
learned_at: 2026-10-15 22:37:15
nodes: [VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, GetNode, VHS_VideoCombine, SamplerCustom, UNETLoader, VAELoaderKJ, SetNode, VAELoaderKJ, SetNode, PathchSageAttentionKJ, PrimitiveNode, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVPreprocess, BasicScheduler, DualCLIPLoader, LTX2SamplingPreviewOverride, LTXVConditioning, ConditioningZeroOut, KSamplerSelect, VisualizeSigmasKJ, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LoadImage, PreviewImage, LTXVConcatAVLatent, Label (rgthree), PromptRelayEncodeTimeline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 241}
---

# 视频生成/图生视频/【Supermate】LTX2.3精控提示词时间线prompt_relay_timeline_2049641151925370882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049641151925370882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SamplerCustom` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `SetNode`
- `VAELoaderKJ`
- `SetNode`
- `PathchSageAttentionKJ`
- `PrimitiveNode`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `BasicScheduler`
- `DualCLIPLoader`
- `LTX2SamplingPreviewOverride`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `PreviewImage`
- `LTXVConcatAVLatent`
- `Label (rgthree)`
- `PromptRelayEncodeTimeline`

## 关键参数

- `width` = `241`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（24/32）

**有卡**：`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`SamplerCustom`、`UNETLoader`、`VAELoaderKJ`、`PathchSageAttentionKJ`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`BasicScheduler`、`DualCLIPLoader`、`LTX2SamplingPreviewOverride`、`LTXVConditioning`、`ConditioningZeroOut`、`KSamplerSelect`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`LTXVConcatAVLatent`、`Label (rgthree)`、`PromptRelayEncodeTimeline`

**用到的条目**：VAEDecode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
