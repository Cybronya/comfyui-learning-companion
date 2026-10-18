---
key: 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074150490602033154.json
name: LTX导演台2.0+3DREAK-白模驱动视频工作流_2074150490602033154.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074150490602033154.json
hash: ede2e728f3040e33
coverage: 0.971429
learned_at: 2026-10-15 22:41:13
nodes: [LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, VAEDecode, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, MarkdownNote, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, ModelPreviewOverrideKJ, LTXDirectorGuide, ConditioningZeroOut, SamplerCustomAdvanced, LTXVLatentUpsampler, LTXDirectorCropGuides, CreateVideo, LTXDirectorGuide, GetVideoComponents, VHS_VideoCombine, LTXVConditioning, VHS_VideoCombine, LTXDirector]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074150490602033154.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074150490602033154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（35 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `ModelPreviewOverrideKJ`
- `LTXDirectorGuide`
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXDirectorCropGuides`
- `CreateVideo`
- `LTXDirectorGuide`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `LTXVConditioning`
- `VHS_VideoCombine`
- `LTXDirector`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`VAEDecode`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXDirectorCropGuides`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`ModelPreviewOverrideKJ`、`LTXDirectorGuide`、`ConditioningZeroOut`、`LTXVLatentUpsampler`、`CreateVideo`、`GetVideoComponents`、`VHS_VideoCombine`、`LTXVConditioning`、`LTXDirector`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
