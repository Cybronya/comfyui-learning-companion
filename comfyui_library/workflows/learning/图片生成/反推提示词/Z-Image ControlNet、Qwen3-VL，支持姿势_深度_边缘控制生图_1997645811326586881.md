---
key: 图片生成/反推提示词/Z-Image ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1997645811326586881.json
name: Z-Image ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1997645811326586881
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Z-Image ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1997645811326586881.json
hash: 49a0748af47ad785
coverage: 0.857143
learned_at: 2026-10-26 01:46:35
nodes: [VAELoader, MarkdownNote, ConditioningZeroOut, QwenImageDiffsynthControlnet, CLIPTextEncode, KSampler, ImageConcanate, PreviewImage, ModelSamplingAuraFlow, SaveImage, VAEDecode, SaveImage, Qwen3_VQA, Label (rgthree), LoadImage, PreviewAny, EmptySD3LatentImage, UNETLoader, ModelPatchLoader, CLIPLoader, AIO_Preprocessor]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 556649315301055, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Z-Image ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1997645811326586881.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Z-Image ControlNet、Qwen3-VL，支持姿势_深度_边缘控制生图_1997645811326586881.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `VAELoader`
- `MarkdownNote`
- `ConditioningZeroOut`
- `QwenImageDiffsynthControlnet`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageConcanate`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Qwen3_VQA`
- `Label (rgthree)`
- `LoadImage`
- `PreviewAny`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `CLIPLoader`
- `AIO_Preprocessor`

## 关键参数

- `seed` = `556649315301055`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`QwenImageDiffsynthControlnet`、`CLIPTextEncode`、`KSampler`、`ImageConcanate`、`ModelSamplingAuraFlow`、`SaveImage`、`VAEDecode`、`Qwen3_VQA`、`Label (rgthree)`、`LoadImage`、`EmptySD3LatentImage`、`UNETLoader`、`ModelPatchLoader`、`CLIPLoader`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
