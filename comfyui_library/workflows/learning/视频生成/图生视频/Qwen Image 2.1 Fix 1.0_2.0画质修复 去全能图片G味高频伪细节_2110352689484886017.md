---
key: 视频生成/图生视频/Qwen Image 2.1 Fix 1.0_2.0画质修复 去全能图片G味高频伪细节_2110352689484886017.json
name: Qwen Image 2.1 Fix 1.0_2.0画质修复 去全能图片G味高频伪细节_2110352689484886017
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1 Fix 1.0_2.0画质修复 去全能图片G味高频伪细节_2110352689484886017.json
hash: 171a0fa350270402
coverage: 0.647059
learned_at: 2026-10-18 00:23:45
nodes: [VAEDecode, SeedNode, EmptyLatentImage, TextEncodeQwenImage21, TextGenerate, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, RegexExtract, ComfySwitchNode, StringConcatenate, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, VAELoader, PrimitiveNode, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, PrimitiveNode, StringConcatenate, UNETLoader, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, LoraLoaderModelOnly, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen Image 2.1 Fix 1.0_2.0画质修复 去全能图片G味高频伪细节_2110352689484886017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1 Fix 1.0_2.0画质修复 去全能图片G味高频伪细节_2110352689484886017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（68 个）：
- `VAEDecode` ★核心
- `SeedNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextGenerate`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `RegexExtract`
- `ComfySwitchNode`
- `StringConcatenate`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveNode`
- `StringConcatenate`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
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

覆盖率 **65%**（44/68）

**有卡**：`VAEDecode`、`SeedNode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerate`、`KSamplerAdvanced`、`RegexExtract`、`StringConcatenate`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`、`SaveImage`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
