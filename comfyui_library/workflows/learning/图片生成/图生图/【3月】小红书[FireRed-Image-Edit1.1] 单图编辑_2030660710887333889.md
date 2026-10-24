---
key: 图片生成/图生图/【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889.json
name: 【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889.json
hash: b9bac35da21feffe
coverage: 0.944444
learned_at: 2026-10-23 11:48:12
nodes: [JWInteger, JWInteger, LoadImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, VAEEncode, ModelSamplingAuraFlow, CFGNorm, KSampler, VAEDecode, SaveImage, PreviewImage, ImageResizeKJv2, TextEncodeQwenImageEditPlus, CR Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 926551384660838, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【3月】小红书[FireRed-Image-Edit1.1] 单图编辑_2030660710887333889.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `JWInteger`
- `JWInteger`
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
- `ImageResizeKJv2`
- `TextEncodeQwenImageEditPlus`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `926551384660838`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`JWInteger`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageResizeKJv2`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
