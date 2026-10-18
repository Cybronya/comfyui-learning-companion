---
key: 视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json
name: Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json
hash: 2e14839589ebdfb1
coverage: 0.913043
learned_at: 2026-10-17 22:18:57
nodes: [UNETLoader, CLIPLoader, easy showAnything, LoadImage, EmptyLatentImage, ComfySwitchNode, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAEDecode, TextEncodeQwenImage21, KSampler, CLIPLoader, TextGenerateLTX2Prompt, VAELoader, PrimitiveBoolean, ResolutionSelector, BatchImagesNode, LoadImage, PrimitiveStringMultiline, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_image_2.1多图编辑int8版｜自带提示词增强｜图生图低显存友好_2104450980506062849.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy showAnything`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `VAELoader`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `BatchImagesNode`
- `LoadImage`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **91%**（63/69）

**有卡**：`UNETLoader`、`CLIPLoader`、`LoadImage`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`KSampler`、`TextGenerateLTX2Prompt`、`VAELoader`、`PrimitiveBoolean`、`ResolutionSelector`、`BatchImagesNode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
