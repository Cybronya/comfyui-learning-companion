---
key: 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122.json
name: qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122.json
hash: e96ab3874a025d29
coverage: 0.844444
learned_at: 2026-10-21 02:57:27
nodes: [VAEDecode, VAELoader, CLIPLoader, CLIPLoader, SaveImage, TextEncodeQwenImage21, easy showAnything, KSamplerSelect, TextGenerateLTX2Prompt, EmptyLatentImage, PrimitiveStringMultiline, SamplerCustom, ManualSigmas, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1 rurbo文生图，高清创意直出_2111281294968709122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `KSamplerSelect` ★核心
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `SamplerCustom` ★核心
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader` ★核心
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

覆盖率 **84%**（38/45）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`KSamplerSelect`、`TextGenerateLTX2Prompt`、`EmptyLatentImage`、`SamplerCustom`、`ManualSigmas`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
