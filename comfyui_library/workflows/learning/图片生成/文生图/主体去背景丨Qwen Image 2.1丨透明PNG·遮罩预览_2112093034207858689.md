---
key: 图片生成/文生图/主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689.json
name: 主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689.json
hash: f2e193c4a0a9f3ec
coverage: 0.823529
learned_at: 2026-10-21 02:58:30
nodes: [LoadImage, UNETLoader, CLIPLoader, VAELoader, PrimitiveInt, QwenImage21Cache, ImageResizeKJv2, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, KSampler, VAEDecode, SaveImage, SplitImageWithAlpha, MaskToImage, SaveImage, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 1027301785644970, "steps": 25, "width": 960}
---

# 图片生成/文生图/主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/主体去背景丨Qwen Image 2.1丨透明PNG·遮罩预览_2112093034207858689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveInt`
- `QwenImage21Cache`
- `ImageResizeKJv2`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SplitImageWithAlpha`
- `MaskToImage`
- `SaveImage`
- `JjkText`

## 关键参数

- `width` = `960`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `1027301785644970`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`ImageResizeKJv2`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`SplitImageWithAlpha`、`MaskToImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
