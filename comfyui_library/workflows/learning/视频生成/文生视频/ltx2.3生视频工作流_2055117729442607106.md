---
key: 视频生成/文生视频/ltx2.3生视频工作流_2055117729442607106.json
name: ltx2.3生视频工作流_2055117729442607106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/ltx2.3生视频工作流_2055117729442607106.json
hash: 52213b6e63399656
coverage: 0.75
learned_at: 2026-10-11 19:49:44
nodes: [SetNode, LTX2SamplingPreviewOverride, VAEDecode, GetNode, LTXVConcatAVLatent, PreviewImage, VisualizeSigmasKJ, ConditioningZeroOut, SamplerCustom, KSamplerSelect, BasicScheduler, LTXVConditioning, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, PrimitiveNode, LTXVEmptyLatentAudio, SetNode, PathchSageAttentionKJ, UNETLoader, LTXVAudioVAEDecode, LTXVSeparateAVLatent, GetNode, GetNode, EmptyLTXVLatentVideo, LTXVImgToVideoInplaceKJ, GetNode, LTXVPreprocess, LoraLoaderModelOnly, PromptRelayEncodeTimeline, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 361}
---

# 视频生成/文生视频/ltx2.3生视频工作流_2055117729442607106.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/ltx2.3生视频工作流_2055117729442607106.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（32 个）：
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `PreviewImage`
- `VisualizeSigmasKJ`
- `ConditioningZeroOut`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConditioning`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `PrimitiveNode`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `LTXVPreprocess`
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncodeTimeline`
- `LoadImage`
- `VHS_VideoCombine`

## 关键参数

- `width` = `361`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（24/32）

**有卡**：`LTX2SamplingPreviewOverride`、`VAEDecode`、`LTXVConcatAVLatent`、`VisualizeSigmasKJ`、`ConditioningZeroOut`、`SamplerCustom`、`KSamplerSelect`、`BasicScheduler`、`LTXVConditioning`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVEmptyLatentAudio`、`PathchSageAttentionKJ`、`UNETLoader`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LTXVPreprocess`、`LoraLoaderModelOnly`、`PromptRelayEncodeTimeline`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
