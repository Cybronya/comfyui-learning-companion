---
key: 图片生成/图生图/Qwen image 2.1 turbo图生图 快速改图直出方案_2110353791806697473.json
name: Qwen image 2.1 turbo图生图 快速改图直出方案_2110353791806697473
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 turbo图生图 快速改图直出方案_2110353791806697473.json
hash: b7e4b31861237491
coverage: 0.857143
learned_at: 2026-10-23 11:13:54
nodes: [VAEDecode, ResolutionSelector, BatchImagesNode, LoadImage, EmptyLatentImage, ComfySwitchNode, PrimitiveStringMultiline, CLIPLoader, TextEncodeQwenImage21, easy showAnything, VAELoader, LoadImage, SaveImage, PrimitiveBoolean, TextGenerateLTX2Prompt, CLIPLoader, UNETLoader, SamplerCustom, KSamplerSelect, ManualSigmas, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1 turbo图生图 快速改图直出方案_2110353791806697473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 turbo图生图 快速改图直出方案_2110353791806697473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `VAEDecode` ★核心
- `ResolutionSelector`
- `BatchImagesNode`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `VAELoader`
- `LoadImage`
- `SaveImage`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **86%**（42/49）

**有卡**：`VAEDecode`、`ResolutionSelector`、`BatchImagesNode`、`LoadImage`、`EmptyLatentImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`VAELoader`、`SaveImage`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`UNETLoader`、`SamplerCustom`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
