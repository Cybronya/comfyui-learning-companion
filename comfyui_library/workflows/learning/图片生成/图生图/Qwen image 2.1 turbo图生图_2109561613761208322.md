---
key: 图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json
name: Qwen image 2.1 turbo图生图_2109561613761208322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json
hash: 7ce724c2a6ea38f3
coverage: 0.85
learned_at: 2026-10-23 11:13:55
nodes: [VAEDecode, ResolutionSelector, BatchImagesNode, LoadImage, EmptyLatentImage, ComfySwitchNode, PrimitiveStringMultiline, CLIPLoader, TextEncodeQwenImage21, easy showAnything, VAELoader, LoadImage, SaveImage, PrimitiveBoolean, TextGenerateLTX2Prompt, CLIPLoader, UNETLoader, SamplerCustom, KSamplerSelect, ManualSigmas]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 turbo图生图_2109561613761208322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAEDecode` ★核心
- `ResolutionSelector`
- `BatchImagesNode`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `VAELoader`
- `LoadImage`
- `SaveImage`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`VAEDecode`、`ResolutionSelector`、`BatchImagesNode`、`LoadImage`、`EmptyLatentImage`、`CLIPLoader`、`TextEncodeQwenImage21`、`VAELoader`、`SaveImage`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`UNETLoader`、`SamplerCustom`、`KSamplerSelect`、`ManualSigmas`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、UNETLoader
