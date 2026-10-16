---
key: 视频生成/图生视频/LTX_Director_V2.0升级版导演台节点工作流_2068939406005854210.json
name: LTX_Director_V2.0升级版导演台节点工作流_2068939406005854210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2068939406005854210.json
hash: b5cd82933c333f78
coverage: 0.941176
learned_at: 2026-10-15 22:40:23
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LTXVLatentUpsampler, LTXVConditioning, ConditioningZeroOut, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, VAEDecode, CreateVideo, SaveVideo, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, SamplerCustomAdvanced, LTXVAudioVAEDecode, ModelPreviewOverrideKJ, MarkdownNote, LTXDirectorGuide, LTXDirectorGuide, VAELoaderKJ, DualCLIPLoader, VAELoader, VAELoader, UNETLoader, LatentUpscaleModelLoader, Note, LTXDirector]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX_Director_V2.0升级版导演台节点工作流_2068939406005854210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2068939406005854210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（34 个）：
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
- `SaveVideo`
- `RandomNoise`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVAudioVAEDecode` ★核心
- `ModelPreviewOverrideKJ`
- `MarkdownNote`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `Note`
- `LTXDirector`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVConditioning`、`ConditioningZeroOut`、`CFGGuider`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`ModelPreviewOverrideKJ`、`LTXDirectorGuide`、`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`LatentUpscaleModelLoader`、`LTXDirector`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
