---
key: 视频生成/图生视频/小红书[FireRed-Image-Edit1.1] 双图编辑_2030672844018946049.json
name: 小红书[FireRed-Image-Edit1.1] 双图编辑_2030672844018946049.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/小红书[FireRed-Image-Edit1.1] 双图编辑_2030672844018946049.json
hash: 3e1010283bde1ca5
coverage: 0.904762
learned_at: 2026-10-15 22:35:27
nodes: [LoadImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, VAEEncode, ModelSamplingAuraFlow, CFGNorm, KSampler, VAEDecode, SaveImage, PreviewImage, TextEncodeQwenImageEditPlus, PreviewImage, LoadImage, ImageResizeKJv2, CR Text, JWInteger, JWInteger, FluxKontextImageScale]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1055846821045972, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/小红书[FireRed-Image-Edit1.1] 双图编辑_2030672844018946049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030672844018946049.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `LoadImage`
- `ImageResizeKJv2`
- `CR Text`
- `JWInteger`
- `JWInteger`
- `FluxKontextImageScale`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1055846821045972`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageResizeKJv2`、`CR Text`、`JWInteger`、`FluxKontextImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
