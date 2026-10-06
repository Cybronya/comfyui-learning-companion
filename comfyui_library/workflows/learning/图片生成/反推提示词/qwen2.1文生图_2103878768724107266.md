---
key: 图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json
name: qwen2.1文生图_2103878768724107266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json
hash: a6a480612725b455
coverage: 0.736842
learned_at: 2026-10-06 22:27:30
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEDecode, ResolutionSelector, PreviewAny, StringReplace, EmptyLatentImage, TextEncodeQwenImage21, KSampler, SaveImage, StringConstantMultiline, StringConstantMultiline, CLIPLoader, TextGenerate, easy showAnything, easy showAnything, StringFunction|pysssss, Note]
patterns: []
missing: [StringFunction|pysssss]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 40, "width": 1024}
discoveries: [次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识]
---

# 图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/qwen2.1文生图_2103878768724107266.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `PreviewAny`
- `StringReplace`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `SaveImage`
- `StringConstantMultiline`
- `StringConstantMultiline`
- `CLIPLoader`
- `TextGenerate`
- `easy showAnything`
- `easy showAnything`
- `StringFunction|pysssss`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ResolutionSelector`、`StringReplace`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`SaveImage`、`StringConstantMultiline`、`TextGenerate`

**缺卡**（1）：`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 学习发现

- 次要节点 `StringFunction|pysssss` 知识库中没有该节点类型的任何知识
