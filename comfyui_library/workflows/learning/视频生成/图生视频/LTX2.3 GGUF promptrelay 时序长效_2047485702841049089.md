---
key: 视频生成/图生视频/LTX2.3 GGUF promptrelay 时序长效_2047485702841049089.json
name: LTX2.3 GGUF promptrelay 时序长效_2047485702841049089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2047485702841049089.json
hash: 2a68d92052cfa594
coverage: 0.717391
learned_at: 2026-10-15 22:37:05
nodes: [LTXVAudioVAEDecode, SetNode, GetNode, SetNode, LTXVEmptyLatentAudio, VisualizeSigmasKJ, GetNode, LTXVPreprocess, LTX2SamplingPreviewOverride, PreviewImage, LTXVSeparateAVLatent, VAEDecode, VAELoaderKJ, VAELoaderKJ, VHS_VideoCombine, GetNode, LTXVImgToVideoInplaceKJ, EmptyLTXVLatentVideo, LTXVConcatAVLatent, SamplerCustom, LTXVConditioning, GetNode, BasicScheduler, KSamplerSelect, PathchSageAttentionKJ, ConditioningZeroOut, easy cleanGpuUsed, easy cleanGpuUsed, LTXVAudioVAEEncode, SetLatentNoiseMask, SolidMask, SetNode, SetNode, AudioCrop, GetNode, easy ifElse, Note, INTConstant, INTConstant, LoadImage, PrimitiveNode, LoadAudio, DualCLIPLoader, LoraLoaderModelOnly, PromptRelayEncode, UnetLoaderGGUF]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 409}
---

# 视频生成/图生视频/LTX2.3 GGUF promptrelay 时序长效_2047485702841049089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047485702841049089.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVEmptyLatentAudio` ★核心
- `VisualizeSigmasKJ`
- `GetNode`
- `LTXVPreprocess`
- `LTX2SamplingPreviewOverride`
- `PreviewImage`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `EmptyLTXVLatentVideo`
- `LTXVConcatAVLatent`
- `SamplerCustom` ★核心
- `LTXVConditioning`
- `GetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `PathchSageAttentionKJ`
- `ConditioningZeroOut`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SolidMask`
- `SetNode`
- `SetNode`
- `AudioCrop`
- `GetNode`
- `easy ifElse`
- `Note`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `PrimitiveNode`
- `LoadAudio`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncode`
- `UnetLoaderGGUF` ★核心

## 关键参数

- `width` = `409`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（33/46）

**有卡**：`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`VisualizeSigmasKJ`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTXVSeparateAVLatent`、`VAEDecode`、`VAELoaderKJ`、`VHS_VideoCombine`、`LTXVImgToVideoInplaceKJ`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`SamplerCustom`、`LTXVConditioning`、`BasicScheduler`、`KSamplerSelect`、`PathchSageAttentionKJ`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`AudioCrop`、`INTConstant`、`LoadImage`、`LoadAudio`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`PromptRelayEncode`、`UnetLoaderGGUF`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、LoadImage、KSamplerSelect、SamplerCustom、LTXVConcatAVLatent、LTXVSeparateAVLatent
