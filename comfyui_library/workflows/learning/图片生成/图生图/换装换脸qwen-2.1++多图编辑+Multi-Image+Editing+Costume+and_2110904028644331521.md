---
key: 图片生成/图生图/换装换脸qwen-2.1++多图编辑+Multi-Image+Editing+Costume+and_2110904028644331521.json
name: 换装换脸qwen-2.1++多图编辑+Multi-Image+Editing+Costume+and_2110904028644331521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换装换脸qwen-2.1++多图编辑+Multi-Image+Editing+Costume+and_2110904028644331521.json
hash: a7086589b9434812
coverage: 0.862069
learned_at: 2026-10-23 13:02:03
nodes: [UNETLoader, GetImageSize, EmptyLatentImage, CLIPLoader, VAELoader, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageConcatMulti, ImageConcatMulti, KSampler, ShowText|pysssss, VAEDecode, XinbaoImageStandardizer, Image Comparer (rgthree), LoadImage, QwenPERewriteT8, ImpactInt, easy imageScaleDownToSize, CR Text, Note, LoadImage, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 79744654667545, "steps": 25, "width": 1088}
---

# 图片生成/图生图/换装换脸qwen-2.1++多图编辑+Multi-Image+Editing+Costume+and_2110904028644331521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换装换脸qwen-2.1++多图编辑+Multi-Image+Editing+Costume+and_2110904028644331521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
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
- `QwenPERewriteT8`
- `ImpactInt`
- `easy imageScaleDownToSize`
- `CR Text`
- `Note`
- `LoadImage`
- `SaveImage`
- `SaveImage`

## 关键参数

- `width` = `1088`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `79744654667545`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`UNETLoader`、`GetImageSize`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`、`ImageConcatMulti`、`KSampler`、`VAEDecode`、`XinbaoImageStandardizer`、`QwenPERewriteT8`、`ImpactInt`、`easy imageScaleDownToSize`、`CR Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
