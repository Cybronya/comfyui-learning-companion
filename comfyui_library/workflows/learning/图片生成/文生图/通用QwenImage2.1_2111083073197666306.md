---
key: 图片生成/文生图/通用QwenImage2.1_2111083073197666306.json
name: 通用QwenImage2.1_2111083073197666306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/通用QwenImage2.1_2111083073197666306.json
hash: 90c1f5cd21a87df3
coverage: 0.727273
learned_at: 2026-10-21 03:03:11
nodes: [TextGenerate, easy showAnything, PrimitiveStringMultiline, easy showAnything, UNETLoader, CLIPLoader, VAELoader, KSampler, QwenImage21Cache, ComfySwitchNode, PrimitiveStringMultiline, CLIPLoader, CLIPLoader, easy isNone, JsonExtractString, TextConcatenator, ComfySwitchNode, easy showAnything, PrimitiveStringMultiline, EmptyLatentImage, SaveImage, VAEDecode, Any Switch (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 739134992175956, "steps": 30, "width": 1024}
---

# 图片生成/文生图/通用QwenImage2.1_2111083073197666306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/通用QwenImage2.1_2111083073197666306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（33 个）：
- `TextGenerate`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `CLIPLoader`
- `easy isNone`
- `JsonExtractString`
- `TextConcatenator`
- `ComfySwitchNode`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `739134992175956`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（24/33）

**有卡**：`TextGenerate`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`easy isNone`、`JsonExtractString`、`TextConcatenator`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
