---
key: 视频生成/文生视频/LTX2.5导演台_2096907120728956929.json
name: LTX2.5导演台_2096907120728956929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5导演台_2096907120728956929.json
hash: 678ad9ec9d784bf9
coverage: 0.617647
learned_at: 2026-10-15 22:45:17
nodes: [CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, CLIPLoader, VAELoaderKJ, VAELoaderKJ, SetNode, SetNode, SetNode, SetNode, DiffusionModelLoaderKJ, ConditioningZeroOut, GetNode, BasicScheduler, GetNode, RandomNoise, GetNode, GetNode, LTXDirectorCropGuides, CreateVideo, SetNode, VAEDecodeTiled, LTXVSeparateAVLatent, LTXDirectorGuide, LTXVConditioning, SaveVideo, LTXDirector, TTResolutionSelector]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX2.5导演台_2096907120728956929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5导演台_2096907120728956929.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（34 个）：
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `CLIPLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `ConditioningZeroOut`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `LTXDirectorCropGuides`
- `CreateVideo`
- `SetNode`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `LTXDirectorGuide`
- `LTXVConditioning`
- `SaveVideo`
- `LTXDirector`
- `TTResolutionSelector`

## 知识

覆盖率 **62%**（21/34）

**有卡**：`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`LTXVAudioVAEDecode`、`CLIPLoader`、`VAELoaderKJ`、`DiffusionModelLoaderKJ`、`ConditioningZeroOut`、`BasicScheduler`、`RandomNoise`、`LTXDirectorCropGuides`、`CreateVideo`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`LTXDirectorGuide`、`LTXVConditioning`、`SaveVideo`、`LTXDirector`、`TTResolutionSelector`

**用到的条目**：CLIPLoader、ConditioningZeroOut、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled
