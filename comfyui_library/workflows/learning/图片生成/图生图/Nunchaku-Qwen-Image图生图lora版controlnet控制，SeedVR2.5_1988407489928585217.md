---
key: 图片生成/图生图/Nunchaku-Qwen-Image图生图lora版controlnet控制，SeedVR2.5_1988407489928585217.json
name: Nunchaku-Qwen-Image图生图lora版controlnet控制，SeedVR2.5_1988407489928585217
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image图生图lora版controlnet控制，SeedVR2.5_1988407489928585217.json
hash: 9183e7c90ef538bf
coverage: 0.842105
learned_at: 2026-10-23 11:10:01
nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ttN concat, Qwen3_VQA, ModelSamplingAuraFlow, CFGNorm, KSampler, ControlNetApplyAdvanced, SetUnionControlNetType, EmptyLatentImage, easy showAnything, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, AIO_Preprocessor, easy imageConcat, easy imageConcat, NunchakuQwenImageLoraStack, SaveImage, SeedVR2VideoUpscaler, NunchakuQwenImageLoraStack, LayerUtility: PurgeVRAM, CR Text, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, VAEDecode, VAELoader, NunchakuQwenImageDiTLoader, ControlNetLoader, PreviewImage, MultiplePathsInput, ImageLoader, SaveImage, Image Comparer (rgthree), SaveImage, Image Comparer (rgthree), PrimitiveInt, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 797202686993305, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku-Qwen-Image图生图lora版controlnet控制，SeedVR2.5_1988407489928585217.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku-Qwen-Image图生图lora版controlnet控制，SeedVR2.5_1988407489928585217.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ttN concat`
- `Qwen3_VQA`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `EmptyLatentImage` ★核心
- `easy showAnything`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `AIO_Preprocessor`
- `easy imageConcat`
- `easy imageConcat`
- `NunchakuQwenImageLoraStack`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `NunchakuQwenImageLoraStack`
- `LayerUtility: PurgeVRAM`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VAELoader`
- `NunchakuQwenImageDiTLoader`
- `ControlNetLoader`
- `PreviewImage`
- `MultiplePathsInput`
- `ImageLoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PrimitiveInt`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `797202686993305`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（32/38）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ttN concat`、`Qwen3_VQA`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`ControlNetApplyAdvanced`、`SetUnionControlNetType`、`EmptyLatentImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`AIO_Preprocessor`、`easy imageConcat`、`NunchakuQwenImageLoraStack`、`SaveImage`、`SeedVR2VideoUpscaler`、`LayerUtility: PurgeVRAM`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`VAELoader`、`NunchakuQwenImageDiTLoader`、`ControlNetLoader`、`MultiplePathsInput`、`ImageLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、ControlNetApplyAdvanced

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
