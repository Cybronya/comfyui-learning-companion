---
key: 视频生成/图生视频/prompt_relay_ltx23_timeline_2055229065958830081.json
name: prompt_relay_ltx23_timeline_2055229065958830081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2055229065958830081.json
hash: b998cefea58d5674
coverage: 0.75
learned_at: 2026-10-15 22:37:56
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, SetNode, LTX2SamplingPreviewOverride, PreviewImage, LTXVSeparateAVLatent, VAEDecode, VHS_VideoCombine, GetNode, SamplerCustom, LTXVConditioning, KSamplerSelect, LoraLoaderModelOnly, ConditioningZeroOut, PathchSageAttentionKJ, LTXVConcatAVLatent, LTXVEmptyLatentAudio, GetNode, GetNode, BasicScheduler, VisualizeSigmasKJ, UNETLoader, VAELoaderKJ, VAELoaderKJ, LTXVPreprocess, LTXVImgToVideoInplaceKJ, EmptyLTXVLatentVideo, LoadImage, DualCLIPLoader, PrimitiveNode, PromptRelayEncodeTimeline]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 353}
---

# 视频生成/图生视频/prompt_relay_ltx23_timeline_2055229065958830081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055229065958830081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `KSamplerSelect` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `DualCLIPLoader`
- `PrimitiveNode`
- `PromptRelayEncodeTimeline`

## 关键参数

- `width` = `353`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（24/32）

**有卡**：`LTXVAudioVAEDecode`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`VHS_VideoCombine`、`SamplerCustom`、`LTXVConditioning`、`KSamplerSelect`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`BasicScheduler`、`VisualizeSigmasKJ`、`UNETLoader`、`VAELoaderKJ`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`LoadImage`、`DualCLIPLoader`、`PromptRelayEncodeTimeline`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
