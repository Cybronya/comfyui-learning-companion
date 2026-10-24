---
key: 图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json
name: Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json
hash: a03fcb9e9327e4aa
coverage: 0.875
learned_at: 2026-10-23 11:16:23
nodes: [QwenImage21Cache, CLIPLoader, VAELoader, KSampler, UNETLoader, SaveImage, Image Comparer (rgthree), EmptyLatentImage, GetImageSize, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoadImage, TextEncodeQwenImage21, LoraLoaderModelOnly, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1124641598826094, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1 一致性保持+图像编辑_2108882050051825665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心

## 关键参数

- `seed` = `1124641598826094`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`KSampler`、`UNETLoader`、`SaveImage`、`EmptyLatentImage`、`GetImageSize`、`ResolutionSelector`、`LoadImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
