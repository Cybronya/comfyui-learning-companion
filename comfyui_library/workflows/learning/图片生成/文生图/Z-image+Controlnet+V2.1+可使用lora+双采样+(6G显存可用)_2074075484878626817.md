---
key: 图片生成/文生图/Z-image+Controlnet+V2.1+可使用lora+双采样+(6G显存可用)_2074075484878626817.json
name: Z-image+Controlnet+V2.1+可使用lora+双采样+(6G显存可用)_2074075484878626817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image+Controlnet+V2.1+可使用lora+双采样+(6G显存可用)_2074075484878626817.json
hash: a69f2098abe0eae3
coverage: 0.696429
learned_at: 2026-10-20 00:01:49
nodes: [CLIPLoader, MarkdownNote, Fast Groups Bypasser (rgthree), SaveImage, LayerUtility: ImageReelComposit, PreviewImage, easy imageIndexSwitch, MarkdownNote, AIO_Preprocessor, AIO_Preprocessor, SaveImage, MarkdownNote, SaveImage, VAEDecode, Reroute, LayerUtility: ImageReel, EmptyLatentImage, PreviewImage, Reroute, ConditioningZeroOut, VAELoader, Int, KSampler, PreviewImage, AIO_Preprocessor, easy cleanGpuUsed, LoraLoaderModelOnly, PreviewImage, KSampler, Reroute, ConditioningZeroOut, UNETLoader, SaveImage, LoraLoaderModelOnly, CLIPTextEncode, MarkdownNote, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2VideoUpscaler, easy int, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, Image Comparer (rgthree), VAEDecode, Int, Seed (rgthree), Seed (rgthree), ModelPatchLoader, MarkdownNote, QwenImageDiffsynthControlnet, AIO_Preprocessor, Image Comparer (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.6500000000000001, "height": 1920, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 309085686893418, "steps": 9, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image+Controlnet+V2.1+可使用lora+双采样+(6G显存可用)_2074075484878626817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image+Controlnet+V2.1+可使用lora+双采样+(6G显存可用)_2074075484878626817.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `CLIPLoader`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `easy imageIndexSwitch`
- `MarkdownNote`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `SaveImage`
- `MarkdownNote`
- `SaveImage`
- `VAEDecode` ★核心
- `Reroute`
- `LayerUtility: ImageReel`
- `EmptyLatentImage` ★核心
- `PreviewImage`
- `Reroute`
- `ConditioningZeroOut`
- `VAELoader`
- `Int`
- `KSampler` ★核心
- `PreviewImage`
- `AIO_Preprocessor`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `Reroute`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2VideoUpscaler`
- `easy int`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `Int`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `ModelPatchLoader`
- `MarkdownNote`
- `QwenImageDiffsynthControlnet`
- `AIO_Preprocessor`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1280`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `309085686893418`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.6500000000000001`

## 知识

覆盖率 **70%**（39/56）

**有卡**：`CLIPLoader`、`SaveImage`、`LayerUtility: ImageReelComposit`、`easy imageIndexSwitch`、`AIO_Preprocessor`、`VAEDecode`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`ConditioningZeroOut`、`VAELoader`、`Int`、`KSampler`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`easy int`、`LoadImage`、`Seed (rgthree)`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
