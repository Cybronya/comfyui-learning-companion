---
key: 图片生成/图生图/Z-image 一键洗图（Qwen3-VL反推+ControlNet控制+SeedVR2高清放大）_2013992293707026433.json
name: Z-image 一键洗图（Qwen3-VL反推+ControlNet控制+SeedVR2高清放大）_2013992293707026433
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image 一键洗图（Qwen3-VL反推+ControlNet控制+SeedVR2高清放大）_2013992293707026433.json
hash: 1672a02929b4628e
coverage: 0.888889
learned_at: 2026-10-23 11:30:20
nodes: [CLIPLoader, KSampler, UNETLoader, VAELoader, ConditioningZeroOut, EmptyLatentImage, LoadImage, ResizeImagesByLongerEdge, MathExpression|pysssss, GetImageSize, ShowText|pysssss, PreviewImage, ModelPatchLoader, AIO_Preprocessor, ModelSamplingAuraFlow, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, CLIPTextEncode, Qwen3_VQA, ZImageFunControlnet, SeedVR2LoadDiTModel, easy cleanGpuUsed, VAEDecode, PreviewImage, easy int, easy float]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 741856309952348, "steps": 9, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image 一键洗图（Qwen3-VL反推+ControlNet控制+SeedVR2高清放大）_2013992293707026433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image 一键洗图（Qwen3-VL反推+ControlNet控制+SeedVR2高清放大）_2013992293707026433.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `CLIPLoader`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ResizeImagesByLongerEdge`
- `MathExpression|pysssss`
- `GetImageSize`
- `ShowText|pysssss`
- `PreviewImage`
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `ModelSamplingAuraFlow`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `Qwen3_VQA`
- `ZImageFunControlnet`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `PreviewImage`
- `easy int`
- `easy float`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `741856309952348`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`CLIPLoader`、`KSampler`、`UNETLoader`、`VAELoader`、`ConditioningZeroOut`、`EmptyLatentImage`、`LoadImage`、`ResizeImagesByLongerEdge`、`MathExpression|pysssss`、`GetImageSize`、`ModelPatchLoader`、`AIO_Preprocessor`、`ModelSamplingAuraFlow`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`CLIPTextEncode`、`Qwen3_VQA`、`ZImageFunControlnet`、`SeedVR2LoadDiTModel`、`easy cleanGpuUsed`、`VAEDecode`、`easy int`、`easy float`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
