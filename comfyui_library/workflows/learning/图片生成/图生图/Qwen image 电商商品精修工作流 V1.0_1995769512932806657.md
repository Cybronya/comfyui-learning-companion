---
key: 图片生成/图生图/Qwen image 电商商品精修工作流 V1.0_1995769512932806657.json
name: Qwen image 电商商品精修工作流 V1.0_1995769512932806657
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 电商商品精修工作流 V1.0_1995769512932806657.json
hash: f9d66cbc294c53b5
coverage: 0.842105
learned_at: 2026-10-23 11:14:19
nodes: [VAEEncode, ImageScaleToTotalPixels, SaveImage, LoadImage, LoadImage, CLIPLoader, VAELoader, VAEDecode, TextEncodeQwenImageEditPlus, ModelSamplingAuraFlow, CFGNorm, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, LoraLoaderModelOnly, LoadImage, UNETLoader, TextEncodeQwenImageEditPlus]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 2, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 310516778369441, "steps": 30}
---

# 图片生成/图生图/Qwen image 电商商品精修工作流 V1.0_1995769512932806657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 电商商品精修工作流 V1.0_1995769512932806657.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `310516778369441`
- `steps` = `30`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`VAEEncode`、`ImageScaleToTotalPixels`、`SaveImage`、`LoadImage`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm
