---
key: 图片生成/图生图/Qwen2.1 Image图片编辑工作流，指令式修图快速精准高效出图_2115012462922780674.json
name: Qwen2.1 Image图片编辑工作流，指令式修图快速精准高效出图_2115012462922780674
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1 Image图片编辑工作流，指令式修图快速精准高效出图_2115012462922780674.json
hash: 761a78837a53aaf9
coverage: 0.795918
learned_at: 2026-10-30 17:51:04
nodes: [JsonExtractString, PreviewAny, PreviewAny, VAEDecode, SaveImage, PreviewAny, BatchImagesNode, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, CLIPLoader, TextGenerate, PrimitiveStringMultiline, VAELoader, CLIPLoader, UNETLoader, PrimitiveStringMultiline, KSampler, 孤海注释, 孤海注释, VAELoader, VAEDecode, solarL_SaveImagesToZip, CLIPTextEncode, CLIPTextEncode, JjkText, KSampler, EmptyLatentImage, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1 Image图片编辑工作流，指令式修图快速精准高效出图_2115012462922780674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1 Image图片编辑工作流，指令式修图快速精准高效出图_2115012462922780674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `JsonExtractString`
- `PreviewAny`
- `PreviewAny`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewAny`
- `BatchImagesNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `CLIPLoader`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `KSampler` ★核心
- `孤海注释`
- `孤海注释`
- `VAELoader`
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JjkText`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
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
- `UNETLoader` ★核心
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

覆盖率 **80%**（39/49）

**有卡**：`JsonExtractString`、`VAEDecode`、`SaveImage`、`BatchImagesNode`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoadImage`、`CLIPLoader`、`TextGenerate`、`VAELoader`、`UNETLoader`、`KSampler`、`solarL_SaveImagesToZip`、`CLIPTextEncode`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
