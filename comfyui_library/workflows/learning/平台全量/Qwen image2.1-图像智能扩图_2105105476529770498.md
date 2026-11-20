---
key: 平台全量/Qwen image2.1-图像智能扩图_2105105476529770498.json
name: Qwen image2.1-图像智能扩图_2105105476529770498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen image2.1-图像智能扩图_2105105476529770498.json
hash: fd2ae6ecc14698cd
coverage: 0.823529
learned_at: 2026-11-14 00:50:48
nodes: [QwenImage21Cache, Seed (rgthree), UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, SaveImage, Image Comparer (rgthree), VAEDecode, KSampler, CLIPLoader, PreviewImage, TextEncodeQwenImage21, DrawMaskOnImage, PreviewImage, LoadImage, LoraLoaderModelOnly, ImagePadForOutpaint]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 246699432528296, "steps": 30}
---

# 平台全量/Qwen image2.1-图像智能扩图_2105105476529770498.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen image2.1-图像智能扩图_2105105476529770498.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `QwenImage21Cache`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `DrawMaskOnImage`
- `PreviewImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ImagePadForOutpaint`

## 关键参数

- `seed` = `246699432528296`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`QwenImage21Cache`、`Seed (rgthree)`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`SaveImage`、`VAEDecode`、`KSampler`、`CLIPLoader`、`TextEncodeQwenImage21`、`DrawMaskOnImage`、`LoadImage`、`LoraLoaderModelOnly`、`ImagePadForOutpaint`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
