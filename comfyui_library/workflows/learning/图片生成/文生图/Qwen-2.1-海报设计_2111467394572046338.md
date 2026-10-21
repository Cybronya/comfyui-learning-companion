---
key: 图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json
name: Qwen-2.1-海报设计_2111467394572046338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json
hash: ae07cbec3470dba5
coverage: 0.714286
learned_at: 2026-10-21 02:54:23
nodes: [UNETLoader, CLIPLoader, VAELoader, PreviewImage, PrimitiveStringMultiline, Image Comparer (rgthree), KSampler, LayerUtility: ImageReelComposit, EmptyLatentImage, QwenImage21Cache, KSampler, PreviewImage, VAEDecode, CR Seed, PreviewImage, LayerUtility: ImageReel, VAEDecode, TextEncodeQwenImage21, LoraLoaderModelOnly, Note, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 1019314273711665, "steps": 25, "width": 1920}
---

# 图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-2.1-海报设计_2111467394572046338.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `CR Seed`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `SaveImage`

## 关键参数

- `seed` = `1019314273711665`
- `steps` = `25`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（15/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`LayerUtility: ImageReelComposit`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`CR Seed`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、QwenImage21Cache
