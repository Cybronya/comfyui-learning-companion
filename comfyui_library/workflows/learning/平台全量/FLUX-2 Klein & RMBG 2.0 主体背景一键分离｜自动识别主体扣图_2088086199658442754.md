---
key: 平台全量/FLUX-2 Klein & RMBG 2.0 主体背景一键分离｜自动识别主体扣图_2088086199658442754.json
name: FLUX-2 Klein & RMBG 2.0 主体背景一键分离｜自动识别主体扣图_2088086199658442754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX-2 Klein & RMBG 2.0 主体背景一键分离｜自动识别主体扣图_2088086199658442754.json
hash: 3a181942ea9691d9
coverage: 0.925926
learned_at: 2026-11-14 00:24:50
nodes: [VAELoader, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, KSamplerSelect, RandomNoise, VAEEncode, Flux2Scheduler, CFGGuider, VAEDecode, SamplerCustomAdvanced, CLIPLoader, LoraLoaderModelOnly, LayerMask: LoadBiRefNetModelV2, ThresholdMask, LayerMask: MaskGrow, GetImageSize+, LoadImage, UNETLoader, ImpactInt, SaveImage, LayerMask: BiRefNetUltraV2, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, 孤海注释, AILab_MaskOverlay, CLIPTextEncode]
patterns: []
missing: []
---

# 平台全量/FLUX-2 Klein & RMBG 2.0 主体背景一键分离｜自动识别主体扣图_2088086199658442754.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX-2 Klein & RMBG 2.0 主体背景一键分离｜自动识别主体扣图_2088086199658442754.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `VAEEncode` ★核心
- `Flux2Scheduler`
- `CFGGuider`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LayerMask: LoadBiRefNetModelV2`
- `ThresholdMask`
- `LayerMask: MaskGrow`
- `GetImageSize+`
- `LoadImage`
- `UNETLoader` ★核心
- `ImpactInt`
- `SaveImage`
- `LayerMask: BiRefNetUltraV2`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `孤海注释`
- `AILab_MaskOverlay`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **93%**（25/27）

**有卡**：`VAELoader`、`ReferenceLatent`、`ConditioningZeroOut`、`KSamplerSelect`、`RandomNoise`、`VAEEncode`、`Flux2Scheduler`、`CFGGuider`、`VAEDecode`、`SamplerCustomAdvanced`、`CLIPLoader`、`LoraLoaderModelOnly`、`LayerMask: LoadBiRefNetModelV2`、`ThresholdMask`、`LayerMask: MaskGrow`、`GetImageSize+`、`LoadImage`、`UNETLoader`、`ImpactInt`、`SaveImage`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_MaskOverlay`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
