---
key: 图片生成/图生图/Qwen Image 2.1自由角度、光影、表情生成人物资产集_2106702976722231298.json
name: Qwen Image 2.1自由角度、光影、表情生成人物资产集_2106702976722231298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1自由角度、光影、表情生成人物资产集_2106702976722231298.json
hash: f49f7367a54af261
coverage: 0.714286
learned_at: 2026-10-21 00:42:45
nodes: [UNETLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, ResolutionSelector, KSampler, TextEncodeQwenImage21, LoadImage, Fast Groups Bypasser (rgthree), 孤海注释, Text Load Line From File, StringConcatenate, StringConcatenate, StringConcatenate, PreviewImage, easy showAnything, easy showAnything, easy showAnything, ImpactWildcardProcessor, Text Multiline, PrimitiveInt, ImageResizeKJv2, TTResolutionSelector, CLIPLoader, SaveImage, SaveImageKJ, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1.2, "denoise": 1, "height": 1024, "sampler_name": "euler_cfg_pp", "scheduler": "simple", "seed": 1052935475886122, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1自由角度、光影、表情生成人物资产集_2106702976722231298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1自由角度、光影、表情生成人物资产集_2106702976722231298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `ResolutionSelector`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `孤海注释`
- `Text Load Line From File`
- `StringConcatenate`
- `StringConcatenate`
- `StringConcatenate`
- `PreviewImage`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ImpactWildcardProcessor`
- `Text Multiline`
- `PrimitiveInt`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `CLIPLoader`
- `SaveImage`
- `SaveImageKJ`
- `VAEDecode` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1052935475886122`
- `steps` = `30`
- `cfg` = `1.2`
- `sampler_name` = `euler_cfg_pp`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（20/28）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`ResolutionSelector`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`Text Load Line From File`、`StringConcatenate`、`ImpactWildcardProcessor`、`Text Multiline`、`ImageResizeKJv2`、`TTResolutionSelector`、`CLIPLoader`、`SaveImage`、`SaveImageKJ`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
