---
key: 图片生成/文生图/Qwen Image2.1 图像编辑_原生_FUN_Viggle_三图对比_2105245619081277442.json
name: Qwen Image2.1 图像编辑_原生_FUN_Viggle_三图对比_2105245619081277442
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图像编辑_原生_FUN_Viggle_三图对比_2105245619081277442.json
hash: 16fc8b91e6604ff0
coverage: 1
learned_at: 2026-10-10 20:58:55
nodes: [INTConstant, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, LoadImage, KSampler, LoraLoaderModelOnly, BasicGuider, RandomNoise, KSamplerSelect, CustomSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, VAEDecode, VAEDecode, SaveImage, ImageConcatMulti, SaveImage, LoadImage, ImageResizeKJv2, SaveImage, T8QwenImage21FunAccPDD4Step, INTConstant, INTConstant, StringConstantMultiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40}
---

# 图片生成/文生图/Qwen Image2.1 图像编辑_原生_FUN_Viggle_三图对比_2105245619081277442.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图像编辑_原生_FUN_Viggle_三图对比_2105245619081277442.json`

## 结构

**节点**（28 个）：
- `INTConstant`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect`
- `CustomSigmas`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `SaveImage`
- `VAEDecode`
- `VAEDecode`
- `SaveImage`
- `ImageConcatMulti`
- `SaveImage`
- `LoadImage`
- `ImageResizeKJv2`
- `SaveImage`
- `T8QwenImage21FunAccPDD4Step`
- `INTConstant`
- `INTConstant`
- `StringConstantMultiline`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `42`
- `steps` = `40`

## 知识

覆盖率 **100%**（28/28）

**有卡**：`INTConstant`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`、`KSampler`、`LoraLoaderModelOnly`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`CustomSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`ImageConcatMulti`、`ImageResizeKJv2`、`T8QwenImage21FunAccPDD4Step`、`StringConstantMultiline`
