---
key: 图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104885905218691074.json
name: Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104885905218691074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104885905218691074.json
hash: 0c020efc8166b9e5
coverage: 0.821429
learned_at: 2026-10-10 20:59:08
nodes: [ResolutionSelector, EmptyLatentImage, AIO_Preprocessor, GetImageSize, PreviewImage, PreviewImage, ImageScaleBy, ImageResizeKJv2, Label (rgthree), ImageResizeKJv2, SaveImage, SeedNode, KSampler, VAEDecode, CLIPLoader, Textbox, TextEncodeQwenImage21, UNETLoader, ResizeImageMaskNode, VAELoader, QwenImage21UnionLoader, QwenImage21Cache, Note, QwenImage21UnionApply, ComfySwitchNode, Textbox, LoadImage, LoadImage]
patterns: []
missing: [Label (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 40, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104885905218691074.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104885905218691074.json`

## 结构

**节点**（28 个）：
- `ResolutionSelector`
- `EmptyLatentImage`
- `AIO_Preprocessor`
- `GetImageSize`
- `PreviewImage`
- `PreviewImage`
- `ImageScaleBy`
- `ImageResizeKJv2`
- `Label (rgthree)`
- `ImageResizeKJv2`
- `SaveImage`
- `SeedNode`
- `KSampler`
- `VAEDecode`
- `CLIPLoader`
- `Textbox`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `ResizeImageMaskNode`
- `VAELoader`
- `QwenImage21UnionLoader`
- `QwenImage21Cache`
- `Note`
- `QwenImage21UnionApply`
- `ComfySwitchNode`
- `Textbox`
- `LoadImage`
- `LoadImage`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `43`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`AIO_Preprocessor`、`GetImageSize`、`PreviewImage`、`ImageScaleBy`、`ImageResizeKJv2`、`Label (rgthree)`、`SaveImage`、`SeedNode`、`KSampler`、`VAEDecode`、`CLIPLoader`、`Textbox`、`TextEncodeQwenImage21`、`UNETLoader`、`ResizeImageMaskNode`、`VAELoader`、`QwenImage21UnionLoader`、`QwenImage21Cache`、`Note`

**缺卡**（1）：`Label (rgthree)`

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
