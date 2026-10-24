---
key: 图片生成/图生图/【阿良绘】单人+多人双流：Qwen Edit 2511+Union姿势编辑控制V1.0_2006242000118489089.json
name: 【阿良绘】单人+多人双流：Qwen Edit 2511+Union姿势编辑控制V1.0_2006242000118489089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【阿良绘】单人+多人双流：Qwen Edit 2511+Union姿势编辑控制V1.0_2006242000118489089.json
hash: cfaf463d1ae87fba
coverage: 0.877551
learned_at: 2026-10-23 11:52:54
nodes: [UNETLoader, ImageScaleToTotalPixels, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, EmptyLatentImage, DWPreprocessor, LoraLoaderModelOnly, CLIPLoader, Anything Everywhere, Anything Everywhere, Anything Everywhere, VAELoader, GetImageSizeAndCount, EmptyLatentImage, KSampler, Text Multiline, ImageScaleToTotalPixels, LoadImage, ImageConcanate, SaveImage, SaveImage, TextEncodeQwenImageEditPlus, LoadImage, TextEncodeQwenImageEditPlus, PreviewImage, Text Multiline, ControlNetApplySD3, KSampler, ImageScaleToTotalPixels, ImageConcanate, VAEDecode, GetImageSizeAndCount, GetImageSizeAndCount, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageConcanate, PreviewImage, DWPreprocessor, VAEDecode, ImageConcanate, SaveImage, PreviewImage, ImageConcanate, SetUnionControlNetType, ControlNetLoader, ControlNetApplySD3]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "beta57", "seed": 695162672710942, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【阿良绘】单人+多人双流：Qwen Edit 2511+Union姿势编辑控制V1.0_2006242000118489089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【阿良绘】单人+多人双流：Qwen Edit 2511+Union姿势编辑控制V1.0_2006242000118489089.json`

## 结构

**生成流程**：Model → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `UNETLoader` ★核心
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `DWPreprocessor`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAELoader`
- `GetImageSizeAndCount`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `Text Multiline`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `PreviewImage`
- `Text Multiline`
- `ControlNetApplySD3` ★核心
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `PreviewImage`
- `DWPreprocessor`
- `VAEDecode` ★核心
- `ImageConcanate`
- `SaveImage`
- `PreviewImage`
- `ImageConcanate`
- `SetUnionControlNetType`
- `ControlNetLoader`
- `ControlNetApplySD3` ★核心

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `695162672710942`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`
- `controlnet_strength` = `1.0000000000000002`

## 知识

覆盖率 **88%**（43/49）

**有卡**：`UNETLoader`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`EmptyLatentImage`、`DWPreprocessor`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`GetImageSizeAndCount`、`KSampler`、`Text Multiline`、`ImageConcanate`、`SaveImage`、`ControlNetApplySD3`、`VAEDecode`、`SetUnionControlNetType`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
