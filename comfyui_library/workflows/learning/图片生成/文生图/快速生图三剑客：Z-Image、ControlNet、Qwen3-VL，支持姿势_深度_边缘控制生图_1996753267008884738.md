---
key: 图片生成/文生图/快速生图三剑客：Z-Image、ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1996753267008884738.json
name: 快速生图三剑客：Z-Image、ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1996753267008884738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/快速生图三剑客：Z-Image、ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1996753267008884738.json
hash: f125f9533a6ace8f
coverage: 0.857143
learned_at: 2026-10-19 21:33:31
nodes: [CLIPLoader, VAELoader, UNETLoader, MarkdownNote, ModelPatchLoader, ConditioningZeroOut, QwenImageDiffsynthControlnet, CLIPTextEncode, KSampler, ImageConcanate, LoadImage, PreviewImage, EmptySD3LatentImage, PreviewAny, ModelSamplingAuraFlow, SaveImage, VAEDecode, SaveImage, AIO_Preprocessor, Qwen3_VQA, Label (rgthree)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 262191091028028, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/快速生图三剑客：Z-Image、ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1996753267008884738.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/快速生图三剑客：Z-Image、ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1996753267008884738.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `ModelPatchLoader`
- `ConditioningZeroOut`
- `QwenImageDiffsynthControlnet`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageConcanate`
- `LoadImage`
- `PreviewImage`
- `EmptySD3LatentImage`
- `PreviewAny`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `AIO_Preprocessor`
- `Qwen3_VQA`
- `Label (rgthree)`

## 关键参数

- `seed` = `262191091028028`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelPatchLoader`、`ConditioningZeroOut`、`QwenImageDiffsynthControlnet`、`CLIPTextEncode`、`KSampler`、`ImageConcanate`、`LoadImage`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`SaveImage`、`VAEDecode`、`AIO_Preprocessor`、`Qwen3_VQA`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
