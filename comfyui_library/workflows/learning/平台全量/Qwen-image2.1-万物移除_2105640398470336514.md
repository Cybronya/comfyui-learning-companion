---
key: 平台全量/Qwen-image2.1-万物移除_2105640398470336514.json
name: Qwen-image2.1-万物移除_2105640398470336514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image2.1-万物移除_2105640398470336514.json
hash: ab2f8a7ccad1475f
coverage: 0.875
learned_at: 2026-11-14 00:52:10
nodes: [UNETLoader, Mask Fill Holes, DrawMaskOnImage, TextEncodeQwenImage21, CLIPLoader, VAELoader, PreviewImage, KSampler, CR Text, LayerUtility: ImageScaleByAspectRatio V2, Int, VAEDecode, LoadImage, CR Prompt Text, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 418587942456049, "steps": 25}
---

# 平台全量/Qwen-image2.1-万物移除_2105640398470336514.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image2.1-万物移除_2105640398470336514.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `Mask Fill Holes`
- `DrawMaskOnImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `KSampler` ★核心
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `VAEDecode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `418587942456049`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`UNETLoader`、`Mask Fill Holes`、`DrawMaskOnImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`KSampler`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`VAEDecode`、`LoadImage`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CR Prompt Text
