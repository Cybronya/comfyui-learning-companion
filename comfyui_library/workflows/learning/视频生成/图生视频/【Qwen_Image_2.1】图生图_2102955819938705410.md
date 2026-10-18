---
key: 视频生成/图生视频/【Qwen_Image_2.1】图生图_2102955819938705410.json
name: 【Qwen_Image_2.1】图生图_2102955819938705410
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【Qwen_Image_2.1】图生图_2102955819938705410.json
hash: 30da845dded3be36
coverage: 0.708333
learned_at: 2026-10-17 02:29:40
nodes: [LayerUtility: ImageReelComposit, PreviewImage, LayerUtility: ImageReel, TextEncodeQwenImage21, ComfySwitchNode, SaveImage, easy setNode, UNETLoader, QwenImage21Cache, VAELoader, KSampler, TextGenerateLTX2Prompt, EmptyLatentImage, ShowText|pysssss, ResolutionSelector, CLIPLoader, CR Prompt Text, GetNode, SetNode, Image Comparer (rgthree), VAEDecode, LoadImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 301307552057284, "steps": 40, "width": 1024}
---

# 视频生成/图生视频/【Qwen_Image_2.1】图生图_2102955819938705410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【Qwen_Image_2.1】图生图_2102955819938705410.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `SaveImage`
- `easy setNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `ShowText|pysssss`
- `ResolutionSelector`
- `CLIPLoader`
- `CR Prompt Text`
- `GetNode`
- `SetNode`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `LoadImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `301307552057284`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`SaveImage`、`easy setNode`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`KSampler`、`TextGenerateLTX2Prompt`、`EmptyLatentImage`、`ResolutionSelector`、`CLIPLoader`、`CR Prompt Text`、`VAEDecode`、`LoadImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
