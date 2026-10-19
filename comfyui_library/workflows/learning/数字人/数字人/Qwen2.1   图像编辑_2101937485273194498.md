---
key: 数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json
name: Qwen2.1   图像编辑_2101937485273194498
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json
hash: c59db9a3d8fdbcdd
coverage: 0.52381
learned_at: 2026-10-19 00:19:13
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, QwenImage21Cache, SetNode, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, SetNode, LoadImage, LoadImage, SetNode, LoadImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, TextEncodeQwenImage21, PreviewImage, GetNode, VAEDecode, SaveImage, GH_ImageVideoComparer, UNETLoader, KSampler, FastGroupsBypassSwitch, ResolutionSelector, FastGroupsBypassSwitch, LoadImage, Fast Groups Bypasser (rgthree), QwenPERewriteT8, JjkText, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 45, "width": 1024}
---

# 数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Qwen2.1   图像编辑_2101937485273194498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `GetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `GH_ImageVideoComparer`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `FastGroupsBypassSwitch`
- `ResolutionSelector`
- `FastGroupsBypassSwitch`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `QwenPERewriteT8`
- `JjkText`
- `easy showAnything`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `45`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（22/42）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`GH_ImageVideoComparer`、`UNETLoader`、`KSampler`、`FastGroupsBypassSwitch`、`ResolutionSelector`、`QwenPERewriteT8`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
