---
key: 图片生成/图生图/Qwen-Image-2.1光影溶图_2104916372500340738.json
name: Qwen-Image-2.1光影溶图_2104916372500340738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1光影溶图_2104916372500340738.json
hash: 7e757239b86a893e
coverage: 0.904762
learned_at: 2026-10-21 00:43:16
nodes: [CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, TextEncodeQwenImage21, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, InvertMask (segment anything), Image Comparer (rgthree), LoadImage, 图像缩放V2_孤海, UC_ImagePad, MaskPreview, MaskToImage, Cut By Mask, SaveImageAdvanced, SaveImage, CR Prompt Text, 孤海注释]
patterns: []
missing: []
parameters: {"cfg": 26, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Qwen-Image-2.1光影溶图_2104916372500340738.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1光影溶图_2104916372500340738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `InvertMask (segment anything)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `图像缩放V2_孤海`
- `UC_ImagePad`
- `MaskPreview`
- `MaskToImage`
- `Cut By Mask`
- `SaveImageAdvanced`
- `SaveImage`
- `CR Prompt Text`
- `孤海注释`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `26`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`KSamplerAdvanced`、`VAEDecode`、`InvertMask (segment anything)`、`LoadImage`、`图像缩放V2_孤海`、`UC_ImagePad`、`MaskPreview`、`MaskToImage`、`Cut By Mask`、`SaveImageAdvanced`、`SaveImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
