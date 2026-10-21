---
key: 图片生成/文生图/Qwen image 2.1文生图_2101905636907896834.json
name: Qwen image 2.1文生图_2101905636907896834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2101905636907896834.json
hash: eed547ed605cd61b
coverage: 0.954545
learned_at: 2026-10-20 01:51:12
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, SaveImageAdvanced, KSampler, MathExpression|pysssss, Int, Seed Generator, easy batchAnything, SaveImageAdvanced, easy forLoopStart, AnySwitch, UNETLoader, UNETLoader, ResolutionSelector, Int, TextEncodeQwenImage21, JjkText, Fast Bypasser (rgthree), easy forLoopEnd, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 523802227161617, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1文生图_2101905636907896834.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2101905636907896834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `KSampler` ★核心
- `MathExpression|pysssss`
- `Int`
- `Seed Generator`
- `easy batchAnything`
- `SaveImageAdvanced`
- `easy forLoopStart`
- `AnySwitch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `Int`
- `TextEncodeQwenImage21`
- `JjkText`
- `Fast Bypasser (rgthree)`
- `easy forLoopEnd`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `523802227161617`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`SaveImageAdvanced`、`KSampler`、`MathExpression|pysssss`、`Int`、`Seed Generator`、`easy batchAnything`、`easy forLoopStart`、`AnySwitch`、`UNETLoader`、`ResolutionSelector`、`TextEncodeQwenImage21`、`Fast Bypasser (rgthree)`、`easy forLoopEnd`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
