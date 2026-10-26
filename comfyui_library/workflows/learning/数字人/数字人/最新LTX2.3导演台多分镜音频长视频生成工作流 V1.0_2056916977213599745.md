---
key: 数字人/数字人/最新LTX2.3导演台多分镜音频长视频生成工作流 V1.0_2056916977213599745.json
name: 最新LTX2.3导演台多分镜音频长视频生成工作流 V1.0_2056916977213599745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/最新LTX2.3导演台多分镜音频长视频生成工作流 V1.0_2056916977213599745.json
hash: 926c129d9cce2d44
coverage: 0.935484
learned_at: 2026-10-26 02:03:29
nodes: [VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LTX2SamplingPreviewOverride, LatentUpscaleModelLoader, UNETLoader, PathchSageAttentionKJ, VAELoaderKJ, CheckpointLoaderSimple, VAEDecode, LTXVAudioVAEDecode, Reroute, VHS_VideoCombine, Reroute, CreateVideo, SaveVideo, LTXVConditioning, UnetLoaderGGUF, LTXDirectorGuide, ConditioningZeroOut, Lora Loader Stack (rgthree), solarL_SaveImagesToZip, BasicScheduler, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXDirector]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 数字人/数字人/最新LTX2.3导演台多分镜音频长视频生成工作流 V1.0_2056916977213599745.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/最新LTX2.3导演台多分镜音频长视频生成工作流 V1.0_2056916977213599745.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（31 个）：
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LTX2SamplingPreviewOverride`
- `LatentUpscaleModelLoader`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `VAELoaderKJ`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `Reroute`
- `CreateVideo`
- `SaveVideo`
- `LTXVConditioning`
- `UnetLoaderGGUF` ★核心
- `LTXDirectorGuide`
- `ConditioningZeroOut`
- `Lora Loader Stack (rgthree)`
- `solarL_SaveImagesToZip`
- `BasicScheduler`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXDirector`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`VAELoaderKJ`、`DualCLIPLoader`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`UNETLoader`、`PathchSageAttentionKJ`、`CheckpointLoaderSimple`、`VAEDecode`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`CreateVideo`、`SaveVideo`、`LTXVConditioning`、`UnetLoaderGGUF`、`LTXDirectorGuide`、`ConditioningZeroOut`、`Lora Loader Stack (rgthree)`、`solarL_SaveImagesToZip`、`BasicScheduler`、`CFGGuider`、`LTXVConcatAVLatent`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXDirector`

**用到的条目**：VAEDecode、CheckpointLoaderSimple、UNETLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent
