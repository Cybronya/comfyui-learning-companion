---
key: 图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json
name: Nunchaku-Qwen-Image-Edit_1965891895425699842
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json
hash: 4d58f3e85d109595
coverage: 1
learned_at: 2026-10-23 11:10:00
nodes: [VAELoader, CFGNorm, VAEDecode, CLIPLoader, VAEEncode, SaveImage, ImageScaleToTotalPixels, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, LoadImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 540867679286709, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image-Edit_1965891895425699842.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `VAELoader`
- `CFGNorm`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAEEncode` ★核心
- `SaveImage`
- `ImageScaleToTotalPixels`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `LoadImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `540867679286709`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`VAELoader`、`CFGNorm`、`VAEDecode`、`CLIPLoader`、`VAEEncode`、`SaveImage`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`NunchakuQwenImageDiTLoader`、`LoadImage`、`TextEncodeQwenImageEdit`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
