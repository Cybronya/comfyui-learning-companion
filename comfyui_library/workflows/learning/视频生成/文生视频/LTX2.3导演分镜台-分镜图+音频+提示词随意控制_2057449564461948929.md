---
key: 视频生成/文生视频/LTX2.3导演分镜台-分镜图+音频+提示词随意控制_2057449564461948929.json
name: LTX2.3导演分镜台-分镜图+音频+提示词随意控制_2057449564461948929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3导演分镜台-分镜图+音频+提示词随意控制_2057449564461948929.json
hash: d896207f014a7eb7
coverage: 0.972222
learned_at: 2026-10-11 19:49:39
nodes: [VAELoaderKJ, VAELoaderKJ, VAELoaderKJ, LTXVCropGuides, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, CreateVideo, LTXVAudioVAEDecode, VAEDecodeTiled, SaveVideo, LTXVSeparateAVLatent, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, BasicScheduler, LTXVConcatAVLatent, LTXVConditioning, LTXDirectorGuide, ConditioningZeroOut, LTXVCropGuides, CFGGuider, LTXVSeparateAVLatent, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, CFGGuider, LTXDirectorGuide, LTXVLatentUpsampler, LatentUpscaleModelLoader, MarkdownNote, LTXDirector]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/文生视频/LTX2.3导演分镜台-分镜图+音频+提示词随意控制_2057449564461948929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3导演分镜台-分镜图+音频+提示词随意控制_2057449564461948929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（36 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LTXVCropGuides`
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXDirectorGuide`
- `ConditioningZeroOut`
- `LTXVCropGuides`
- `CFGGuider`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `LTXDirectorGuide`
- `LTXVLatentUpsampler` ★核心
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `LTXDirector`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`VAELoaderKJ`、`LTXVCropGuides`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SaveVideo`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`BasicScheduler`、`LTXVConcatAVLatent`、`LTXVConditioning`、`LTXDirectorGuide`、`ConditioningZeroOut`、`CFGGuider`、`LTXVLatentUpsampler`、`LatentUpscaleModelLoader`、`LTXDirector`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
