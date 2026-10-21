---
key: 图片生成/图生图/Qwen Image 2.1去除AI感工作流，写实风格人像图生图自然质感提升_2102839671737896962.json
name: Qwen Image 2.1去除AI感工作流，写实风格人像图生图自然质感提升_2102839671737896962
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1去除AI感工作流，写实风格人像图生图自然质感提升_2102839671737896962.json
hash: dd849c21f5413271
coverage: 0.875
learned_at: 2026-10-21 00:42:24
nodes: [CLIPLoader, VAELoader, LoadImage, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAEDecode, ImageStitch, KSampler, SaveImage, TextEncodeQwenImage21, LoraLoaderModelOnly, CLIPLoader, VAELoader, ResolutionSelector, QwenImage21Cache, ComfySwitchNode, EmptyLatentImage, VAEDecode, ImageStitch, KSampler, SaveImage, LoraLoaderModelOnly, UNETLoader, SaveImage, UNETLoader, ComfySwitchNode, ComfySwitchNode, LoadImage, TextEncodeQwenImage21, SaveImage, SaveImage, SaveImage, PrimitiveBoolean, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1去除AI感工作流，写实风格人像图生图自然质感提升_2102839671737896962.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1去除AI感工作流，写实风格人像图生图自然质感提升_2102839671737896962.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `ResolutionSelector`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `KSampler` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LoadImage`
- `TextEncodeQwenImage21`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PrimitiveBoolean`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

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

覆盖率 **88%**（56/64）

**有卡**：`CLIPLoader`、`VAELoader`、`LoadImage`、`ResolutionSelector`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`ImageStitch`、`KSampler`、`SaveImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`UNETLoader`、`PrimitiveBoolean`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
