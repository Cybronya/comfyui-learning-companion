---
key: 图片生成/文生图/Qwen编辑 AIO 1.2_2006990923732885505.json
name: Qwen编辑 AIO 1.2_2006990923732885505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen编辑 AIO 1.2_2006990923732885505.json
hash: aae00ea22c07e562
coverage: 0.727273
learned_at: 2026-10-19 22:00:55
nodes: [Anything Everywhere3, LoadImage, CheckpointLoaderSimple, CLIPLoader, LoraLoaderModelOnly, LoadImage, QwenImageIntegratedKSampler, SaveImage, Image Comparer (rgthree), EmptyLatentImage, PrimitiveNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "e6093d0b626b2a046868f0fc1b5b98962608194df5d2dcbd3f2f737401897c47.safetensors", "denoise": 204857165212271, "height": 1720, "sampler_name": 1280, "scheduler": 1720, "seed": "让图1的女孩带上图2的帽子", "steps": "图生图 image-to-image", "width": 1280}
---

# 图片生成/文生图/Qwen编辑 AIO 1.2_2006990923732885505.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen编辑 AIO 1.2_2006990923732885505.json`

## 结构

**生成流程**：Model → Latent → Sampling → Output → Other

**节点**（11 个）：
- `Anything Everywhere3`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `QwenImageIntegratedKSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `PrimitiveNode`

## 关键参数

- `checkpoint` = `e6093d0b626b2a046868f0fc1b5b98962608194df5d2dcbd3f2f737401897c47.safetensors`
- `seed` = `让图1的女孩带上图2的帽子`
- `steps` = `图生图 image-to-image`
- `cfg` = `1`
- `sampler_name` = `1280`
- `scheduler` = `1720`
- `denoise` = `204857165212271`
- `width` = `1280`
- `height` = `1720`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（8/11）

**有卡**：`LoadImage`、`CheckpointLoaderSimple`、`CLIPLoader`、`LoraLoaderModelOnly`、`QwenImageIntegratedKSampler`、`SaveImage`、`EmptyLatentImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、EmptyLatentImage、LoadImage、QwenImageIntegratedKSampler、SaveImage、KSampler
