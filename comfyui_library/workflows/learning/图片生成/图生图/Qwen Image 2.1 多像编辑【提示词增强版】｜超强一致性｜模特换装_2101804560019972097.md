---
key: 图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json
name: Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json
hash: 26447eeea7694b2f
coverage: 0.552632
learned_at: 2026-10-21 00:42:13
nodes: [SetNode, SetNode, SetNode, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, QwenImage21Cache, ComfySwitchNode, GetNode, GetNode, 忽略多组孤海, GetNode, GetNode, KSampler, LoadImage, LoadImage, LoadImage, SaveImage, EmptyLatentImage, VAEDecode, PreviewAny, BatchImagesNode, TextGenerateLTX2Prompt, GetNode, GetNode, MuyeTextEditOutput, TextEncodeQwenImage21, SetNode, SetNode, SetNode, LoadImage, LoadImage, LoadImage, INTConstant, 孤海注释, 孤海注释, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2400, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1600}
---

# 图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 多像编辑【提示词增强版】｜超强一致性｜模特换装_2101804560019972097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `忽略多组孤海`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `PreviewAny`
- `BatchImagesNode`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `GetNode`
- `MuyeTextEditOutput`
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `INTConstant`
- `孤海注释`
- `孤海注释`
- `孤海注释`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1600`
- `height` = `2400`
- `batch_size` = `1`

## 知识

覆盖率 **55%**（21/38）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`忽略多组孤海`、`KSampler`、`LoadImage`、`SaveImage`、`EmptyLatentImage`、`VAEDecode`、`BatchImagesNode`、`TextGenerateLTX2Prompt`、`MuyeTextEditOutput`、`TextEncodeQwenImage21`、`INTConstant`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、SaveImage、EmptyLatentImage、LoadImage
