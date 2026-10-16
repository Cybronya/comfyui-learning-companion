---
key: 视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json
name: LTX2.5导演台2.5剪辑台_2092197444435140610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json
hash: 6ca3a646ccaf02bf
coverage: 0.971429
learned_at: 2026-10-16 22:59:05
nodes: [LTXVLatentUpsampler, LTXVDualCFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConditioning, LTXVDualCFGGuider, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, ManualSigmas, LTXVSeparateAVLatent, LTXDirectorCropGuides, LTXDirectorCropGuides, LTXDirectorGuide, SaveVideo, LTX2_NAG, CreateVideo, VAEDecodeTiled, LatentUpscaleModelLoader, LTXDirectorGuide, LTX2_NAG, VAELoader, VAELoader, RandomNoise, MarkdownNote, CLIPTextEncode, CLIPLoader, UNETLoader, LoadVideoUI, LTXDirector]
patterns: []
missing: []
---

# 视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.5导演台2.5剪辑台_2092197444435140610.json`

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
- `RandomNoise`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadVideoUI`
- `LTXDirector`

## 知识

覆盖率 **97%**（34/35）

**有卡**：`LTXVLatentUpsampler`、`LTXVDualCFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`RandomNoise`、`LTXDirectorCropGuides`、`LTXDirectorGuide`、`SaveVideo`、`LTX2_NAG`、`CreateVideo`、`VAEDecodeTiled`、`LatentUpscaleModelLoader`、`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LoadVideoUI`、`LTXDirector`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、LTXVDualCFGGuider、LTXVLatentUpsampler
