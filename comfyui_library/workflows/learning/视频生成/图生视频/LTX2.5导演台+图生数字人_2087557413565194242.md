---
key: 视频生成/图生视频/LTX2.5导演台+图生数字人_2087557413565194242.json
name: LTX2.5导演台+图生数字人_2087557413565194242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5导演台+图生数字人_2087557413565194242.json
hash: b8afb888661b5b05
coverage: 1
learned_at: 2026-10-16 21:27:37
nodes: [RandomNoise, BasicScheduler, KSamplerSelect, VAELoaderKJ, DiffusionModelLoaderKJ, VAELoaderKJ, LTXVConcatAVLatent, VAEDecodeTiled, LTXVSeparateAVLatent, YusuLTXDirectorCropGuides, SamplerCustomAdvanced, CFGGuider, YusuLTXDirectorGuide, LTXVConditioning, CLIPLoader, SaveVideo, LTXVAudioVAEDecode, CreateVideo, CLIPTextEncode, Label (rgthree), TTResolutionSelector, YusuLTXDirector]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.5导演台+图生数字人_2087557413565194242.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5导演台+图生数字人_2087557413565194242.json`

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
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `YusuLTXDirectorGuide`
- `LTXVConditioning`
- `CLIPLoader`
- `SaveVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `CLIPTextEncode` ★核心
- `Label (rgthree)`
- `TTResolutionSelector`
- `YusuLTXDirector`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`RandomNoise`、`BasicScheduler`、`KSamplerSelect`、`VAELoaderKJ`、`DiffusionModelLoaderKJ`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVSeparateAVLatent`、`YusuLTXDirectorCropGuides`、`SamplerCustomAdvanced`、`CFGGuider`、`YusuLTXDirectorGuide`、`LTXVConditioning`、`CLIPLoader`、`SaveVideo`、`LTXVAudioVAEDecode`、`CreateVideo`、`CLIPTextEncode`、`Label (rgthree)`、`TTResolutionSelector`、`YusuLTXDirector`

**用到的条目**：CLIPTextEncode、CLIPLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVConcatAVLatent、LTXVSeparateAVLatent、VAEDecodeTiled
