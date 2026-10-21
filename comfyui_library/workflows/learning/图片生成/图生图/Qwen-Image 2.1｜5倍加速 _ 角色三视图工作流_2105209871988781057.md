---
key: 图片生成/图生图/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流_2105209871988781057.json
name: Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流_2105209871988781057
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流_2105209871988781057.json
hash: 551edadfc47aa804
coverage: 0.8
learned_at: 2026-10-21 00:43:11
nodes: [LoraLoaderModelOnly, RandomNoise, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, SamplerCustomAdvanced, Reroute, Reroute, MathExpression|pysssss, BasicGuider, StringFormat, CLIPLoader, ResolutionSelector, UNETLoader, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, VAEDecode, easy imageConcat, PreviewImage, CLIPLoader, QwenImage21Cache, TextEncodeQwenImage21, EmptyLatentImage, UNETLoader, QwenImage21Cache, KSampler, PrimitiveStringMultiline, TextGenerateLTX2Prompt, easy showAnything, JsonExtractString, VAELoader, VAEDecode, PreviewImage, SaveImage, SeedNode, LoadImage, MarkdownNote, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 231858906851573, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流_2105209871988781057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1｜5倍加速 _ 角色三视图工作流_2105209871988781057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `MathExpression|pysssss`
- `BasicGuider`
- `StringFormat`
- `CLIPLoader`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `VAEDecode` ★核心
- `easy imageConcat`
- `PreviewImage`
- `CLIPLoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `JsonExtractString`
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `SeedNode`
- `LoadImage`
- `MarkdownNote`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `231858906851573`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **80%**（32/40）

**有卡**：`LoraLoaderModelOnly`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`MathExpression|pysssss`、`BasicGuider`、`StringFormat`、`CLIPLoader`、`ResolutionSelector`、`UNETLoader`、`VAEDecode`、`easy imageConcat`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`JsonExtractString`、`VAELoader`、`SaveImage`、`SeedNode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
