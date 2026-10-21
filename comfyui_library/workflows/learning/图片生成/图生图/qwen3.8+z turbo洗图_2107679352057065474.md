---
key: 图片生成/图生图/qwen3.8+z turbo洗图_2107679352057065474.json
name: qwen3.8+z turbo洗图_2107679352057065474
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen3.8+z turbo洗图_2107679352057065474.json
hash: 19fc19e8044b6388
coverage: 0.882353
learned_at: 2026-10-21 00:46:19
nodes: [MarkdownNote, CLIPLoader, VAEDecode, llama_cpp_parameters, llama_cpp_model_loader, UNETLoader, ConditioningZeroOut, EmptySD3LatentImage, VAELoader, VAEEncode, llama_cpp_instruct_adv, PreviewAny, KSampler, CLIPTextEncode, SaveImage, ImageScaleToTotalPixels, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1047863189703998, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen3.8+z turbo洗图_2107679352057065474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen3.8+z turbo洗图_2107679352057065474.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAEDecode` ★核心
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `VAELoader`
- `VAEEncode` ★核心
- `llama_cpp_instruct_adv`
- `PreviewAny`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `ImageScaleToTotalPixels`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1047863189703998`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPLoader`、`VAEDecode`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`UNETLoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`VAELoader`、`VAEEncode`、`llama_cpp_instruct_adv`、`KSampler`、`CLIPTextEncode`、`SaveImage`、`ImageScaleToTotalPixels`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
