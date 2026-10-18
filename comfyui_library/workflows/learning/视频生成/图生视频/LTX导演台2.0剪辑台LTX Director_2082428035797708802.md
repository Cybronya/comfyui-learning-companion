---
key: 视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2082428035797708802.json
name: LTX导演台2.0剪辑台LTX Director_2082428035797708802.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2082428035797708802.json
hash: 5f411940bd4dc09d
coverage: 0.969697
learned_at: 2026-10-15 22:42:31
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LTXVLatentUpsampler, LTXVConditioning, ConditioningZeroOut, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, VAEDecode, CreateVideo, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVAudioVAEDecode, MarkdownNote, LTXDirectorGuide, LTXDirectorGuide, SaveVideo, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, ModelPreviewOverrideKJ, LTXDirector]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2082428035797708802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2082428035797708802.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
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
- `CreateVideo`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `SaveVideo`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `ModelPreviewOverrideKJ`
- `LTXDirector`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVConditioning`、`ConditioningZeroOut`、`CFGGuider`、`VAEDecode`、`CreateVideo`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`LTXDirectorGuide`、`SaveVideo`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`ModelPreviewOverrideKJ`、`LTXDirector`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
