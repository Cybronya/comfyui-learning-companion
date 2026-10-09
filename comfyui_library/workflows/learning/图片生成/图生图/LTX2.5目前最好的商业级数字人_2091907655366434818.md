---
key: 图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json
name: LTX2.5目前最好的商业级数字人_2091907655366434818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json
hash: 519f62539f8214c0
coverage: 0.918919
learned_at: 2026-10-09 22:36:23
nodes: [LTXVLatentUpsampler, LTXVDualCFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConditioning, LTXVDualCFGGuider, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXDirectorCropGuides, LTXDirectorGuide, SaveVideo, LTX2_NAG, CreateVideo, VAEDecodeTiled, LatentUpscaleModelLoader, LTXDirectorGuide, LTX2_NAG, VAELoader, VAELoader, RandomNoise, MarkdownNote, CLIPTextEncode, 孤海注释, 孤海注释, CLIPLoader, UNETLoader, LoadVideoUI, LTXDirector]
patterns: []
missing: []
---

# 图片生成/图生图/LTX2.5目前最好的商业级数字人_2091907655366434818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2091907655366434818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（37 个）：
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
- `RandomNoise`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `孤海注释`
- `孤海注释`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadVideoUI`
- `LTXDirector`

## 知识

覆盖率 **92%**（34/37）

**有卡**：`LTXVLatentUpsampler`、`LTXVDualCFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`RandomNoise`、`LTXDirectorCropGuides`、`LTXDirectorGuide`、`SaveVideo`、`LTX2_NAG`、`CreateVideo`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LoadVideoUI`、`LTXDirector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider、LTXVLatentUpsampler
