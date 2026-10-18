---
key: 视频生成/图生视频/LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json
name: LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json
hash: 31a3ad01351c0c7a
coverage: 0.741935
learned_at: 2026-10-15 22:37:02
nodes: [KSamplerSelect, LTXVConditioning, SetNode, GetNode, VisualizeSigmasKJ, DualCLIPLoader, ConditioningZeroOut, VAELoaderKJ, VAEDecode, BasicScheduler, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAELoaderKJ, SamplerCustom, PreviewImage, SetNode, GetNode, GetNode, PrimitiveNode, GetNode, LTX2SamplingPreviewOverride, VHS_VideoCombine, UNETLoader, EmptyLTXVLatentVideo, LoadImage, LTXVPreprocess, LTXVImgToVideoInplaceKJ, LTXVEmptyLatentAudio, PathchSageAttentionKJ, PromptRelayEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 441}
---

# 视频生成/图生视频/LTX2.3更高的遵从度-提示词对应连续动作_2046925023830614018.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046925023830614018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（31 个）：
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `SetNode`
- `GetNode`
- `VisualizeSigmasKJ`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `VAELoaderKJ`
- `VAEDecode` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAELoaderKJ`
- `SamplerCustom` ★核心
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `GetNode`
- `LTX2SamplingPreviewOverride`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `EmptyLTXVLatentVideo`
- `LoadImage`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `LTXVEmptyLatentAudio` ★核心
- `PathchSageAttentionKJ`
- `PromptRelayEncode`

## 关键参数

- `width` = `441`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（23/31）

**有卡**：`KSamplerSelect`、`LTXVConditioning`、`VisualizeSigmasKJ`、`DualCLIPLoader`、`ConditioningZeroOut`、`VAELoaderKJ`、`VAEDecode`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`SamplerCustom`、`LTX2SamplingPreviewOverride`、`VHS_VideoCombine`、`UNETLoader`、`EmptyLTXVLatentVideo`、`LoadImage`、`LTXVPreprocess`、`LTXVImgToVideoInplaceKJ`、`LTXVEmptyLatentAudio`、`PathchSageAttentionKJ`、`PromptRelayEncode`

**用到的条目**：VAEDecode、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
