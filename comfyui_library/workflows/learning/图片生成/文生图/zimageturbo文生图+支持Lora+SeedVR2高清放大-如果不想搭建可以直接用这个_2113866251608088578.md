---
key: 图片生成/文生图/zimageturbo文生图+支持Lora+SeedVR2高清放大-如果不想搭建可以直接用这个_2113866251608088578.json
name: zimageturbo文生图+支持Lora+SeedVR2高清放大-如果不想搭建可以直接用这个_2113866251608088578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/zimageturbo文生图+支持Lora+SeedVR2高清放大-如果不想搭建可以直接用这个_2113866251608088578.json
hash: db65e486010752f2
coverage: 0.95
learned_at: 2026-10-26 22:09:14
nodes: [SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), SaveImage, VAELoader, EmptySD3LatentImage, INTConstant, Power Lora Loader (rgthree), CLIPTextEncode, VAEDecode, KSampler, ModelSamplingAuraFlow, CLIPTextEncode, LoaderGGUF, CLIPLoader, ClipLoaderGGUF, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 775667057861770, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/zimageturbo文生图+支持Lora+SeedVR2高清放大-如果不想搭建可以直接用这个_2113866251608088578.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/zimageturbo文生图+支持Lora+SeedVR2高清放大-如果不想搭建可以直接用这个_2113866251608088578.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `VAELoader`
- `EmptySD3LatentImage`
- `INTConstant`
- `Power Lora Loader (rgthree)`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `LoaderGGUF`
- `CLIPLoader`
- `ClipLoaderGGUF`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `775667057861770`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2GGUF`、`INTConstant`、`SaveImage`、`VAELoader`、`EmptySD3LatentImage`、`Power Lora Loader (rgthree)`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`ModelSamplingAuraFlow`、`LoaderGGUF`、`CLIPLoader`、`ClipLoaderGGUF`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、SeedVR2BlockSwap、SeedVR2ExtraArgs

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
