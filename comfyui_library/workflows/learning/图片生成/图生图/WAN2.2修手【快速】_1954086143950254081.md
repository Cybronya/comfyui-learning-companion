---
key: 图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json
name: WAN2.2修手【快速】_1954086143950254081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json
hash: f00e1b3a2f58f49f
coverage: 0.842105
learned_at: 2026-10-23 11:27:31
nodes: [ModelSamplingSD3, Anything Everywhere, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, ShowText, RH_Captioner, InpaintModelConditioning, KSampler, VAEDecode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), SaveImage, PreviewImage, LayerUtility: ImageScaleRestore V2]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 2579, "steps": 10}
---

# 图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2修手【快速】_1954086143950254081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ModelSamplingSD3`
- `Anything Everywhere`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ShowText`
- `RH_Captioner`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `LayerUtility: ImageScaleRestore V2`

## 关键参数

- `seed` = `2579`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ShowText`、`RH_Captioner`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`LayerUtility: ImageScaleRestore V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
