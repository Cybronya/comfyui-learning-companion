---
key: 视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json
name: LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json
hash: ae143e7d69a854c3
coverage: 0.969697
learned_at: 2026-10-15 22:44:36
nodes: [LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LatentUpscaleModelLoader, LTXVLatentUpsampler, ConditioningZeroOut, CFGGuider, KSamplerSelect, BasicScheduler, VAEDecode, CreateVideo, RandomNoise, CFGGuider, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVAudioVAEDecode, VAELoaderKJ, DualCLIPLoader, VAELoader, VAELoader, MarkdownNote, ModelPreviewOverrideKJ, LTXDirector, LTXDirectorGuide, LTXVConditioning, LTXDirectorCropGuides, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXDirectorGuide, SaveVideo, UNETLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `ConditioningZeroOut`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `CreateVideo`
- `RandomNoise`
- `CFGGuider`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `MarkdownNote`
- `ModelPreviewOverrideKJ`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVConditioning`
- `LTXDirectorCropGuides`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXDirectorGuide`
- `SaveVideo`
- `UNETLoader` ★核心

## 知识

覆盖率 **97%**（32/33）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`ConditioningZeroOut`、`CFGGuider`、`VAEDecode`、`CreateVideo`、`RandomNoise`、`LTXDirectorCropGuides`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`ModelPreviewOverrideKJ`、`LTXDirector`、`LTXDirectorGuide`、`LTXVConditioning`、`SaveVideo`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
