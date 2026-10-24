---
key: 图片生成/图生图/FireRed-Image-edit1.1无痕扩图_1987748417499803649.json
name: FireRed-Image-edit1.1无痕扩图_1987748417499803649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1无痕扩图_1987748417499803649.json
hash: 3f039dfdd15f1e62
coverage: 0.904762
learned_at: 2026-10-23 10:55:52
nodes: [CLIPLoader, VAELoader, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, GrowMaskWithBlur, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, InpaintModelConditioning, KSampler, VAEDecode, FluxKontextImageScale, UNETLoader, PreviewImage, SaveImage, Image Comparer (rgthree), LayerUtility: ExtendCanvasV2, LoadImage, Int, Int, Int, Int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 251856722563607, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1无痕扩图_1987748417499803649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1无痕扩图_1987748417499803649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMaskWithBlur`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `UNETLoader` ★核心
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ExtendCanvasV2`
- `LoadImage`
- `Int`
- `Int`
- `Int`
- `Int`

## 关键参数

- `seed` = `251856722563607`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`TextEncodeQwenImageEditPlus`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`FluxKontextImageScale`、`UNETLoader`、`SaveImage`、`LayerUtility: ExtendCanvasV2`、`LoadImage`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
