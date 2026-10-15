---
key: 图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json
name: Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json
hash: e524efb7e34d1979
coverage: 0.901235
learned_at: 2026-10-10 20:58:50
nodes: [ResolutionSelector, EmptyLatentImage, AIO_Preprocessor, GetImageSize, PreviewImage, PreviewImage, ImageScaleBy, ImageResizeKJv2, LoadImage, LoadImage, ImageResizeKJv2, SaveImage, SeedNode, KSampler, VAEDecode, CLIPLoader, Textbox, Textbox, TextEncodeQwenImage21, UNETLoader, ResizeImageMaskNode, VAELoader, QwenImage21UnionLoader, QwenImage21Cache, QwenImage21UnionApply, ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 ControlNet图像编辑工作流，精准控制改图图生图工具_2105806539499069442.json`

## 结构

**节点**（81 个）：
- `ResolutionSelector`
- `EmptyLatentImage`
- `AIO_Preprocessor`
- `GetImageSize`
- `PreviewImage`
- `PreviewImage`
- `ImageScaleBy`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `SaveImage`
- `SeedNode`
- `KSampler`
- `VAEDecode`
- `CLIPLoader`
- `Textbox`
- `Textbox`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `ResizeImageMaskNode`
- `VAELoader`
- `QwenImage21UnionLoader`
- `QwenImage21Cache`
- `QwenImage21UnionApply`
- `ComfySwitchNode`
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

覆盖率 **90%**（73/81）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`AIO_Preprocessor`、`GetImageSize`、`PreviewImage`、`ImageScaleBy`、`ImageResizeKJv2`、`LoadImage`、`SaveImage`、`SeedNode`、`KSampler`、`VAEDecode`、`CLIPLoader`、`Textbox`、`TextEncodeQwenImage21`、`UNETLoader`、`ResizeImageMaskNode`、`VAELoader`、`QwenImage21UnionLoader`、`QwenImage21Cache`、`QwenImage21UnionApply`、`ComfySwitchNode`、`LoraLoaderModelOnly`、`JjkText`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`孤海注释`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
