---
key: 视频生成/文生视频/自用版 LTX2.5 文生+图生视频多功能整合工作流_2087437987343855618.json
name: 自用版 LTX2.5 文生+图生视频多功能整合工作流_2087437987343855618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/自用版 LTX2.5 文生+图生视频多功能整合工作流_2087437987343855618.json
hash: 945c2c40edcc95f3
coverage: 0.5
learned_at: 2026-10-15 22:48:59
nodes: [SetNode, SetNode, SetNode, SimpleMath+, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy convertAnything, GetNode, GetNode, KSamplerSelect, ManualSigmas, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, LTXVDualCFGGuider, GetNode, LTXVConditioning, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, RandomNoise, LTXVLatentUpsampler, SamplerCustomAdvanced, RandomNoise, LTXVEmptyLatentAudio, easy convertAnything, GetNode, LTXVAudioVAEDecode, SaveVideo, CreateVideo, SetNode, LTX2SamplingPreviewOverride, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, CreateVideo, RepeatImageBatch, SetNode, RepeatImageBatch, SetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, ImageResizeKJv2, Int, Int, SetNode, 忽略多组孤海, 忽略多组孤海, 孤海注释, MarkdownNote, SamplerCustomAdvanced, SetNode, SetNode, LTXVSeparateAVLatent, Seed_, 孤海注释, 孤海注释, UNETLoader, VAELoader, VAELoader, LatentUpscaleModelLoader, PrimitiveStringMultiline, LTXVSeparateAVLatent, VAEDecodeTiled, ResolutionSelector, SetNode, SaveVideo, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, LTXVDualCFGGuider, LTXVAddGuideMulti, LoadImage, GetNode, CLIPLoader, VAEDecodeTiled, LoadImage, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 视频生成/文生视频/自用版 LTX2.5 文生+图生视频多功能整合工作流_2087437987343855618.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/自用版 LTX2.5 文生+图生视频多功能整合工作流_2087437987343855618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（102 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy convertAnything`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVDualCFGGuider`
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVEmptyLatentAudio` ★核心
- `easy convertAnything`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SaveVideo`
- `CreateVideo`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `RepeatImageBatch`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `SetNode`
- `忽略多组孤海`
- `忽略多组孤海`
- `孤海注释`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `Seed_`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `LatentUpscaleModelLoader`
- `PrimitiveStringMultiline`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ResolutionSelector`
- `SetNode`
- `SaveVideo`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTXVDualCFGGuider`
- `LTXVAddGuideMulti`
- `LoadImage`
- `GetNode`
- `CLIPLoader`
- `VAEDecodeTiled` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（51/102）

**有卡**：`SimpleMath+`、`easy convertAnything`、`KSamplerSelect`、`ManualSigmas`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVDualCFGGuider`、`LTXVConditioning`、`RandomNoise`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`SaveVideo`、`CreateVideo`、`LTX2SamplingPreviewOverride`、`EmptyLTXVLatentVideo`、`RepeatImageBatch`、`ImageResizeKJv2`、`Int`、`忽略多组孤海`、`LTXVSeparateAVLatent`、`Seed_`、`UNETLoader`、`VAELoader`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`ResolutionSelector`、`LTXVAddGuideMulti`、`LoadImage`、`CLIPLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
