---
key: 数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json
name: LTX2.5目前最好的商业级数字人_2071844871547211778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json
hash: 601d8e423413dbf6
coverage: 0.971429
learned_at: 2026-10-18 19:07:42
nodes: [LTXVLatentUpsampler, LTXVDualCFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConditioning, LTXVDualCFGGuider, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXDirectorCropGuides, LTXDirectorGuide, SaveVideo, LTX2_NAG, CreateVideo, VAEDecodeTiled, LatentUpscaleModelLoader, LTXDirectorGuide, LTX2_NAG, VAELoader, VAELoader, LTXDirector, CLIPLoader, UNETLoader, RandomNoise, MarkdownNote, LoadVideoUI, CLIPTextEncode]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.5目前最好的商业级数字人_2071844871547211778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（35 个）：
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
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `LTXDirectorCropGuides`
- `LTXDirectorCropGuides`
- `LTXDirectorGuide`
- `SaveVideo`
- `LTX2_NAG`
- `CreateVideo`
- `VAEDecodeTiled` ★核心
- `LatentUpscaleModelLoader`
- `LTXDirectorGuide`
- `LTX2_NAG`
- `VAELoader`
- `VAELoader`
- `LTXDirector`
- `CLIPLoader`
- `UNETLoader` ★核心
- `RandomNoise`
- `MarkdownNote`
- `LoadVideoUI`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **97%**（34/35）

**有卡**：`LTXVLatentUpsampler`、`LTXVDualCFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`RandomNoise`、`LTXDirectorCropGuides`、`LTXDirectorGuide`、`SaveVideo`、`LTX2_NAG`、`CreateVideo`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`VAELoader`、`LTXDirector`、`CLIPLoader`、`UNETLoader`、`LoadVideoUI`、`CLIPTextEncode`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider、LTXVLatentUpsampler
