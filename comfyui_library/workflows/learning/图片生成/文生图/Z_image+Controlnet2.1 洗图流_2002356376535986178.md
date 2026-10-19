---
key: 图片生成/文生图/Z_image+Controlnet2.1 洗图流_2002356376535986178.json
name: Z_image+Controlnet2.1 洗图流_2002356376535986178
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z_image+Controlnet2.1 洗图流_2002356376535986178.json
hash: 3972dfa7a1c847de
coverage: 0.692308
learned_at: 2026-10-19 21:47:13
nodes: [Note, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, CLIPTextEncode, easy cleanGpuUsed, ModelSamplingAuraFlow, ImageScaleToTotalPixels, SeedVR2, AIO_Preprocessor, easy showAnything, VAEDecode, easy cleanGpuUsed, Reroute, KSampler, AIO_Preprocessor, CLIPTextEncode, VAELoader, PreviewImage, AIO_Preprocessor, AIO_Preprocessor, QwenImageDiffsynthControlnet, Reroute, SaveImage, AIO_Preprocessor, VAEEncode, ModelPatchLoader, UNETLoader, CLIPLoader, Image Comparer (rgthree), LoadImage, CR Prompt Text, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), PreviewImage, Fast Groups Bypasser (rgthree), Qwen3_VQA]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 453095432634353, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z_image+Controlnet2.1 洗图流_2002356376535986178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z_image+Controlnet2.1 洗图流_2002356376535986178.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `Note`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `SeedVR2`
- `AIO_Preprocessor`
- `easy showAnything`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Reroute`
- `KSampler` ★核心
- `AIO_Preprocessor`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PreviewImage`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `Reroute`
- `SaveImage`
- `AIO_Preprocessor`
- `VAEEncode` ★核心
- `ModelPatchLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `LoadImage`
- `CR Prompt Text`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Qwen3_VQA`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `453095432634353`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`SaveImage`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`CLIPTextEncode`、`easy cleanGpuUsed`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`SeedVR2`、`AIO_Preprocessor`、`VAEDecode`、`KSampler`、`VAELoader`、`QwenImageDiffsynthControlnet`、`VAEEncode`、`ModelPatchLoader`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`CR Prompt Text`、`Qwen3_VQA`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、QwenImageDiffsynthControlnet

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
