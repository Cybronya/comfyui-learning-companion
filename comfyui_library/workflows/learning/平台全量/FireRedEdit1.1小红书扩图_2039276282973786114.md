---
key: 平台全量/FireRedEdit1.1小红书扩图_2039276282973786114.json
name: FireRedEdit1.1小红书扩图_2039276282973786114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FireRedEdit1.1小红书扩图_2039276282973786114.json
hash: 140e6a096c333399
coverage: 0.774194
learned_at: 2026-11-14 00:26:45
nodes: [LoraLoaderModelOnly, CLIPLoader, UNETLoader, VAELoader, FluxKontextImageScale, GetImageSize, SolidMask, MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ExtendCanvasV2, MaskPreview, PreviewImage, MaskPreview, PreviewImage, Any Switch (rgthree), Any Switch (rgthree), PreviewImage, MaskPreview, Int, LayerMask: MaskInvert, GrowMaskWithBlur, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, InpaintModelConditioning, PreviewImage, KSampler, LayerUtility: SaveImagePlusV2, VAEDecode, Image Comparer (rgthree), LoadImage, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 991514126353545, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FireRedEdit1.1小红书扩图_2039276282973786114.json

> 来源文件 `comfyui_library/workflows/平台全量/FireRedEdit1.1小红书扩图_2039276282973786114.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `FluxKontextImageScale`
- `GetImageSize`
- `SolidMask`
- `MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ExtendCanvasV2`
- `MaskPreview`
- `PreviewImage`
- `MaskPreview`
- `PreviewImage`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `PreviewImage`
- `MaskPreview`
- `Int`
- `LayerMask: MaskInvert`
- `GrowMaskWithBlur`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `InpaintModelConditioning`
- `PreviewImage`
- `KSampler` ★核心
- `LayerUtility: SaveImagePlusV2`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `991514126353545`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`FluxKontextImageScale`、`GetImageSize`、`SolidMask`、`MaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ExtendCanvasV2`、`Int`、`LayerMask: MaskInvert`、`GrowMaskWithBlur`、`TextEncodeQwenImageEditPlus`、`InpaintModelConditioning`、`KSampler`、`LayerUtility: SaveImagePlusV2`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
