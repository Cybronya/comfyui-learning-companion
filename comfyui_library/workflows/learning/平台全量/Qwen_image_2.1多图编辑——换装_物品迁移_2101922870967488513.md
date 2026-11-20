---
key: 平台全量/Qwen_image_2.1多图编辑——换装_物品迁移_2101922870967488513.json
name: Qwen_image_2.1多图编辑——换装_物品迁移_2101922870967488513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen_image_2.1多图编辑——换装_物品迁移_2101922870967488513.json
hash: 0254bea6430b0626
coverage: 0.954545
learned_at: 2026-11-14 00:53:33
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Text, LoadImage, ImageConcatMulti, ImageConcatMulti, Image Comparer (rgthree), SaveImage, VAEDecode, SaveImage, KSampler, TextEncodeQwenImage21, UNETLoader, CLIPLoader, EmptyLatentImage, CR Text, VAELoader, 图像缩放V2_孤海, GetImageSize]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 601071881222040, "steps": 25, "width": 1088}
---

# 平台全量/Qwen_image_2.1多图编辑——换装_物品迁移_2101922870967488513.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen_image_2.1多图编辑——换装_物品迁移_2101922870967488513.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `LoadImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `CR Text`
- `VAELoader`
- `图像缩放V2_孤海`
- `GetImageSize`

## 关键参数

- `seed` = `601071881222040`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1088`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`LoadImage`、`CR Text`、`ImageConcatMulti`、`SaveImage`、`VAEDecode`、`KSampler`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`图像缩放V2_孤海`、`GetImageSize`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
