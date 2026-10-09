---
key: 图片生成/图生图/Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json
name: Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json
hash: 9d51405c3cccc408
coverage: 0.853659
learned_at: 2026-10-09 22:09:17
nodes: [ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, PrimitiveBoolean, 孤海注释, JoinStrings, EmptyLatentImage, ComfySwitchNode, TextGenerate, easy positive, BatchImagesNode, SaveImage, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, ShowText|pysssss, 忽略多组孤海, VAEDecode, KSampler, ResolutionSelector, easy positive, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: [easy positive, easy positive, 忽略多组孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 795189855916023, "steps": 25, "width": 1024}
discoveries: [次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen Image 2.1 图片编辑工作流（官流） 2609_2105934523547602945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2105934523547602945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `PrimitiveBoolean`
- `孤海注释`
- `JoinStrings`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `TextGenerate`
- `easy positive`
- `BatchImagesNode`
- `SaveImage`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `ShowText|pysssss`
- `忽略多组孤海`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ResolutionSelector`
- `easy positive`
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `795189855916023`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`ImageScaleToTotalPixels`、`PrimitiveBoolean`、`JoinStrings`、`EmptyLatentImage`、`TextGenerate`、`BatchImagesNode`、`SaveImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`ResolutionSelector`、`LoadImage`

**缺卡**（3）：`easy positive`、`easy positive`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
