---
key: 数字人/数字人/LTX2.3唱歌对口型数字人_2071844848252055554.json
name: LTX2.3唱歌对口型数字人_2071844848252055554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3唱歌对口型数字人_2071844848252055554.json
hash: a9bcc5c556658cbf
coverage: 1
learned_at: 2026-10-26 01:55:56
nodes: [VAEDecode, CreateVideo, VAELoaderKJ, VAELoader, LatentUpscaleModelLoader, LTXVLatentUpsampler, CFGGuider, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVConditioning, CFGGuider, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, LTXVSeparateAVLatent, VAELoader, LTXDirectorCropGuides, LTXDirectorCropGuides, ConditioningZeroOut, LTXDirectorGuide, DualCLIPLoader, CLIPTextEncode, SaveVideo, LTXDirectorGuide, LTX2_NAG, LTX2_NAG, ModelPreviewOverrideKJ, UNETLoader, LTXDirector, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.3唱歌对口型数字人_2071844848252055554.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3唱歌对口型数字人_2071844848252055554.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（36 个）：
- `VAEDecode` ★核心
- `CreateVideo`
- `VAELoaderKJ`
- `VAELoader`
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
- `ModelPreviewOverrideKJ`
- `UNETLoader` ★核心
- `LTXDirector`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **100%**（36/36）

**有卡**：`VAEDecode`、`CreateVideo`、`VAELoaderKJ`、`VAELoader`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`CFGGuider`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`RandomNoise`、`LTXDirectorCropGuides`、`ConditioningZeroOut`、`LTXDirectorGuide`、`DualCLIPLoader`、`CLIPTextEncode`、`SaveVideo`、`LTX2_NAG`、`ModelPreviewOverrideKJ`、`UNETLoader`、`LTXDirector`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、UNETLoader、CFGGuider、KSamplerSelect
