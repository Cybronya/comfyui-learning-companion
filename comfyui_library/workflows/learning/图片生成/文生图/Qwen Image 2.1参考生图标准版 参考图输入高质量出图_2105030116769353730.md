---
key: 图片生成/文生图/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json
name: Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json
hash: f6509276bd25d0c2
coverage: 0.844444
learned_at: 2026-10-10 21:27:43
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, TextGenerate, PrimitiveStringMultiline, PreviewAny, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, LoadImage, CR Text, ResolutionSelector, CLIPLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1参考生图标准版 参考图输入高质量出图_2105030116769353730.json`

## 结构

**节点**（45 个）：
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `LoadImage`
- `CR Text`
- `ResolutionSelector`
- `CLIPLoader`
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

覆盖率 **84%**（38/45）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerate`、`PrimitiveStringMultiline`、`PreviewAny`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`CR Text`、`ResolutionSelector`、`孤海注释`、`LoraLoaderModelOnly`、`JjkText`

**缺卡**（1）：`CR Text`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
