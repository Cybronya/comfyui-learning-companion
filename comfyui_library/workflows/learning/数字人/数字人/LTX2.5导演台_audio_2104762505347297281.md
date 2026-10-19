---
key: 数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json
name: LTX2.5导演台_audio_2104762505347297281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json
hash: f71d77ca96659936
coverage: 1
learned_at: 2026-10-19 00:41:01
nodes: [VAEDecodeTiled, CreateVideo, VAELoader, LatentUpscaleModelLoader, LTXVLatentUpsampler, LTXVDualCFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConditioning, LTXVDualCFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, UNETLoader, VAELoader, SaveVideo, LTXDirectorCropGuides, LTXDirectorCropGuides, LTXDirectorGuide, LTXDirectorGuide, LTX2_NAG, LTX2_NAG, CLIPTextEncode, CLIPLoader, RandomNoise, RandomNoise, LTXDirector]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.5导演台_audio_2104762505347297281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（33 个）：
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `LTXVDualCFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `LTXVDualCFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `SaveVideo`
- `LTXDirectorCropGuides`
- `LTXDirectorCropGuides`
- `LTXDirectorGuide`
- `LTXDirectorGuide`
- `LTX2_NAG`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `RandomNoise`
- `RandomNoise`
- `LTXDirector`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`VAEDecodeTiled`、`CreateVideo`、`VAELoader`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVDualCFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`UNETLoader`、`SaveVideo`、`LTXDirectorCropGuides`、`LTXDirectorGuide`、`LTX2_NAG`、`CLIPTextEncode`、`CLIPLoader`、`RandomNoise`、`LTXDirector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider、LTXVLatentUpsampler
