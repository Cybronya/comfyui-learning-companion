---
key: 图片生成/图生图/F.1 在线生图-图生图_1890336798118158337.json
name: F.1 在线生图-图生图_1890336798118158337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1 在线生图-图生图_1890336798118158337.json
hash: 2f743da49e16276e
coverage: 0.868421
learned_at: 2026-10-23 10:52:36
nodes: [SaveImage, SaveImage, SaveImage, LoadImage, easy showAnything, easy imageSize, ImageScaleBy, easy showAnything, ShowText|pysssss, ConstrainImage|pysssss, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, FluxGuidance, VAELoader, VAEEncode, BasicGuider, KSamplerSelect, BasicScheduler, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, VAEDecode, Anything Everywhere3, Anything Everywhere3, DualCLIPLoader, LayerUtility: JoyCaptionBeta1, RandomNoise, SamplerCustomAdvanced, RandomNoise, SamplerCustomAdvanced, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, UNETLoader, LoraLoaderModelOnly, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/F.1 在线生图-图生图_1890336798118158337.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1 在线生图-图生图_1890336798118158337.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `easy showAnything`
- `easy imageSize`
- `ImageScaleBy`
- `easy showAnything`
- `ShowText|pysssss`
- `ConstrainImage|pysssss`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `FluxGuidance`
- `VAELoader`
- `VAEEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Anything Everywhere3`
- `Anything Everywhere3`
- `DualCLIPLoader`
- `LayerUtility: JoyCaptionBeta1`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`SaveImage`、`LoadImage`、`easy imageSize`、`ImageScaleBy`、`ConstrainImage|pysssss`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`FluxGuidance`、`VAELoader`、`VAEEncode`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`DualCLIPLoader`、`LayerUtility: JoyCaptionBeta1`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
