---
key: 图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json
name: Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json
hash: 3e9f1a8fce11fc89
coverage: 1
learned_at: 2026-10-23 11:09:59
nodes: [LoadImage, ControlNetLoader, VAELoader, CLIPLoader, NunchakuQwenImageDiTLoader, ModelSamplingAuraFlow, ControlNetInpaintingAliMamaApply, VAEEncode, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, SaveImage, ImageScaleToTotalPixels]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 24950132874946, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image-ControlNet-Inpainting 局部重绘_2073059743991681026.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `LoadImage`
- `ControlNetLoader`
- `VAELoader`
- `CLIPLoader`
- `NunchakuQwenImageDiTLoader`
- `ModelSamplingAuraFlow`
- `ControlNetInpaintingAliMamaApply`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageScaleToTotalPixels`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `24950132874946`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`LoadImage`、`ControlNetLoader`、`VAELoader`、`CLIPLoader`、`NunchakuQwenImageDiTLoader`、`ModelSamplingAuraFlow`、`ControlNetInpaintingAliMamaApply`、`VAEEncode`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、ControlNetInpaintingAliMamaApply、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
