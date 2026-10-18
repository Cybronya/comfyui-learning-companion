---
key: 视频生成/图生视频/人脸一致性-LTX导演台2.0+dasiwaV3_2075476336205983745.json
name: 人脸一致性-LTX导演台2.0+dasiwaV3_2075476336205983745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/人脸一致性-LTX导演台2.0+dasiwaV3_2075476336205983745.json
hash: 1bd89f10764f8042
coverage: 0.972973
learned_at: 2026-10-15 22:41:24
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LTXVLatentUpsampler, LTXVConditioning, ConditioningZeroOut, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, VAEDecode, LTXDirectorCropGuides, LTXVSeparateAVLatent, LTXVAudioVAEDecode, MarkdownNote, LTXDirectorGuide, LTXDirectorGuide, VAELoaderKJ, VAELoader, VAELoader, LatentUpscaleModelLoader, ModelPreviewOverrideKJ, DualCLIPLoader, PathchSageAttentionKJ, SamplerCustomAdvanced, RandomNoise, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTX2SamplingPreviewOverride, TTResolutionSelector, UNETLoader, LoraLoaderModelOnly, LTXDirector, CreateVideo, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/人脸一致性-LTX导演台2.0+dasiwaV3_2075476336205983745.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2075476336205983745.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（37 个）：
- `LTXDirectorCropGuides`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVLatentUpsampler` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `VAELoaderKJ`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `ModelPreviewOverrideKJ`
- `DualCLIPLoader`
- `PathchSageAttentionKJ`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTX2SamplingPreviewOverride`
- `TTResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXDirector`
- `CreateVideo`
- `SaveVideo`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVConditioning`、`ConditioningZeroOut`、`CFGGuider`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXDirectorGuide`、`VAELoaderKJ`、`VAELoader`、`LatentUpscaleModelLoader`、`ModelPreviewOverrideKJ`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`SamplerCustomAdvanced`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`TTResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`LTXDirector`、`CreateVideo`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
