---
key: 视频生成/图生视频/LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json
name: LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json
hash: c3f623ac670a2cde
coverage: 0.969697
learned_at: 2026-10-15 22:40:53
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVConditioning, ConditioningZeroOut, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, VAEDecode, CreateVideo, SaveVideo, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVAudioVAEDecode, UNETLoader, DualCLIPLoader, VAELoader, VAELoader, LTXDirectorGuide, LTXDirectorGuide, VAELoaderKJ, MarkdownNote, ModelPreviewOverrideKJ, LTXDirector]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2072252924708872193.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `LTXDirectorCropGuides`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVConditioning`
- `ConditioningZeroOut`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `CreateVideo`
- `SaveVideo`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `VAELoaderKJ`
- `MarkdownNote`
- `ModelPreviewOverrideKJ`
- `LTXDirector`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVConditioning`、`ConditioningZeroOut`、`CFGGuider`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LTXDirectorGuide`、`VAELoaderKJ`、`ModelPreviewOverrideKJ`、`LTXDirector`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
