---
key: 图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json
name: Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json
hash: a9a64a182ca669e5
coverage: 0.854839
learned_at: 2026-10-10 20:48:00
nodes: [TextEncodeQwenImage21, QwenImage21Cache, PreviewAny, SaveImageAdvanced, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextGenerate, PrimitiveStringMultiline, EmptyLatentImage, UNETLoader, CLIPLoader, PrimitiveStringMultiline, ComfySwitchNode, SeedNode, CLIPLoader, PrimitiveBoolean, StringConcatenate, Textbox, VAEDecode, ResolutionSelector, ComfySwitchNode, PrimitiveBoolean, VAELoader, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（62 个）：
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `PreviewAny`
- `SaveImageAdvanced`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `SeedNode`
- `CLIPLoader`
- `PrimitiveBoolean`
- `StringConcatenate`
- `Textbox`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `VAELoader`
- `KSampler` ★核心
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

覆盖率 **85%**（53/62）

**有卡**：`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImageAdvanced`、`SaveImage`、`LoadImage`、`TextGenerate`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`SeedNode`、`PrimitiveBoolean`、`StringConcatenate`、`Textbox`、`VAEDecode`、`ResolutionSelector`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
