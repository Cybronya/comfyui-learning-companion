---
key: 平台全量/Qwen-Image-2.1纠正背景透视溶图_2114601767320244225.json
name: Qwen-Image-2.1纠正背景透视溶图_2114601767320244225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-2.1纠正背景透视溶图_2114601767320244225.json
hash: c9f34c0ebd220a82
coverage: 0.909091
learned_at: 2026-11-14 00:51:35
nodes: [CLIPLoader, VAELoader, UNETLoader, TextEncodeQwenImage21, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Image Comparer (rgthree), LoadImage, 图像缩放V2_孤海, UC_ImagePad, LoraLoaderModelOnly, LoraLoaderModelOnly, 孤海注释, CR Prompt Text, FluxGuidance, InvertMask (segment anything), MaskToImage, Cut By Mask, SaveImageAdvanced, SaveImage, MaskPreview]
patterns: []
missing: []
parameters: {"cfg": 26, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/Qwen-Image-2.1纠正背景透视溶图_2114601767320244225.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-2.1纠正背景透视溶图_2114601767320244225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
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
- `MaskPreview`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `26`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`图像缩放V2_孤海`、`UC_ImagePad`、`LoraLoaderModelOnly`、`CR Prompt Text`、`FluxGuidance`、`InvertMask (segment anything)`、`MaskToImage`、`Cut By Mask`、`SaveImageAdvanced`、`SaveImage`、`MaskPreview`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、FluxGuidance
