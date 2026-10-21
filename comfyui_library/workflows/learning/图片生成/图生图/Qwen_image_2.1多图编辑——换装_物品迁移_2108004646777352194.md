---
key: 图片生成/图生图/Qwen_image_2.1多图编辑——换装_物品迁移_2108004646777352194.json
name: Qwen_image_2.1多图编辑——换装_物品迁移_2108004646777352194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1多图编辑——换装_物品迁移_2108004646777352194.json
hash: bcd9a4ad62b21d80
coverage: 0.909091
learned_at: 2026-10-21 00:44:03
nodes: [LoadImage, LoadImage, LoadImage, CR Text, Image Comparer (rgthree), VAEDecode, KSampler, TextEncodeQwenImage21, UNETLoader, CLIPLoader, EmptyLatentImage, CR Text, VAELoader, GetImageSize, SaveImage, ImageConcatMulti, ImageConcatMulti, PreviewImage, LoadImage, 图像缩放V2_孤海, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 708321398114453, "steps": 25, "width": 1088}
---

# 图片生成/图生图/Qwen_image_2.1多图编辑——换装_物品迁移_2108004646777352194.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1多图编辑——换装_物品迁移_2108004646777352194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `CR Text`
- `VAELoader`
- `GetImageSize`
- `SaveImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `LoadImage`
- `图像缩放V2_孤海`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `708321398114453`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1088`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`LoadImage`、`CR Text`、`VAEDecode`、`KSampler`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`GetImageSize`、`SaveImage`、`ImageConcatMulti`、`图像缩放V2_孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
