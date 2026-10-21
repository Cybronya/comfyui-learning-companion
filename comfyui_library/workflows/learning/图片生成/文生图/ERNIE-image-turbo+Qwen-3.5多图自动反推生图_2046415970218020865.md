---
key: 图片生成/文生图/ERNIE-image-turbo+Qwen-3.5多图自动反推生图_2046415970218020865.json
name: ERNIE-image-turbo+Qwen-3.5多图自动反推生图_2046415970218020865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/ERNIE-image-turbo+Qwen-3.5多图自动反推生图_2046415970218020865.json
hash: 0f31775bcc44a5ae
coverage: 0.952381
learned_at: 2026-10-21 02:51:37
nodes: [KSampler, llama_cpp_parameters, LoadImage, llama_cpp_instruct_adv, LoadImage, llama_cpp_model_loader, ShowText|pysssss, LoadImage, 孤海图像组合批次, UNETLoader, VAELoader, ConditioningZeroOut, AspectRatio, EmptyFlux2LatentImage, Seed (rgthree), LayerUtility: PurgeVRAM V2, VAEDecode, CLIPTextEncode, CLIPLoader, UnetLoaderGGUF, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 288246259671698, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/ERNIE-image-turbo+Qwen-3.5多图自动反推生图_2046415970218020865.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/ERNIE-image-turbo+Qwen-3.5多图自动反推生图_2046415970218020865.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `KSampler` ★核心
- `llama_cpp_parameters`
- `LoadImage`
- `llama_cpp_instruct_adv`
- `LoadImage`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `LoadImage`
- `孤海图像组合批次`
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `AspectRatio`
- `EmptyFlux2LatentImage`
- `Seed (rgthree)`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UnetLoaderGGUF` ★核心
- `SaveImage`

## 关键参数

- `seed` = `288246259671698`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`KSampler`、`llama_cpp_parameters`、`LoadImage`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`孤海图像组合批次`、`UNETLoader`、`VAELoader`、`ConditioningZeroOut`、`AspectRatio`、`EmptyFlux2LatentImage`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`CLIPTextEncode`、`CLIPLoader`、`UnetLoaderGGUF`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
