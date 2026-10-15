---
key: 视频生成/文生视频/LTX2.3导演台_原生音视频_修复版_2073961723706560514.json
name: LTX2.3导演台_原生音视频_修复版_2073961723706560514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3导演台_原生音视频_修复版_2073961723706560514.json
hash: bd948218a06ceb62
coverage: 1
learned_at: 2026-10-15 22:45:08
nodes: [VAEDecode, CreateVideo, VAELoaderKJ, VAELoader, ModelPreviewOverrideKJ, LatentUpscaleModelLoader, LTXVLatentUpsampler, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConditioning, CFGGuider, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, LTXVSeparateAVLatent, UNETLoader, VAELoader, LTXDirectorCropGuides, LTXDirectorCropGuides, ConditioningZeroOut, LTXDirectorGuide, DualCLIPLoader, CLIPTextEncode, SaveVideo, LTXDirectorGuide, LTX2_NAG, LTX2_NAG, LTXDirector]
patterns: []
missing: []
---

# 视频生成/文生视频/LTX2.3导演台_原生音视频_修复版_2073961723706560514.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3导演台_原生音视频_修复版_2073961723706560514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（35 个）：
- `VAEDecode` ★核心
- `CreateVideo`
- `VAELoaderKJ`
- `VAELoader`
- `ModelPreviewOverrideKJ`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `LTXVSeparateAVLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `LTXDirectorCropGuides`
- `LTXDirectorCropGuides`
- `ConditioningZeroOut`
- `LTXDirectorGuide`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `LTXDirectorGuide`
- `LTX2_NAG`
- `LTX2_NAG`
- `LTXDirector`

## 知识

覆盖率 **100%**（35/35）

**有卡**：`VAEDecode`、`CreateVideo`、`VAELoaderKJ`、`VAELoader`、`ModelPreviewOverrideKJ`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`RandomNoise`、`UNETLoader`、`LTXDirectorCropGuides`、`ConditioningZeroOut`、`LTXDirectorGuide`、`DualCLIPLoader`、`CLIPTextEncode`、`SaveVideo`、`LTX2_NAG`、`LTXDirector`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
