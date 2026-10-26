---
key: 数字人/数字人/LTX导演台2.0白模驱动视频_2074797734040784897.json
name: LTX导演台2.0白模驱动视频_2074797734040784897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX导演台2.0白模驱动视频_2074797734040784897.json
hash: 3353b7d36c352c45
coverage: 0.969697
learned_at: 2026-10-26 01:56:15
nodes: [KSamplerSelect, BasicScheduler, LTXVConditioning, CFGGuider, KSamplerSelect, BasicScheduler, VAEDecode, CFGGuider, LTXVSeparateAVLatent, LTXVAudioVAEDecode, MarkdownNote, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, ConditioningZeroOut, SaveVideo, RandomNoise, CreateVideo, LTXDirectorCropGuides, LTXVSeparateAVLatent, LTXVConcatAVLatent, LTXDirectorGuide, LTXVLatentUpsampler, LTXDirectorCropGuides, SamplerCustomAdvanced, LTXVConcatAVLatent, LTXDirectorGuide, SamplerCustomAdvanced, ModelPreviewOverrideKJ, LTXDirector]
patterns: []
missing: []
---

# 数字人/数字人/LTX导演台2.0白模驱动视频_2074797734040784897.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX导演台2.0白模驱动视频_2074797734040784897.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConditioning`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `ConditioningZeroOut`
- `SaveVideo`
- `RandomNoise`
- `CreateVideo`
- `LTXDirectorCropGuides`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LTXDirectorGuide`
- `LTXVLatentUpsampler` ★核心
- `LTXDirectorCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `LTXDirectorGuide`
- `SamplerCustomAdvanced` ★核心
- `ModelPreviewOverrideKJ`
- `LTXDirector`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`KSamplerSelect`、`BasicScheduler`、`LTXVConditioning`、`CFGGuider`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`ConditioningZeroOut`、`SaveVideo`、`RandomNoise`、`CreateVideo`、`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`LTXDirectorGuide`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`ModelPreviewOverrideKJ`、`LTXDirector`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
