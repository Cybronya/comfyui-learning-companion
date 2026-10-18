---
key: 视频生成/图生视频/LTX2.3_PromptRelay图生视频模型和工作流_2111402430121472002.json
name: LTX2.3_PromptRelay图生视频模型和工作流_2111402430121472002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3_PromptRelay图生视频模型和工作流_2111402430121472002.json
hash: 5dfb7314fd4b0d4d
coverage: 0.756098
learned_at: 2026-10-18 00:43:21
nodes: [LTXVAudioVAEDecode, PathchSageAttentionKJ, SetNode, KSamplerSelect, LTXVConditioning, BasicScheduler, LTX2SamplingPreviewOverride, VAEDecode, LTXVSeparateAVLatent, ConditioningZeroOut, easy mathInt, VHS_VideoCombine, VisualizeSigmasKJ, LTXVEmptyLatentAudio, ComfyNumberConvert, PreviewAny, easy mathInt, PreviewImage, INTConstant, EmptyLTXVLatentVideo, INTConstant, INTConstant, SamplerCustom, Note, Note, LoadImage, PromptRelayEncodeTimeline, SetNode, DualCLIPLoader, LoraLoaderModelOnly, UNETLoader, GetNode, GetNode, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, GetNode, GetNode, LTXVPreprocess, INTConstant, VAELoaderKJ, VAELoaderKJ]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 489}
---

# 视频生成/图生视频/LTX2.3_PromptRelay图生视频模型和工作流_2111402430121472002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3_PromptRelay图生视频模型和工作流_2111402430121472002.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
- `LTXVAudioVAEDecode` ★核心
- `PathchSageAttentionKJ`
- `SetNode`
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `BasicScheduler`
- `LTX2SamplingPreviewOverride`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `ConditioningZeroOut`
- `easy mathInt`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `LTXVEmptyLatentAudio` ★核心
- `ComfyNumberConvert`
- `PreviewAny`
- `easy mathInt`
- `PreviewImage`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `INTConstant`
- `SamplerCustom` ★核心
- `Note`
- `Note`
- `LoadImage`
- `PromptRelayEncodeTimeline`
- `SetNode`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `GetNode`
- `GetNode`
- `LTXVPreprocess`
- `INTConstant`
- `VAELoaderKJ`
- `VAELoaderKJ`

## 关键参数

- `width` = `489`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（31/41）

**有卡**：`LTXVAudioVAEDecode`、`PathchSageAttentionKJ`、`KSamplerSelect`、`LTXVConditioning`、`BasicScheduler`、`LTX2SamplingPreviewOverride`、`VAEDecode`、`LTXVSeparateAVLatent`、`ConditioningZeroOut`、`easy mathInt`、`VHS_VideoCombine`、`VisualizeSigmasKJ`、`LTXVEmptyLatentAudio`、`ComfyNumberConvert`、`INTConstant`、`EmptyLTXVLatentVideo`、`SamplerCustom`、`LoadImage`、`PromptRelayEncodeTimeline`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LTXVConcatAVLatent`、`LTXVImgToVideoInplaceKJ`、`LTXVPreprocess`、`VAELoaderKJ`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent
