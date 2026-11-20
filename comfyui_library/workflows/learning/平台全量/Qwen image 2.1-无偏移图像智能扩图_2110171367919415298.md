---
key: 平台全量/Qwen image 2.1-无偏移图像智能扩图_2110171367919415298.json
name: Qwen image 2.1-无偏移图像智能扩图_2110171367919415298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen image 2.1-无偏移图像智能扩图_2110171367919415298.json
hash: 4e8de10705c28c0a
coverage: 0.833333
learned_at: 2026-11-14 00:50:41
nodes: [QwenImage21Cache, Seed (rgthree), UNETLoader, Image Comparer (rgthree), VAEDecode, KSampler, CLIPLoader, PreviewImage, TextEncodeQwenImage21, DrawMaskOnImage, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAELoader, PreviewImage, ImagePadForOutpaint, LoraLoaderModelOnly, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 966163514980680, "steps": 30}
---

# 平台全量/Qwen image 2.1-无偏移图像智能扩图_2110171367919415298.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen image 2.1-无偏移图像智能扩图_2110171367919415298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `QwenImage21Cache`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `DrawMaskOnImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAELoader`
- `PreviewImage`
- `ImagePadForOutpaint`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`

## 关键参数

- `seed` = `966163514980680`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`QwenImage21Cache`、`Seed (rgthree)`、`UNETLoader`、`VAEDecode`、`KSampler`、`CLIPLoader`、`TextEncodeQwenImage21`、`DrawMaskOnImage`、`LoadImage`、`ImageScaleToTotalPixels`、`VAELoader`、`ImagePadForOutpaint`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
