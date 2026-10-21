---
key: 图片生成/图生图/CHIEFAI-千问IMAGE2.1电商换身换头工作流_2108359942859218946.json
name: CHIEFAI-千问IMAGE2.1电商换身换头工作流_2108359942859218946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/CHIEFAI-千问IMAGE2.1电商换身换头工作流_2108359942859218946.json
hash: 1ec734fcadef09a3
coverage: 0.842105
learned_at: 2026-10-21 00:38:51
nodes: [Anything Everywhere, Anything Everywhere, Anything Everywhere, VAEDecode, Get resolution [Crystools], VAELoader, EmptyLatentImage, CLIPLoader, RegexReplace, CLIPLoader, StringConcatenate, UNETLoader, KSampler, TextGenerate, PreviewImage, VAEDecode, VAELoader, VAEEncode, ReferenceLatent, VAEDecode, PreviewImage, SaveImage, LoraLoaderModelOnly, TextEncodeQwenImage21, ConditioningZeroOut, CLIPLoader, TextEncodeQwenImage21, CLIPTextEncode, KSampler, LoraLoaderModelOnly, LoadImage, LoadImage, PrimitiveStringMultiline, EmptyLatentImage, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 1024, "sampler_name": 1, "scheduler": "sa_solver", "seed": "disable", "steps": "randomize", "width": 1024}
---

# 图片生成/图生图/CHIEFAI-千问IMAGE2.1电商换身换头工作流_2108359942859218946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/CHIEFAI-千问IMAGE2.1电商换身换头工作流_2108359942859218946.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `Get resolution [Crystools]`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `RegexReplace`
- `CLIPLoader`
- `StringConcatenate`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `TextGenerate`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `ConditioningZeroOut`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `sa_solver`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`VAEDecode`、`Get resolution [Crystools]`、`VAELoader`、`EmptyLatentImage`、`CLIPLoader`、`RegexReplace`、`StringConcatenate`、`UNETLoader`、`KSampler`、`TextGenerate`、`VAEEncode`、`ReferenceLatent`、`SaveImage`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoadImage`、`KSamplerAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
