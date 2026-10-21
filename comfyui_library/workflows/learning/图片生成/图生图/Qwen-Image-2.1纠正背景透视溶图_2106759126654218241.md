---
key: 图片生成/图生图/Qwen-Image-2.1纠正背景透视溶图_2106759126654218241.json
name: Qwen-Image-2.1纠正背景透视溶图_2106759126654218241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1纠正背景透视溶图_2106759126654218241.json
hash: 4e96184817f207eb
coverage: 0.904762
learned_at: 2026-10-21 00:43:18
nodes: [CLIPLoader, VAELoader, UNETLoader, TextEncodeQwenImage21, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Image Comparer (rgthree), LoadImage, 图像缩放V2_孤海, UC_ImagePad, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, CR Prompt Text, FluxGuidance, InvertMask (segment anything), MaskToImage, Cut By Mask, SaveImageAdvanced, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 26, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Qwen-Image-2.1纠正背景透视溶图_2106759126654218241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1纠正背景透视溶图_2106759126654218241.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `图像缩放V2_孤海`
- `UC_ImagePad`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `CR Prompt Text`
- `FluxGuidance`
- `InvertMask (segment anything)`
- `MaskToImage`
- `Cut By Mask`
- `SaveImageAdvanced`
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `26`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`图像缩放V2_孤海`、`UC_ImagePad`、`LoraLoaderModelOnly`、`CR Prompt Text`、`FluxGuidance`、`InvertMask (segment anything)`、`MaskToImage`、`Cut By Mask`、`SaveImageAdvanced`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、FluxGuidance
