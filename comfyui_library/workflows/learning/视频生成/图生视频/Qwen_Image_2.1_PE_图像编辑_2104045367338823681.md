---
key: 视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json
name: Qwen_Image_2.1_PE_图像编辑_2104045367338823681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json
hash: 7221ccea072aed4a
coverage: 0.851852
learned_at: 2026-10-17 02:29:18
nodes: [Note, UNETLoader, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, SaveImage, easy cleanGpuUsed, KSampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, QwenPERewriteT8, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_Image_2.1_PE_图像编辑_2104045367338823681.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `SaveImage`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `QwenPERewriteT8`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（23/27）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`SaveImage`、`easy cleanGpuUsed`、`KSampler`、`LoadImage`、`CR Prompt Text`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
