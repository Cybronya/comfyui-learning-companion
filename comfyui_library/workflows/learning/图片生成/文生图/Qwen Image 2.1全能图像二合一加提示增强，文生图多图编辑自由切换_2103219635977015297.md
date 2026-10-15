---
key: 图片生成/文生图/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json
name: Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json
hash: aeb765a152f92c0c
coverage: 0.854839
learned_at: 2026-10-10 21:27:42
nodes: [TextEncodeQwenImage21, QwenImage21Cache, PreviewAny, SaveImageAdvanced, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextGenerate, PrimitiveStringMultiline, EmptyLatentImage, UNETLoader, CLIPLoader, PrimitiveStringMultiline, ComfySwitchNode, SeedNode, CLIPLoader, PrimitiveBoolean, StringConcatenate, Textbox, VAEDecode, ResolutionSelector, ComfySwitchNode, PrimitiveBoolean, VAELoader, KSampler, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1全能图像二合一加提示增强，文生图多图编辑自由切换_2103219635977015297.json`

## 结构

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
- `EmptyLatentImage`
- `UNETLoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `SeedNode`
- `CLIPLoader`
- `PrimitiveBoolean`
- `StringConcatenate`
- `Textbox`
- `VAEDecode`
- `ResolutionSelector`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `VAELoader`
- `KSampler`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **85%**（53/62）

**有卡**：`TextEncodeQwenImage21`、`QwenImage21Cache`、`PreviewAny`、`SaveImageAdvanced`、`SaveImage`、`LoadImage`、`TextGenerate`、`PrimitiveStringMultiline`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`ComfySwitchNode`、`SeedNode`、`PrimitiveBoolean`、`StringConcatenate`、`Textbox`、`VAEDecode`、`ResolutionSelector`、`VAELoader`、`KSampler`、`孤海注释`、`LoraLoaderModelOnly`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
