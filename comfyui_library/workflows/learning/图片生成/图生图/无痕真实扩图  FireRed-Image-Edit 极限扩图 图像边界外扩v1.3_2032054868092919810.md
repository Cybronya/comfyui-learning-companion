---
key: 图片生成/图生图/无痕真实扩图  FireRed-Image-Edit 极限扩图 图像边界外扩v1.3_2032054868092919810.json
name: 无痕真实扩图  FireRed-Image-Edit 极限扩图 图像边界外扩v1.3_2032054868092919810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/无痕真实扩图  FireRed-Image-Edit 极限扩图 图像边界外扩v1.3_2032054868092919810.json
hash: 7e607c4a78bab779
coverage: 0.882353
learned_at: 2026-10-23 13:04:27
nodes: [FluxKontextImageScale, TextEncodeQwenImageEditPlus, InpaintModelConditioning, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, GrowMaskWithBlur, Image Comparer (rgthree), VAELoader, KSampler, VAEDecode, TextEncodeQwenImageEditPlus, LoadImage, LayerUtility: ExtendCanvasV2, UNETLoader, LoraLoaderModelOnly, SaveImage, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 488013042915289, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/无痕真实扩图  FireRed-Image-Edit 极限扩图 图像边界外扩v1.3_2032054868092919810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/无痕真实扩图  FireRed-Image-Edit 极限扩图 图像边界外扩v1.3_2032054868092919810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `InpaintModelConditioning`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LayerUtility: ExtendCanvasV2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `488013042915289`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`FluxKontextImageScale`、`TextEncodeQwenImageEditPlus`、`InpaintModelConditioning`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`VAELoader`、`KSampler`、`VAEDecode`、`LoadImage`、`LayerUtility: ExtendCanvasV2`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
