---
key: 视频生成/文生视频/LTX2.5导演台+文生数字人_2087538824678301697.json
name: LTX2.5导演台+文生数字人_2087538824678301697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.5导演台+文生数字人_2087538824678301697.json
hash: ef7bf10abc116a2e
coverage: 0.954545
learned_at: 2026-10-11 20:53:38
nodes: [RandomNoise, BasicScheduler, KSamplerSelect, VAELoaderKJ, DiffusionModelLoaderKJ, VAELoaderKJ, LTXVConcatAVLatent, VAEDecodeTiled, LTXVSeparateAVLatent, YusuLTXDirectorCropGuides, TTResolutionSelector, SamplerCustomAdvanced, Label (rgthree), CFGGuider, YusuLTXDirectorGuide, LTXVConditioning, CLIPLoader, SaveVideo, LTXVAudioVAEDecode, CreateVideo, YusuLTXDirector, CLIPTextEncode]
patterns: []
missing: [Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.5导演台+文生数字人_2087538824678301697.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.5导演台+文生数字人_2087538824678301697.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `RandomNoise`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `VAELoaderKJ`
- `DiffusionModelLoaderKJ`
- `VAELoaderKJ`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVSeparateAVLatent`
- `YusuLTXDirectorCropGuides`
- `TTResolutionSelector`
- `SamplerCustomAdvanced` ★核心
- `Label (rgthree)`
- `CFGGuider`
- `YusuLTXDirectorGuide`
- `LTXVConditioning`
- `CLIPLoader`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `YusuLTXDirector`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **95%**（21/22）

**有卡**：`RandomNoise`、`BasicScheduler`、`KSamplerSelect`、`VAELoaderKJ`、`DiffusionModelLoaderKJ`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`YusuLTXDirectorCropGuides`、`TTResolutionSelector`、`SamplerCustomAdvanced`、`CFGGuider`、`YusuLTXDirectorGuide`、`LTXVConditioning`、`CLIPLoader`、`SaveVideo`、`LTXVAudioVAEDecode`、`CreateVideo`、`YusuLTXDirector`、`CLIPTextEncode`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
