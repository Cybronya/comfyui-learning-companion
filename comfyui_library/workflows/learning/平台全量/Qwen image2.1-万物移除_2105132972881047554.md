---
key: 平台全量/Qwen image2.1-万物移除_2105132972881047554.json
name: Qwen image2.1-万物移除_2105132972881047554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen image2.1-万物移除_2105132972881047554.json
hash: ed652562cfdeb306
coverage: 0.823529
learned_at: 2026-11-14 00:50:47
nodes: [QwenImage21Cache, LoraLoaderModelOnly, Seed (rgthree), CLIPLoader, UNETLoader, Image Comparer (rgthree), VAEDecode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, DrawMaskOnImage, TextEncodeQwenImage21, PreviewImage, VAELoader, MaskFillHoles, LoadImage, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 378173874938631, "steps": 30}
---

# 平台全量/Qwen image2.1-万物移除_2105132972881047554.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen image2.1-万物移除_2105132972881047554.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `Seed (rgthree)`
- `CLIPLoader`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DrawMaskOnImage`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `VAELoader`
- `MaskFillHoles`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `378173874938631`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`QwenImage21Cache`、`LoraLoaderModelOnly`、`Seed (rgthree)`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`DrawMaskOnImage`、`TextEncodeQwenImage21`、`VAELoader`、`MaskFillHoles`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
