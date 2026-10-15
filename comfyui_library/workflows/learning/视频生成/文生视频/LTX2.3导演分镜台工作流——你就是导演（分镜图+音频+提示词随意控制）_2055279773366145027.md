---
key: 视频生成/文生视频/LTX2.3导演分镜台工作流——你就是导演（分镜图+音频+提示词随意控制）_2055279773366145027.json
name: LTX2.3导演分镜台工作流——你就是导演（分镜图+音频+提示词随意控制）_2055279773366145027
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3导演分镜台工作流——你就是导演（分镜图+音频+提示词随意控制）_2055279773366145027.json
hash: 1be2016b62dacc17
coverage: 0.972973
learned_at: 2026-10-15 22:45:08
nodes: [VAELoaderKJ, VAELoaderKJ, BasicScheduler, KSamplerSelect, SamplerCustomAdvanced, LTXVConcatAVLatent, VAELoaderKJ, KSamplerSelect, BasicScheduler, CFGGuider, LTXVConcatAVLatent, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXDirectorGuide, CFGGuider, LTXVCropGuides, LTXDirectorGuide, LTXVCropGuides, LTXVConditioning, ConditioningZeroOut, MarkdownNote, RandomNoise, LTXVLatentUpsampler, LTX2SamplingPreviewOverride, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, CreateVideo, LTXVAudioVAEDecode, VAEDecodeTiled, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXDirector, SaveVideo, LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/文生视频/LTX2.3导演分镜台工作流——你就是导演（分镜图+音频+提示词随意控制）_2055279773366145027.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3导演分镜台工作流——你就是导演（分镜图+音频+提示词随意控制）_2055279773366145027.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（37 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `VAELoaderKJ`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LTXDirectorGuide`
- `CFGGuider`
- `LTXVCropGuides`
- `LTXDirectorGuide`
- `LTXVCropGuides`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `MarkdownNote`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `LTX2SamplingPreviewOverride`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXDirector`
- `SaveVideo`
- `LoadVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`VAELoaderKJ`、`BasicScheduler`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`CFGGuider`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXDirectorGuide`、`LTXVCropGuides`、`LTXVConditioning`、`ConditioningZeroOut`、`RandomNoise`、`LTXVLatentUpsampler`、`LTX2SamplingPreviewOverride`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`CheckpointLoaderSimple`、`CreateVideo`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`LTXDirector`、`SaveVideo`、`LoadVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
