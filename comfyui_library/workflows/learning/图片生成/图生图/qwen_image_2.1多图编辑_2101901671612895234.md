---
key: 图片生成/图生图/qwen_image_2.1多图编辑_2101901671612895234.json
name: qwen_image_2.1多图编辑_2101901671612895234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1多图编辑_2101901671612895234.json
hash: 32cd7cc2926daa0e
coverage: 0.821429
learned_at: 2026-10-10 20:48:13
nodes: [SaveImage, SaveImage, UNETLoader, LoadImage, ImpactInt, easy imageScaleDownToSize, GetImageSize, EmptyLatentImage, CLIPLoader, VAELoader, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, ImageConcatMulti, ImageConcatMulti, KSampler, QwenPERewriteT8, ShowText|pysssss, VAEDecode, XinbaoImageStandardizer, Image Comparer (rgthree)]
patterns: []
missing: [CR Text, easy imageScaleDownToSize]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 36496774754364, "steps": 25, "width": 1088}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageScaleDownToSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/qwen_image_2.1多图编辑_2101901671612895234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1多图编辑_2101901671612895234.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `ImpactInt`
- `easy imageScaleDownToSize`
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
- `LoadImage`
- `CR Text`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `KSampler` ★核心
- `QwenPERewriteT8`
- `ShowText|pysssss`
- `VAEDecode` ★核心
- `XinbaoImageStandardizer`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1088`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `36496774754364`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`SaveImage`、`UNETLoader`、`LoadImage`、`ImpactInt`、`GetImageSize`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`ImageConcatMulti`、`KSampler`、`QwenPERewriteT8`、`VAEDecode`、`XinbaoImageStandardizer`

**缺卡**（2）：`CR Text`、`easy imageScaleDownToSize`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageScaleDownToSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
