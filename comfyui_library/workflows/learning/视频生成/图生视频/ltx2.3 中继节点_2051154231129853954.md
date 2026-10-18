---
key: 视频生成/图生视频/ltx2.3 中继节点_2051154231129853954.json
name: ltx2.3 中继节点_2051154231129853954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3 中继节点_2051154231129853954.json
hash: 1804b4faf6d4b398
coverage: 0.923077
learned_at: 2026-10-15 22:37:21
nodes: [PathchSageAttentionKJ, KSamplerSelect, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, ConditioningZeroOut, BasicScheduler, VisualizeSigmasKJ, LTXVPreprocess, SamplerCustom, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecode, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, UNETLoader, VAELoaderKJ, VAELoaderKJ, PreviewImage, PrimitiveNode, EmptyLTXVLatentVideo, VHS_VideoCombine, LTXVEmptyLatentAudio, LTXVConditioning, PromptRelayEncodeTimeline, DualCLIPLoader, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/ltx2.3 中继节点_2051154231129853954.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051154231129853954.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `ConditioningZeroOut`
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `LTXVPreprocess`
- `SamplerCustom` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecode` ★核心
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `PreviewImage`
- `PrimitiveNode`
- `EmptyLTXVLatentVideo`
- `VHS_VideoCombine`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConditioning`
- `PromptRelayEncodeTimeline`
- `DualCLIPLoader`
- `LoadImage`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`PathchSageAttentionKJ`、`KSamplerSelect`、`LTXVImgToVideoInplaceKJ`、`LTXVConcatAVLatent`、`ConditioningZeroOut`、`BasicScheduler`、`VisualizeSigmasKJ`、`LTXVPreprocess`、`SamplerCustom`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`VAEDecode`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoaderKJ`、`EmptyLTXVLatentVideo`、`VHS_VideoCombine`、`LTXVEmptyLatentAudio`、`LTXVConditioning`、`PromptRelayEncodeTimeline`、`DualCLIPLoader`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
