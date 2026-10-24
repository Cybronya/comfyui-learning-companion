---
key: 图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json
name: 一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json
hash: b47d3f583e33f2dd
coverage: 0.862069
learned_at: 2026-10-23 11:54:46
nodes: [UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, Int, LayerMask: LoadBiRefNetModelV2, CLIPTextEncode, LoraLoaderModelOnly, ConditioningZeroOut, VAEEncode, LayerMask: BiRefNetUltraV2, ThresholdMask, LayerMask: MaskGrow, ReferenceLatent, ReferenceLatent, RandomNoise, KSamplerSelect, GetImageSize, AILab_MaskOverlay, Flux2Scheduler, SamplerCustomAdvanced, VAEDecode, Image Comparer (rgthree), LoadImage, SaveImage, PreviewImage, 孤海注释, CFGGuider, MarkdownNote]
patterns: []
missing: []
---

# 图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键人物&背景分离-FLUX-2 Klein & RMBG 2.0 自动识别主体扣图_2089912037089566722.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LayerMask: LoadBiRefNetModelV2`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `LayerMask: BiRefNetUltraV2`
- `ThresholdMask`
- `LayerMask: MaskGrow`
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `GetImageSize`
- `AILab_MaskOverlay`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `孤海注释`
- `CFGGuider`
- `MarkdownNote`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LayerMask: LoadBiRefNetModelV2`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`VAEEncode`、`LayerMask: BiRefNetUltraV2`、`ThresholdMask`、`LayerMask: MaskGrow`、`ReferenceLatent`、`RandomNoise`、`KSamplerSelect`、`GetImageSize`、`AILab_MaskOverlay`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`LoadImage`、`SaveImage`、`CFGGuider`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
