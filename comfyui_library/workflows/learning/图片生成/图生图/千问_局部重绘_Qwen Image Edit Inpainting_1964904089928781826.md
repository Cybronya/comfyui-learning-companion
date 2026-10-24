---
key: 图片生成/图生图/千问_局部重绘_Qwen Image Edit Inpainting_1964904089928781826.json
name: 千问_局部重绘_Qwen Image Edit Inpainting_1964904089928781826
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问_局部重绘_Qwen Image Edit Inpainting_1964904089928781826.json
hash: 93eca4fe7f03ccbc
coverage: 0.909091
learned_at: 2026-10-23 12:30:22
nodes: [ModelSamplingAuraFlow, VAEDecode, VAEEncode, CLIPLoader, VAELoader, LoraLoaderModelOnly, KSampler, CFGNorm, ImageStitch, SaveImage, SaveImage, LoadImage, UNETLoader, Note, ImageStitch, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, ImageAndMaskPreview, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2.5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 973988894187909, "steps": 20}
---

# 图片生成/图生图/千问_局部重绘_Qwen Image Edit Inpainting_1964904089928781826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问_局部重绘_Qwen Image Edit Inpainting_1964904089928781826.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CFGNorm`
- `ImageStitch`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `Note`
- `ImageStitch`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `ImageAndMaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `973988894187909`
- `steps` = `20`
- `cfg` = `2.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`ModelSamplingAuraFlow`、`VAEDecode`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`CFGNorm`、`ImageStitch`、`SaveImage`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImageEdit`、`ImageAndMaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm
