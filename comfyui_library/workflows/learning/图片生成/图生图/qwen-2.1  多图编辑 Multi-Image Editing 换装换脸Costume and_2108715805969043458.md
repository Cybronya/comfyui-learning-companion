---
key: 图片生成/图生图/qwen-2.1  多图编辑 Multi-Image Editing 换装换脸Costume and_2108715805969043458.json
name: qwen-2.1  多图编辑 Multi-Image Editing 换装换脸Costume and_2108715805969043458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-2.1  多图编辑 Multi-Image Editing 换装换脸Costume and_2108715805969043458.json
hash: eb54df2634cdc6c7
coverage: 0.862069
learned_at: 2026-10-23 11:42:12
nodes: [SaveImage, UNETLoader, GetImageSize, EmptyLatentImage, CLIPLoader, VAELoader, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageConcatMulti, ImageConcatMulti, KSampler, ShowText|pysssss, VAEDecode, XinbaoImageStandardizer, Image Comparer (rgthree), LoadImage, LoadImage, QwenPERewriteT8, ImpactInt, easy imageScaleDownToSize, CR Text, Note, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 1097390802690512, "steps": 25, "width": 1088}
---

# 图片生成/图生图/qwen-2.1  多图编辑 Multi-Image Editing 换装换脸Costume and_2108715805969043458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-2.1  多图编辑 Multi-Image Editing 换装换脸Costume and_2108715805969043458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `SaveImage`
- `UNETLoader` ★核心
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `KSampler` ★核心
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `XinbaoImageStandardizer`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `ImpactInt`
- `easy imageScaleDownToSize`
- `CR Text`
- `Note`
- `SaveImage`

## 关键参数

- `width` = `1088`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `1097390802690512`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`SaveImage`、`UNETLoader`、`GetImageSize`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`、`ImageConcatMulti`、`KSampler`、`VAEDecode`、`XinbaoImageStandardizer`、`QwenPERewriteT8`、`ImpactInt`、`easy imageScaleDownToSize`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
