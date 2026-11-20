---
key: 平台全量/SUNE-智能扩图-FireRed-Image-Edit_2066351360525819905.json
name: SUNE-智能扩图-FireRed-Image-Edit_2066351360525819905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SUNE-智能扩图-FireRed-Image-Edit_2066351360525819905.json
hash: fd0e34ba8e9663db
coverage: 0.909091
learned_at: 2026-11-14 00:56:36
nodes: [FluxKontextImageScale, InpaintModelConditioning, LayerUtility: ExtendCanvasV2, Image Comparer (rgthree), TextEncodeQwenImageEditPlus, KSampler, UNETLoader, GrowMaskWithBlur, TextEncodeQwenImageEditPlus, PreviewImage, VAEDecode, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, ImageComposite+, LoadImage, CLIPLoader, VAELoader, LoraLoaderModelOnly, Int, Int, Int, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1013002254822522, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/SUNE-智能扩图-FireRed-Image-Edit_2066351360525819905.json

> 来源文件 `comfyui_library/workflows/平台全量/SUNE-智能扩图-FireRed-Image-Edit_2066351360525819905.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `FluxKontextImageScale`
- `InpaintModelConditioning`
- `LayerUtility: ExtendCanvasV2`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `GrowMaskWithBlur`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageComposite+`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Int`
- `Int`
- `Int`

## 关键参数

- `seed` = `1013002254822522`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`FluxKontextImageScale`、`InpaintModelConditioning`、`LayerUtility: ExtendCanvasV2`、`TextEncodeQwenImageEditPlus`、`KSampler`、`UNETLoader`、`GrowMaskWithBlur`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageComposite+`、`LoadImage`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
