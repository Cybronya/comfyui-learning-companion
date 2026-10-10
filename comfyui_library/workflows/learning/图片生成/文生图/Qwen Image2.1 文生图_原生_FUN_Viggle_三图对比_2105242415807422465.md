---
key: Qwen Image2.1 文生图_原生_FUN_Viggle_三图对比_2105242415807422465.json
name: Qwen Image2.1 文生图_原生_FUN_Viggle_三图对比_2105242415807422465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 文生图_原生_FUN_Viggle_三图对比_2105242415807422465.json
hash: 207c2b5b23dd5e99
coverage: 1
learned_at: 2026-10-10 20:58:55
nodes: [StringConstantMultiline, INTConstant, INTConstant, INTConstant, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, KSampler, LoraLoaderModelOnly, BasicGuider, RandomNoise, KSamplerSelect, CustomSigmas, SamplerCustomAdvanced, VAEDecode, VAEDecode, VAEDecode, SaveImage, T8QwenImage21FunAccPDD4Step, SaveImage, AddLabel, SaveImage, AddLabel, SaveImage, AddLabel, ImageConcatMulti]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# Qwen Image2.1 文生图_原生_FUN_Viggle_三图对比_2105242415807422465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 文生图_原生_FUN_Viggle_三图对比_2105242415807422465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `StringConstantMultiline`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CustomSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `T8QwenImage21FunAccPDD4Step`
- `SaveImage`
- `AddLabel`
- `SaveImage`
- `AddLabel`
- `SaveImage`
- `AddLabel`
- `ImageConcatMulti`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`StringConstantMultiline`、`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`LoraLoaderModelOnly`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`CustomSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`T8QwenImage21FunAccPDD4Step`、`AddLabel`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、UNETLoader
