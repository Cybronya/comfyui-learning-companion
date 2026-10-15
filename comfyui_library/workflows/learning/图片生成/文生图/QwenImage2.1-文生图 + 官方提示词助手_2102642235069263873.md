---
key: 图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json
name: QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json
hash: f39407d2547d2699
coverage: 0.736842
learned_at: 2026-10-10 20:59:07
nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, PrimitiveStringMultiline, VAEDecode, TextConcatenator, TextGenerate, CLIPLoader, JsonExtractString, VAELoader, Any Switch (rgthree), UNETLoader, SaveImageAdvanced, SaveImage, ShowAnything|Mie, TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline]
patterns: []
missing: [ShowAnything|Mie]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 0, "steps": 30, "width": 1560}
discoveries: [次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImage2.1-文生图 + 官方提示词助手_2102642235069263873.json`

## 结构

**节点**（19 个）：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `VAEDecode`
- `TextConcatenator`
- `TextGenerate`
- `CLIPLoader`
- `JsonExtractString`
- `VAELoader`
- `Any Switch (rgthree)`
- `UNETLoader`
- `SaveImageAdvanced`
- `SaveImage`
- `ShowAnything|Mie`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1080`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `seed` = `0`
- `steps` = `30`
- `width` = `1560`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`PrimitiveStringMultiline`、`VAEDecode`、`TextConcatenator`、`TextGenerate`、`JsonExtractString`、`VAELoader`、`Any Switch (rgthree)`、`UNETLoader`、`SaveImageAdvanced`

**缺卡**（1）：`ShowAnything|Mie`

## 学习发现

- 次要节点 `ShowAnything|Mie` 知识库中没有该节点类型的任何知识
