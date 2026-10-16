---
key: 视频生成/图生视频/小红书[FireRed-Image-Edit1.1] 三图编辑_2030684351255547905.json
name: 小红书[FireRed-Image-Edit1.1] 三图编辑_2030684351255547905.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030684351255547905.json
hash: b93f709ab02cdf72
coverage: 0.875
learned_at: 2026-10-15 22:35:27
nodes: [LoadImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, VAEEncode, ModelSamplingAuraFlow, CFGNorm, KSampler, VAEDecode, SaveImage, PreviewImage, TextEncodeQwenImageEditPlus, PreviewImage, LoadImage, ImageResizeKJv2, JWInteger, FluxKontextImageScale, PreviewImage, LoadImage, FluxKontextImageScale, CR Text, JWInteger]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 230689330120937, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/小红书[FireRed-Image-Edit1.1] 三图编辑_2030684351255547905.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030684351255547905.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
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
- `JWInteger`
- `FluxKontextImageScale`
- `PreviewImage`
- `LoadImage`
- `FluxKontextImageScale`
- `CR Text`
- `JWInteger`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `230689330120937`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageResizeKJv2`、`JWInteger`、`FluxKontextImageScale`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
