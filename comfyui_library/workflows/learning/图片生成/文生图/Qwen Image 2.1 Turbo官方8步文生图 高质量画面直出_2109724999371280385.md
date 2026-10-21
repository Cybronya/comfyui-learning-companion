---
key: 图片生成/文生图/Qwen Image 2.1 Turbo官方8步文生图 高质量画面直出_2109724999371280385.json
name: Qwen Image 2.1 Turbo官方8步文生图 高质量画面直出_2109724999371280385
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Turbo官方8步文生图 高质量画面直出_2109724999371280385.json
hash: 0aeb6e9bd27f30e8
coverage: 0.837209
learned_at: 2026-10-21 02:54:04
nodes: [UNETLoader, CLIPLoader, VAELoader, KSamplerSelect, VAEDecode, ManualSigmas, SaveImage, SamplerCustom, ResolutionSelector, EmptyLatentImage, easy showAnything, easy showAnything, TextEncodeQwenImage21, JjkText, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 Turbo官方8步文生图 高质量画面直出_2109724999371280385.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 Turbo官方8步文生图 高质量画面直出_2109724999371280385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（43 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `ManualSigmas`
- `SaveImage`
- `SamplerCustom` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `JjkText`
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

覆盖率 **84%**（36/43）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSamplerSelect`、`VAEDecode`、`ManualSigmas`、`SaveImage`、`SamplerCustom`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
