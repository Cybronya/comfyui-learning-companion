---
key: 视频生成/文生视频/【3D白模转真实】LTX-2.3 真实物理渲染与驱动_2073385860002832386.json
name: 【3D白模转真实】LTX-2.3 真实物理渲染与驱动_2073385860002832386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【3D白模转真实】LTX-2.3 真实物理渲染与驱动_2073385860002832386.json
hash: 3f2f454bdb670ffc
coverage: 1
learned_at: 2026-10-15 22:47:38
nodes: [LTXDirectorCropGuides, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, LTXVLatentUpsampler, LTXVConditioning, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, BasicScheduler, VAEDecode, CreateVideo, RandomNoise, CFGGuider, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVAudioVAEDecode, VAELoaderKJ, DualCLIPLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, LTXDirectorGuide, LTXDirectorGuide, ConditioningZeroOut, SamplerCustomAdvanced, SaveVideo, ModelPreviewOverrideKJ, Mesh2MotionExplore, LTXDirector, SaveVideo, UNETLoader]
patterns: []
missing: []
---

# 视频生成/文生视频/【3D白模转真实】LTX-2.3 真实物理渲染与驱动_2073385860002832386.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【3D白模转真实】LTX-2.3 真实物理渲染与驱动_2073385860002832386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（34 个）：
- `LTXDirectorCropGuides`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVLatentUpsampler` ★核心
- `LTXVConditioning`
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
- `LTXVAudioVAEDecode` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `ConditioningZeroOut`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `ModelPreviewOverrideKJ`
- `Mesh2MotionExplore`
- `LTXDirector`
- `SaveVideo`
- `UNETLoader` ★核心

## 知识

覆盖率 **100%**（34/34）

**有卡**：`LTXDirectorCropGuides`、`LTXVConcatAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVConditioning`、`CFGGuider`、`VAEDecode`、`CreateVideo`、`RandomNoise`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`LTXVAudioVAEDecode`、`VAELoaderKJ`、`DualCLIPLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`LTXDirectorGuide`、`ConditioningZeroOut`、`SaveVideo`、`ModelPreviewOverrideKJ`、`Mesh2MotionExplore`、`LTXDirector`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
