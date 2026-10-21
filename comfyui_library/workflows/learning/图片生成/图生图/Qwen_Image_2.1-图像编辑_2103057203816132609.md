---
key: 图片生成/图生图/Qwen_Image_2.1-图像编辑_2103057203816132609.json
name: Qwen_Image_2.1-图像编辑_2103057203816132609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1-图像编辑_2103057203816132609.json
hash: d7dbe4b17b28558a
coverage: 0.923077
learned_at: 2026-10-21 00:43:55
nodes: [CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, VAELoader, QwenImage21Cache, VAEDecode, KSampler, UNETLoader, SaveImage, ResolutionSelector, JjkText, LoadImage, QwenPERewriteT8]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 997026444462722, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen_Image_2.1-图像编辑_2103057203816132609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1-图像编辑_2103057203816132609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `ResolutionSelector`
- `JjkText`
- `LoadImage`
- `QwenPERewriteT8`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `997026444462722`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`UNETLoader`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`QwenPERewriteT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
