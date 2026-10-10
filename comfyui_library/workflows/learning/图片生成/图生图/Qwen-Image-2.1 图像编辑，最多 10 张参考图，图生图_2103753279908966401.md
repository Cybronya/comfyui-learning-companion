---
key: 图片生成/图生图/Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401.json
name: Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401.json
hash: a25e7779f0fa2ce7
coverage: 0.343284
learned_at: 2026-10-10 20:48:09
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, SetNode, SetNode, SetNode, LoadImage, MarkdownNote, LoadImage, SaveImage, GetNode, GetNode, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, ResolutionSelector, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), SetNode, SetNode, SetNode, GetNode, LoadImage, LoadImage, LoadImage, UNETLoader, GetNode, GetNode, CLIPLoader, CLIPLoader, VAELoader, GetNode, GetNode, GetNode, EmptyLatentImage, GetNode, TextGenerateLTX2Prompt, KSampler, ComfySwitchNode, QwenImage21Cache, SetNode, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, GetNode, BatchImagesNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1045621175892264, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 图像编辑，最多 10 张参考图，图生图_2103753279908966401.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `BatchImagesNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1045621175892264`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **34%**（23/67）

**有卡**：`LoadImage`、`SaveImage`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`KSampler`、`QwenImage21Cache`、`VAEDecode`、`TextEncodeQwenImage21`、`BatchImagesNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
