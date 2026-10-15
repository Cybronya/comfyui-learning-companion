---
key: 视频生成/文生视频/LTX2.3导演台V2_2081573363293708290.json
name: LTX2.3导演台V2_2081573363293708290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3导演台V2_2081573363293708290.json
hash: f322809b11bdf291
coverage: 0.540984
learned_at: 2026-10-15 22:45:08
nodes: [SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, GetNode, LTXVConditioning, LTXVConcatAVLatent, GetNode, ConditioningZeroOut, GetNode, BasicScheduler, GetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, CFGGuider, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, GetNode, LTXVCropGuides, LTXVAudioVAEDecode, GetNode, VAEDecode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, SamplerCustomAdvanced, VHS_VideoCombine, LTXDirectorGuide, LoraLoaderModelOnly, LoraLoaderModelOnly, DualCLIPLoader, VAELoaderKJ, VAELoaderKJ, GetNode, LoraLoaderModelOnly, LTXDirectorGuide, UNETLoader, GetNode, SetNode, SetNode, RandomNoise, LTXDirector, DNode_CameraShakeLissajous, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX2.3导演台V2_2081573363293708290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3导演台V2_2081573363293708290.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（61 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `GetNode`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVCropGuides`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `LTXDirectorGuide`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXDirectorGuide`
- `UNETLoader` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `RandomNoise`
- `LTXDirector`
- `DNode_CameraShakeLissajous`
- `VHS_VideoCombine`

## 知识

覆盖率 **54%**（33/61）

**有卡**：`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVConditioning`、`LTXVConcatAVLatent`、`ConditioningZeroOut`、`BasicScheduler`、`LTXVLatentUpsampler`、`KSamplerSelect`、`ManualSigmas`、`LTXVAudioVAEDecode`、`VAEDecode`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`LTXDirectorGuide`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoaderKJ`、`UNETLoader`、`RandomNoise`、`LTXDirector`、`DNode_CameraShakeLissajous`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
