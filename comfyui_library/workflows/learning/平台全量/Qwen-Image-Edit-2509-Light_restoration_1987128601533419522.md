---
key: 平台全量/Qwen-Image-Edit-2509-Light_restoration_1987128601533419522.json
name: Qwen-Image-Edit-2509-Light_restoration_1987128601533419522
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-Edit-2509-Light_restoration_1987128601533419522.json
hash: 87db9cb47e4c4dce
coverage: 0.941176
learned_at: 2026-11-14 00:51:42
nodes: [KSampler, ImageScaleToTotalPixels, easy imageSize, CFGNorm, ModelSamplingAuraFlow, CLIPLoader, VAELoader, VAEEncode, TextEncodeQwenImageEditPlus, Image Comparer (rgthree), VAEDecode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, TextEncodeQwenImageEditPlus, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 651027123737387, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Qwen-Image-Edit-2509-Light_restoration_1987128601533419522.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-Edit-2509-Light_restoration_1987128601533419522.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `651027123737387`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`KSampler`、`ImageScaleToTotalPixels`、`easy imageSize`、`CFGNorm`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
