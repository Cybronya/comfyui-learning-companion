---
key: 视频生成/图生视频/LTX2.3导演台功能_vbvr提示词优化_2055094635088891905.json
name: LTX2.3导演台功能_vbvr提示词优化_2055094635088891905.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3导演台功能_vbvr提示词优化_2055094635088891905.json
hash: f41367bd6fcb0eeb
coverage: 0.734694
learned_at: 2026-10-15 22:37:54
nodes: [VAELoaderKJ, LTX2SamplingPreviewOverride, CheckpointLoaderSimple, DualCLIPLoader, SetNode, SetNode, SetNode, VAELoaderKJ, VAELoaderKJ, RandomNoise, CFGGuider, LTXVConditioning, ConditioningZeroOut, GetNode, LTXDirectorGuide, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, BasicScheduler, GetNode, LTXVLatentUpsampler, LTXVCropGuides, LatentUpscaleModelLoader, GetNode, KSamplerSelect, BasicScheduler, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVConcatAVLatent, GetNode, GetNode, GetNode, LTXVCropGuides, GetNode, GetNode, LTXVAudioVAEDecode, VAEDecodeTiled, LTXDirectorGuide, CreateVideo, SetNode, CFGGuider, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, SaveVideo, LTXDirector]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors"}
---

# 视频生成/图生视频/LTX2.3导演台功能_vbvr提示词优化_2055094635088891905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2055094635088891905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（49 个）：
- `VAELoaderKJ`
- `LTX2SamplingPreviewOverride`
- `CheckpointLoaderSimple` ★核心
- `DualCLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `RandomNoise`
- `CFGGuider`
- `LTXVConditioning`
- `ConditioningZeroOut`
- `GetNode`
- `LTXDirectorGuide`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LatentUpscaleModelLoader`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `LTXDirectorGuide`
- `CreateVideo`
- `SetNode`
- `CFGGuider`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SaveVideo`
- `LTXDirector`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **73%**（36/49）

**有卡**：`VAELoaderKJ`、`LTX2SamplingPreviewOverride`、`CheckpointLoaderSimple`、`DualCLIPLoader`、`RandomNoise`、`CFGGuider`、`LTXVConditioning`、`ConditioningZeroOut`、`LTXDirectorGuide`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`BasicScheduler`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CreateVideo`、`LoraLoaderModelOnly`、`SaveVideo`、`LTXDirector`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
