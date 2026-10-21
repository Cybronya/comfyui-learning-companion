---
key: 图片生成/文生图/Qwen2.1 文生图 turbo vs fusal vs 原生_2109541021666332674.json
name: Qwen2.1 文生图 turbo vs fusal vs 原生_2109541021666332674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1 文生图 turbo vs fusal vs 原生_2109541021666332674.json
hash: 9e79d1604eef4608
coverage: 0.911765
learned_at: 2026-10-21 02:54:41
nodes: [UNETLoader, CLIPLoader, VAELoader, INTConstant, TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, QwenImage21Cache, LoraLoaderModelOnly, UNETLoader, QwenImage21Cache, KSampler, VAEDecode, SaveImage, AddLabel, KSampler, VAEDecode, SaveImage, AddLabel, ManualSigmas, KSamplerSelect, SamplerCustom, VAEDecode, SaveImage, AddLabel, ImageConcatMulti, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), StringConstant, JoinStrings, StringConstantMultiline, INTConstant]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 20261011, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen2.1 文生图 turbo vs fusal vs 原生_2109541021666332674.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1 文生图 turbo vs fusal vs 原生_2109541021666332674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `ImageConcatMulti`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `StringConstant`
- `JoinStrings`
- `StringConstantMultiline`
- `INTConstant`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `20261011`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（31/34）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`INTConstant`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`KSampler`、`VAEDecode`、`SaveImage`、`AddLabel`、`ManualSigmas`、`KSamplerSelect`、`SamplerCustom`、`ImageConcatMulti`、`StringConstant`、`JoinStrings`、`StringConstantMultiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
